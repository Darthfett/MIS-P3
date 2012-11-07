import colorsys

color_spaces = {"rgb", "yuv", "hsv"}

def RGB_to_RGB(*pixel):
    return pixel

def RGB_to_YUV(r, g, b):
    y =  0.299 * r +  0.587 * g +  0.144 * b
    u = -0.299 * r + -0.587 * g +  0.886 * b
    v =  0.701 * r + -0.587 * g + -0.114 * b
    return (y, u, v)

def YUV_to_RGB(y, u, v):
    r = y + 1.14 * v
    g = y - 0.394 * u - 0.581 * u
    b = y + 2.028 * u
    return (r, g, b)

RGB_to_color_space_converter = {
    "rgb": RGB_to_RGB,
    "yuv": RGB_to_YUV,
    "hsv": colorsys.rgb_to_hsv,
}

color_space_to_RGB_converter = {
    "rgb": RGB_to_RGB,
    "yuv": YUV_to_RGB,
    "hsv": colorsys.hsv_to_rgb,
}

def convert_pixel(pixel, from_color_space, to_color_space):
    if from_color_space not in color_spaces:
        raise ValueError("Invalid color space {}".format(from_color_space))
    if to_color_space not in color_spaces:
        raise ValueError("Invalid color space {}".format(to_color_space))

    if from_color_space != "rgb":
        pixel = color_space_to_RGB_converter[from_color_space](*pixel)

    if to_color_space != "rgb":
        pixel = RGB_to_color_space_converter[to_color_space](*pixel)

    return pixel