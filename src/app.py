# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:54:04 2024

@author: a.smit
"""

from dash import Dash, html, dcc
import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import logging

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Define the style for the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "font-family": "Arial", 
}

# Define the style for the content area
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

LINK_STYLE = {
    "color": "black",  # Setting text color to black
    "text-decoration": "none",
    "font-family": "Arial",
    "font-size": "20px"
    }

pages_links = [html.Div([dcc.Link(page['name'], href=page["relative_path"], className="nav-link", style=LINK_STYLE)],
    className="nav-item") for page in dash.page_registry.values()]

# Sidebar layout
sidebar = html.Div(
    [html.H2("Navigatie", className="display-4"),
     html.Hr(),
     ] + pages_links,
    style=SIDEBAR_STYLE,
)

# Main content area layout
content = html.Div([
    dash.page_container
])

# Final layout
app.layout = html.Div([
        dcc.Location(id="url"),
        dcc.Store(id='data-store-warmte-ventilatie'),
        dcc.Store(id='data-store-gb'),
        dbc.Row(
            [
                dbc.Col(sidebar, md=2, className="mt-5", style={'position': 'fixed'}),  # 'mt-5' adds margin-top, 'fixed' keeps it on the side
                dbc.Col(content, md={'size': 10, 'offset': 2})    # 'offset=2' shifts the content to the right of the sidebar
            ],
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=False)

    