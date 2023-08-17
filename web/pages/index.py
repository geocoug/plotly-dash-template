#!/usr/bin/env python

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path="/", name="Home", order=0)


def grid() -> list:
    return [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Row(
                        dbc.Button(
                            "Click me!",
                            id="example-btn",
                        ),
                    ),
                    className="mx-3 col-md-4 col-lg-3 col-12",
                ),
                dbc.Col(
                    dbc.Row(
                        id="example-btn-output",
                        className="d-hidden",
                    ),
                    className="mx-3 col-md-7 col-lg-8 col-12",
                ),
            ],
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
