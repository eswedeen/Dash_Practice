import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

bar1 = dcc.Graph(
    id='bar1',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            {'x': [1, 2, 3], 'y': [7, 9, 5], 'type': 'bar', 'name': 'AZ'}
        ],
        'layout': {
            'title': 'Dash Data Visualization 1',
            'plot_bgcolor': '#0F1536',
            'paper_bgcolor': '#0F1536',
            'height':'300',
            'font': {
                'color': 'white'
            }
        }
    }
)

bar2 = dcc.Graph(
    id='bar2',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            {'x': [1, 2, 3], 'y': [7, 9, 5], 'type': 'bar', 'name': 'AZ'}
        ],
        'layout': {
            'title': 'Dash Data Visualization 2',
            'plot_bgcolor': '#0F1536',
            'paper_bgcolor': '#0F1536',
            'height':'300',
            'font': {
                'color': 'white'
            }
        }
    }
)

bar3 = dcc.Graph(
    id='bar3',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            {'x': [1, 2, 3], 'y': [7, 9, 5], 'type': 'bar', 'name': 'AZ'}
        ],
        'layout': {
            'title': 'Dash Data Visualization 3',
            'plot_bgcolor': '#0F1536',
            'paper_bgcolor': '#0F1536',
            'height':'300',
            'font': {
                'color': 'white'
            }
        },
    }
)

bar4 = dcc.Graph(id='bar4')

map = html.Iframe(
    id = 'map',
    srcDoc = open('map.html', 'r').read(),
    width = '100%',
    height = '100%'
)

slider = dcc.Slider(
    id='slider-input',
    min=0,
    max=9,
    marks={i: 'Date {}'.format(i) for i in range(10)},
    value=4,
)

textinput = dcc.Input(id='textin-id', value='initial value', type='text')
textout = html.Div(id='textout-div')



mainContainer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        bar1,
                        bar2,
                        #bar3
                        bar4
                    ],
                    width = 4,
                ),

                dbc.Col(
                    [
                        map
                    ],
                    width = 8
                )
            ],
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        textinput,
                        textout
                    ],
                    width = 4
                ),

                dbc.Col(
                    [
                        slider,
                    ],
                    width = 4
                )
            ]
        )   
    ],
    fluid=True
    #style={'backgroundColor':'#212748'} #373C5A
)

app.layout = html.Div(
    [
        mainContainer        
    ],
)

@app.callback(
    Output('bar4', 'figure'),
    [Input('slider-input', 'value')])
def update_figure(selected_year):
    
    traces = [
        {'x': [1], 'y': [selected_year], 'type': 'bar', 'name': 'Slider Out'},
        {'x': [2], 'y': [selected_year], 'type': 'bar', 'name': 'Slider Out'},
    ]

    return {
        'data': traces,
        'layout': {
            'title': 'Dash Data Visualization 4',
            'yaxis': {'title': 'OUT Y', 'range': [0, 10]},
            'plot_bgcolor': '#0F1536',
            'paper_bgcolor': '#0F1536',
            'height':'300',
            'font': {
                'color': 'white'
            }
        },
    }
    

if __name__ == '__main__':
    app.run_server(debug=True)