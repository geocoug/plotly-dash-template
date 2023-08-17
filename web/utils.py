#!/usr/bin/env python


class ColorGradient:
    """Create a gradient between two colors.

    Example usage:

    gradient = ColorGradient(
        start_hex="#db641f",
        finish_hex="#FFFFFF",
        n=10
        ).linear_gradient()
    """

    def __init__(
        self: "ColorGradient",
        start_hex: str,
        finish_hex: str,
        n: int,
    ) -> None:
        """Create a gradient that is (n) steps between two colors.

        Args:
        ----
            start_hex (str): Starting hexidecimal color code.
            finish_hex (str): Ending hexidecimal color code.
            n (int): Number of gradient steps between the starting and
            ending hexidecimal colors.
        """
        self.start_hex = start_hex
        self.finish_hex = finish_hex
        self.n = n

    @classmethod
    def hex_to_rgb(cls, hex: str) -> list[int]:
        """Convert a hexidecimal code to RGB (#FFFFFF -> [255,255,255]).

        Args:
        ----
            hex (str): Hexidecimal color code.

        Returns
        -------
            list[int]: List of red, green, and blue color values.
        """
        return [int(hex[i : i + 2], 16) for i in range(1, 6, 2)]

    @classmethod
    def rgb_to_hex(cls, rgb: list[int]) -> str:
        """Convert RGB to a hexidecimal code ([255,255,255] -> #FFFFFF).

        Args:
        ----
            rgb (list): List of red, green, and blue color values.

        Returns
        -------
            list[int]: Hexidecimal color code.
        """
        rgb = [int(x) for x in rgb]
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb],
        )

    def color_dict(self: "ColorGradient", gradient: list) -> dict:
        """Takes in a list of RGB sub-lists and returns dictionary of colors
        in RGB and hex form for use in a graphing function defined later on.

        Args:
        ----
            gradient (list): List of red, green, and blue color values.

        Returns
        -------
            dict: Dictionary containing RGB and hexidecimal codes
            of the generated color gradient.
        """
        return {
            "hex": [self.rgb_to_hex(rgb) for rgb in gradient],
            "rgb": gradient,
            "r": [rgb[0] for rgb in gradient],
            "g": [rgb[1] for rgb in gradient],
            "b": [rgb[2] for rgb in gradient],
        }

    def linear_gradient(self: "ColorGradient") -> dict:
        """Returns a gradient list of (n) colors between two hex colors.

        start_hex and finish_hex should be the full six-digit color string,
        inlcuding the number sign (#FFFFFF).

        Returns
        -------
            dict: Dictionary containing RGB and hexidecimal codes
            of the generated color gradient.
        """
        # Starting and ending colors in RGB form
        s = self.hex_to_rgb(self.start_hex)
        f = self.hex_to_rgb(self.finish_hex)
        # Initilize a list of the output colors with the starting color
        rgb_list = [s]
        # Calcuate a color at each evenly spaced value of t from 1 to n
        for t in range(1, self.n):
            # Interpolate RGB vector for color at the current value of t
            curr_vector = [
                int(s[j] + (float(t) / (self.n - 1)) * (f[j] - s[j])) for j in range(3)
            ]
            # Add it to our list of output colors
            rgb_list.append(curr_vector)
        return self.color_dict(rgb_list)
