import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = df.head(20)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        #Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        #Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['weight_class'] == i]['B_current_win_streak'],
                    y=df[df['weight_class'] == i]['B_avg_BODY_landed'],
                    text=df[df['weight_class'] == i]['R_fighter'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.weight_class.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'B_current_win_streak'},
                yaxis={'title': 'B_avg_BODY_landed'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True) 