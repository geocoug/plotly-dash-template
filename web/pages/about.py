#!/usr/bin/env python

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path="/about", name="About", order=1)


def grid() -> list:
    return [
        dbc.Row(
            "Another page here...",
            className="p-3 m-3 justify-content-center",
        ),
    ]


layout = (
    html.Div(
        [
            dcc.Location(id="url", refresh=False),
            dcc.Loading(
                children=grid(),
                type="dot",
            ),
        ],
    ),
)
