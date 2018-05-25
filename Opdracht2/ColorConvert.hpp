//Convert between RGB and CMY
float* RGBtoCMY(float r, float g, float b);
float* CMYtoRGB(float c, float m, float y);

//Convert between RGB and HSL
float* RGBtoHSL(float r, float g, float b);
float* HSLtoRGB(float h, float s, float l);

//Extra method to convert between CMY and HSL
//It uses the methods stated below
float* CMYtoHSL(float c, float m, float y);
float* HSLtoCMY(float h, float s, float l);


//Extra methods which take a float array
//This way methods can be used inside eachother:
//`RGBtoHSL(CMYtoRGB(c, m, y));` = `CMYtoHSL(c, m, y)`
float* RGBtoCMY(float rgb[3]);
float* CMYtoRGB(float cmy[3]);
float* RGBtoHSL(float rgb[3]);
float* HSLtoRGB(float hsl[3]);
float* CMYtoHSL(float cmy[3]);
float* HSLtoCMY(float hsl[3]);



//Calculate RGB value from a transparent colored area on an opaque colored area
float* transparency(float r1, float g1, float b1, float a, float r2, float g2, float b2);
