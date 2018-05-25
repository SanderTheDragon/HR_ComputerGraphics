#include "ColorConvert.hpp"

#include <algorithm>
#include <cmath>

float* RGBtoCMY(float r, float g, float b)
{
	float* cmy = new float[3];

	//Cyan
	//A higher red means a lower cyan
	cmy[0] = 1.0f - r;

	//Magenta
	//A higher green means a lower magenta
	cmy[1] = 1.0f - g;

	//Yellow
	//A higher blue means a lower yellow
	cmy[2] = 1.0f - b;

	return cmy;
}

float* CMYtoRGB(float c, float m, float y)
{
	//See `RGBtoCMY`, this is that, only the other way around

	float* rgb = new float[3];

	//Red
	rgb[0] = 1.0f - c;

	//Green
	rgb[1] = 1.0f - m;

	//Blue
	rgb[2] = 1.0f - y;

	return rgb;
}


float* RGBtoHSL(float r, float g, float b)
{
	//If the color is a shade of gray
	if (r == g && g == b)
	{
		//Gray in HSL has no hue or saturation, only lightness
		//Lightness can also be G or B
		return new float[3]{ 0.0f, 0.0f, r };
	}

	//See 'HSL-kleurruimte.pdf'(found on N@tschool) for more information

	//Get minimum and maximum from RGB
	float min = std::min({ r, g, b });
	float max = std::max({ r, g, b });

	float* hsl = new float[3];

	//Hue
	hsl[0] = 0.0f;

	//Calculate based on minimum and maximum
	if (b == min && r == max)
	{
		hsl[0] = (g - min) / (max - min) * 60.0f;
	}
	else if (b == min && g == max)
	{
		hsl[0] = (max - r) / (max - min) * 60.0f + 60.0f;
	}
	else if (r == min && g == max)
	{
		hsl[0] = (b - min) / (max - min) * 60.0f + 120.0f;
	}
	else if (r == min && b == max)
	{
		hsl[0] = (max - g) / (max - min) * 60.0f + 180.0f;
	}
	else if (g == min && b == max)
	{
		hsl[0] = (r - min) / (max - min) * 60.0f + 240.0f;
	}
	else if (g == min && r == max)
	{
		hsl[0] = (max - b) / (max - min) * 60.0f + 300.0f;
	}

	//Saturation
	hsl[1] = (max - min) / (1.0f - std::abs(min + max - 1.0f));

	//Lightness
	hsl[2] = (min + max) / 2.0f;

	return hsl;
}

//Extra function since the same code is required 3 times
float B(float h, float min, float max)
{
	//See 'HSL-kleurruimte.pdf'(found on N@tschool) for more information

	if (h < 0)
	{
		h += 360.0f;
	}

	h = fmod(h, 360.0f);

	if (h >= 0.0f && h < 120.0f)
	{
		return min;
	}
	else if (h >= 120.0f && h < 180.0f)
	{
		return min + (max - min) * ((h - 120.0f) / 60.0f);
	}
	else if (h >= 180.0f && h < 300.0f)
	{
		return max;
	}
	else if (h >= 300.0f && h < 360.0f)
	{
		return max - (max - min) * ((h - 300.0f) / 60.0f);
	}
}

float* HSLtoRGB(float h, float s, float l)
{
	//If the color is a shade of gray
	if (h == 0 && s == 0)
	{
		//See `RGBtoHSL` (first 'if' block)
		return new float[3]{ l, l, l };
	}

	float min = l + s * std::abs(l - 0.5f) - 0.5f * s;
	float max = l - s * std::abs(l - 0.5f) + 0.5f * s;

	float* rgb = new float[3];

	//See 'HSL-kleurruimte.pdf'(found on N@tschool) for more information

	//Red
	rgb[0] = B(h - 120.0f, min, max);

	//Green
	rgb[1] = B(h + 120.0f, min, max);

	//Blue
	rgb[2] = B(h, min, max);

	return rgb;
}


//Convert CMY and HSL using the previous methods
float* CMYtoHSL(float c, float m, float y)
{
	return RGBtoHSL(CMYtoRGB(c, m, y));
}

float* HSLtoCMY(float h, float s, float l)
{
	return RGBtoCMY(HSLtoRGB(h, s, l));
}


float* RGBtoCMY(float rgb[3]) { return RGBtoCMY(rgb[0], rgb[1], rgb[2]); }
float* CMYtoRGB(float cmy[3]) { return CMYtoRGB(cmy[0], cmy[1], cmy[2]); }
float* RGBtoHSL(float rgb[3]) { return RGBtoHSL(rgb[0], rgb[1], rgb[2]); }
float* HSLtoRGB(float hsl[3]) { return HSLtoRGB(hsl[0], hsl[1], hsl[2]); }
float* CMYtoHSL(float cmy[3]) { return RGBtoHSL(CMYtoRGB(cmy)); }
float* HSLtoCMY(float hsl[3]) { return RGBtoCMY(HSLtoRGB(hsl)); }



float* transparency(float r1, float g1, float b1, float a, float r2, float g2, float b2)
{
	float* rgb = new float[3];

	//Make RGB1 'transparent'
	r1 *= a;
	g1 *= a;
	b1 *= a;

	//Make RGB2 also 'transparent'
	//so that the transparencies(a) of the areas combined is 1
	r2 *= (1.0f - a);
	g2 *= (1.0f - a);
	b2 *= (1.0f - a);

	//Add the together
	rgb[0] = r1 + r2;
	rgb[1] = g1 + g2;
	rgb[2] = b1 + b2;

	return rgb;
}
