import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'dfbackground': '#808FDF'
}

app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="four columns",
                    children=[
                        html.Div(
                            className='two columns div-header-columns',
                            children=[
                                html.H2(
                                    children='H2'
                                ),
                                html.H2(
                                    children='H2'
                                )
                            ]
                        )

                    ]
                ),

                html.Div(
                    className="eight columns div-map",
                    children=[
                        html.Iframe(
                            id='map',
                            srcDoc = open('map.html', 'r').read(),
                            width='100%',
                            height='850'
                        )
                    ]
                )
            ]
        ),

        html.Div(
            className="row",
            children=[
                html.Div(
                    className="four columns viz-1",
                    children=[
                        dcc.Graph(
                            id='viz-1',
                            figure={
                                'data':[
                                    {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}
                                ],
                                'layout': {
                                    'title': 'Dash Data Visualization',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {
                                        'color': colors['text']
                                    }
                                }
                            }
                        )
                    ]
                ),

                html.Div(
                    className="four columns viz-2",
                    children=[
                        dcc.Graph(
                            id='viz-2',
                            figure={
                                'data':[
                                    {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}
                                ],
                                'layout': {
                                    'title': 'Dash Data Visualization',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {
                                        'color': colors['text']
                                    }
                                }
                            }
                        )
                    ]
                ),

                html.Div(
                    className="four columns viz-3",
                    children=[
                        dcc.Graph(
                            id='viz-3',
                            figure={
                                'data':[
                                    {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}
                                ],
                                'layout': {
                                    'title': 'Dash Data Visualization',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {
                                        'color': colors['text']
                                    }
                                }
                            }
                        )
                    ]
                ),
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)