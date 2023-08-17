#!/usr/bin/env python

import dash
import dash_bootstrap_components as dbc
from dash import Dash, html

import web.callbacks  # noqa

app = Dash(
    __name__,
    title="Dashboard",
    assets_folder="assets",
    use_pages=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1",
        },
    ],
)

app.layout = html.Div(
    [
        dbc.NavbarSimple(
            [
                dbc.NavItem(dbc.NavLink(page["name"], href=page["relative_path"]))
                for page in dash.page_registry.values()
            ],
            color="dark",
            dark=True,
            brand=html.Img(
                src="assets/logo.svg",
                height="36px",
            ),
            brand_href="#",
            links_left=True,
            expand="md",
            fluid=True,
        ),
        dash.page_container,
    ],
    id="container",
)


dashboard = app.server


if __name__ == "__main__":
    app.run(debug=True)
