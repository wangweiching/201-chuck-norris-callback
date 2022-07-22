######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=[
    {
        "label": "forehand",
        "demo": "https://images.squarespace-cdn.com/content/v1/5d9d0c165b67224fffdc025b/1577819405443-PNFCD3IN17E38MTSKTEC/image-asset.gif"
    },
    {
        "label":"backhand",
        "demo": "https://images.squarespace-cdn.com/content/v1/5d9d0c165b67224fffdc025b/1577901915805-G6NLJ636A7MACNUQQFGE/ezgif.com-optimize+%284%29.gif"
    },
    {
        "label": "slice",
        "demo": "https://images.squarespace-cdn.com/content/v1/5d9d0c165b67224fffdc025b/1577904057399-G4JOA4HUAL57OSCL03CG/ezgif.com-optimize+%286%29.gif"
    },
    {
        "label": "volley",
        "demo": "https://images.squarespace-cdn.com/content/v1/5d9d0c165b67224fffdc025b/1577909204949-W44BX73Y6ULGHOY9VAXG/ezgif.com-optimize+%287%29.gif"
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
    html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices],
                value='punch',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
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
