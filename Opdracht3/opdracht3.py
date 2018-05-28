#!/usr/bin/python3

import math
import glfw
import sys

from OpenGL.GL import *



# Constants
# Size of one pixel
PX_SIZE = 10
# Size of window in PX_SIZE
WINDOW_W = 64
WINDOW_H = 32
# Smallest dimension, for the rotating line function
WINDOW_C = WINDOW_H if WINDOW_H < WINDOW_W else WINDOW_H



# Array of current points as tuple(x, y, color)
points = []



# Draw grid, stolen from 'grid.py'(found on N@tschool)
def draw_grid():
    # Set line color
    glColor(0.5, 0.5, 0.5)

    # Draw lines
    glBegin(GL_LINES)
    for x in range(1, WINDOW_W):
        glVertex(x * PX_SIZE, 0)
        glVertex(x * PX_SIZE, WINDOW_H * PX_SIZE)
    for y in range(1, WINDOW_H):
        glVertex(0, y * PX_SIZE)
        glVertex(WINDOW_W * PX_SIZE, y * PX_SIZE)
    glEnd()
    glFlush()


# Draw points, stolen from 'grid.py'(found on N@tschool)
def draw_points():
    for point in points:
        # Unpack point values
        ( x, y, color ) = point

        # Set point color
        glColor(color, color, color)

        # Draw quad
        glBegin(GL_QUADS)
        glVertex(x * PX_SIZE, y * PX_SIZE)
        glVertex((x + 1) * PX_SIZE, y * PX_SIZE)
        glVertex((x + 1) * PX_SIZE, (y + 1) * PX_SIZE)
        glVertex(x * PX_SIZE, (y + 1) * PX_SIZE)
        glEnd()



# Extra functions for rasterline_aa()
def ipart(x):
    return math.floor(x)

def fpart(x):
    return x - ipart(x)

def rfpart(x):
    return 1 - fpart(x)


# Draw an antialiased line on the grid using "Xiaolin Wu's line algorithm"
# https://en.wikipedia.org/wiki/Xiaolin_Wu%27s_line_algorithm
def rasterline_aa(x1, y1, x2, y2):
    # Check if line is steep, if it is, swap x and y
    steep = abs(y2 - y1) > abs(x2 - x1)
    if steep:
        ( x1, y1, x2, y2 ) = ( y1, x1, y2, x2 )

    # If first coordinate more right than second, swap them
    if x1 > x2:
        ( x1, x2, y1, y2 ) = ( x2, x1, y2, y1 )

    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1
    gradient = 1 if dx == 0 else dy / dx

    # Calculate first end point
    x_end = round(x1)
    y_end = y1 + gradient * (x_end - x1)
    x_gap = rfpart(x1 + 0.5)
    x_pixel1 = x_end
    y_pixel1 = ipart(y_end)

    # "Draw" first end point
    if steep:
        points.append(( y_pixel1, x_pixel1, rfpart(y_end) * x_gap ))
        points.append(( y_pixel1 + 1, x_pixel1, fpart(y_end) * x_gap ))
    else:
        points.append(( x_pixel1, y_pixel1, rfpart(y_end) * x_gap ))
        points.append(( x_pixel1, y_pixel1 + 1, fpart(y_end) * x_gap ))

    # Set first y intersection
    y_intersect = y_end + gradient

    # Calculate second end point
    x_end = round(x2)
    y_end = y2 + gradient * (x_end - x2)
    x_gap = fpart(x2 + 0.5)
    x_pixel2 = x_end
    y_pixel2 = ipart(y_end)

    # "Draw" second end point
    if steep:
        points.append(( y_pixel2, x_pixel2, rfpart(y_end) * x_gap ))
        points.append(( y_pixel2 + 1, x_pixel2, fpart(y_end) * x_gap ))
    else:
        points.append(( x_pixel2, y_pixel2, rfpart(y_end) * x_gap ))
        points.append(( x_pixel2, y_pixel2 + 1, fpart(y_end) * x_gap ))

    # Loop pixels
    for x in range(x_pixel1 + 1, x_pixel2):
        if steep:
            points.append(( ipart(y_intersect), x, rfpart(y_intersect) ))
            points.append(( ipart(y_intersect) + 1, x, fpart(y_intersect) ))
        else:
            points.append(( x, ipart(y_intersect), rfpart(y_intersect) ))
            points.append(( x, ipart(y_intersect) + 1, fpart(y_intersect) ))

        y_intersect += gradient


# Draw a line on the grid, from (x1,y1) to (x2,y2), aa will enable antialiasing
def rasterline(x1, y1, x2, y2, aa=True):
    if aa: # Send data to antialias function
        rasterline_aa(x1, y1, x2, y2)
    else:
        if round(x1) == round(x2): # Vertical line
            if y1 > y2:
                ( y1, y2 ) = ( y2, y1 )

            for y in range(round(y1), round(y2)):
                points.append(( round(x1), y, 1.0 ))
        elif round(y1) == round(y2): # Horizontal line
            if x1 > x2:
                ( x1, x2 ) = ( x2, x1 )

            for x in range(round(x1), round(x2)):
                points.append(( x, round(y1), 1.0 ))
        else:
            # Calculate steepness
            steepness = (y2 - y1) / (x2 - x1)

            if steepness > 1 or steepness < -1: # Calculate points from top to bottom
                for y in range(round(y1), round(y2), -1 if y1 > y2 else 1):
                    points.append(( round(1 / steepness * (y - y1)) + round(x1), y, 1.0 ))
            else: # Calculate points from left to right
                for x in range(round(x1), round(x2), -1 if x1 > x2 else 1):
                    points.append(( x, round(steepness * (x - x1)) + round(y1), 1.0 ))


# Draw a line from center to a point on a circle, aa will enable antialiasing
def rotateline(a, aa=True):
    # Convert degrees to radians for sin and cos functions
    rad = math.radians(a)
    rasterline(WINDOW_W / 2, WINDOW_H / 2, WINDOW_W / 2 + WINDOW_C / 2 * math.cos(rad), WINDOW_H / 2 + WINDOW_C / 2 * math.sin(rad), aa)



if __name__ == '__main__':
    # Initialize GLFW, exit on fail
    if not glfw.init():
        print('Failed to initialize GLFW')
        sys.exit(1)

    # Create window, exit on fail
    window = glfw.create_window(WINDOW_W * PX_SIZE, WINDOW_H * PX_SIZE, 'Opdracht 3', None, None)
    if not window:
        print('Failed to create GLFW window')
        glfw.terminate()
        sys.exit(2)

    # Tell OpenGL to use this window and show it
    glfw.make_context_current(window)

    # Set space where OpenGL can draw to
    glOrtho(0, WINDOW_W * PX_SIZE, WINDOW_H * PX_SIZE, 0, -1, 1)

    # Current angle for rotating line
    a = 0

    while not glfw.window_should_close(window):
        # Poll for mouse/key/other events
        glfw.poll_events()

        # Clear window and points
        glClear(GL_COLOR_BUFFER_BIT)
        points.clear()

        #############################################
        # Add rasterline(x1, y1, x2, y2) calls here #
        # or use rotateline(a) for a rotating line  #
        #############################################
        rotateline(a)
        rasterline(4, 4, 16, 12)
        rasterline(4, 8, 16, 16, False)

        # Draw points and grid
        draw_points()
        draw_grid()

        # Swap buffer
        glfw.swap_buffers(window)

        # Update angle
        a = (a + 1 % 360)

    # Terminate GLFW
    glfw.terminate()
