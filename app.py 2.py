# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:24:39 2022

@author: nizar
"""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Nizar',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data. Pretty cool! 😎 ', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'})

#The style property in HTML is a semicolon-separated string. In Dash, you can just supply a dictionary.
#The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
#The HTML class attribute is className in Dash.
#The children of the HTML tag is specified through the children keyword argument. By convention, this is always the first argument and so it is often omitted.