import os
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.Div(children='''
        Sumbol to graph:
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output_graph')
    
    ])

@app.callback(
    Output(component_id='output_graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):

    try:
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.get_data_yahoo(input_data, start, end)

        return dcc.Graph(
                id='example_graph', 
                figure={
                    'data': [
                        {'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data},
                    ],
                    'layout': {
                        'title':input_data
                    }
                })
    except:
        return "Cannot find data of " + input_data

server = app.server
dev_server = app.run_server




