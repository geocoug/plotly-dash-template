#!/usr/bin/env python

import random

import dash
from dash import Input, Output

from web.utils import ColorGradient


@dash.callback(
    Output("example-btn-output", "style"),
    Output("example-btn-output", "className"),
    Input("example-btn", "n_clicks"),
)
def button_clicked(click):
    if click:
        start_hex = ColorGradient.rgb_to_hex(
            rgb=[
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ],
        )
        end_hex = ColorGradient.rgb_to_hex(
            rgb=[
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ],
        )
        colors = ", ".join(
            ColorGradient(start_hex, end_hex, n=10).linear_gradient()["hex"],
        )
        return (
            {
                "background-image": f"linear-gradient(to right, {colors})",
                "min-height": "250px",
            },
            "border rounded border-dark",
        )
    return dash.no_update, dash.no_update
