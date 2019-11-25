import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('C:/Users/erikj/Desktop\Workspace/Dash/Resources/data.csv')

def generate_table(dataframe, max_rows=5):
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

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'dfbackground': '#808FDF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style = {
            'textAlign': 'center',
            'color': colors['text']
        }
    ),


    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [8, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                {'x': [1, 2, 3], 'y': [7, 9, 5], 'type': 'bar', 'name': 'AZ'}
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
    ),

    html.H2(
        children = 'UFC DataFrame',
        style = {
            'textAlign': 'center',
            'color': colors['text']
        } 
    ),

    html.Div(
        children = [
            html.H4(
                children = 'UFC Fighters Statistics (1993-2019)',
                style = {
                    'textAlign': 'left',
                    'color': 'black'
                }
            ),

            html.P(
                children ='''This is a list of UFC fighter statistics for the total history of the organization. the following data represents results from fighters
                    bouts including information such as: Fighter Name, Referee, date of event, location, weight class, etc.''',
                style = {
                    'textAlign': 'left',
                    'color': 'black'
                }
            ),   

            generate_table(df)
        ],
        style = {
            'backgroundColor': 'white'
        }
    ),





])

if __name__ == '__main__':
    app.run_server(debug=True)