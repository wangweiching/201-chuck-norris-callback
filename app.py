######### Import your libraries #######
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import os

###### Set up variables
list_of_choices=[
    {
        "label": "forehand",
        "demo": "https://media.giphy.com/media/d91znKMfav9mre2TlC/giphy.gif"
    },
    {
        "label":"backhand",
        "demo": "https://media.giphy.com/media/4Nvg2jmFkhZr0Gngjk/giphy.gif"
    },
    {
        "label": "slice",
        "demo": "https://media.giphy.com/media/9Dxgzo7hRUAWHSQO0e/giphy-downsized-large.gif"
    },
    {
        "label": "volley",
        "demo": "https://media.giphy.com/media/vhuQyyEfDbVPedVyYk/giphy.gif"
    }
]
githublink = 'https://github.com/wangweiching/201-chuck-norris-callback'
heading1='Tennis basic strokes'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Learn Tennis'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    # dcc.Dropdown(id='your-input-here',
    #             options=[{'label': i, 'value': i} for i in list_of_choices],
    #             value='punch',
    #             style={'width': '500px'}),
    dcc.Dropdown(id='your-input-here',
            options=[{'label': i["label"], 'value': idx} for idx,i in enumerate(list_of_choices)],
            value=0,
            style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Iframe(src='', style={'width': '300', 'height':'200'}, id='demo'),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), Output('demo', 'src')],
              [Input('your-input-here', 'value')])
def display_value(choice_idx):
    label = list_of_choices[choice_idx]["label"]
    demo = list_of_choices[choice_idx]["demo"]
    return f'I can execute you with a {label}.', demo

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
