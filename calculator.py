import dash
from dash import dcc
from dash import html
from dash import no_update as nop
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Calculator'


def update_layout():
    body = dbc.Container([
        dbc.Row(html.Div("",style={'height':'100px'})),
        dbc.Row([
            dbc.Row([
                dbc.Row(html.Div(""),style={'height':'10px'}),
                dbc.Col([
                    dbc.Textarea(id='test_box',style={'height':'150px','width':'104%','display':'block'}),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("7",id='btn_7',style={'margin-right':'5px','margin-top':'5px'}),
                            dbc.Button("8",id='btn_8',style={'margin-right':'5px','margin-top':'5px'}), 
                            dbc.Button("9",id='btn_9',style={'margin-right':'5px','margin-top':'5px'}),
                            dbc.Button("+",id='btn_plus',style={'margin-right':'5px','margin-top':'5px'})
                        ],width=6)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("4",id='btn_4',style={'margin-right':'5px','margin-top':'5px'}), 
                            dbc.Button("5",id='btn_5',style={'margin-right':'5px','margin-top':'5px'}), 
                            dbc.Button("6",id='btn_6',style={'margin-right':'5px','margin-top':'5px'}),
                            dbc.Button("-",id='btn_minus',style={'margin-right':'5px','margin-top':'5px'})
                        ],width=6),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("1",id='btn_1',style={'margin-right':'5px','margin-top':'5px'}), 
                            dbc.Button("2",id='btn_2',style={'margin-right':'5px','margin-top':'5px'}), 
                            dbc.Button("3",id='btn_3',style={'margin-right':'5px','margin-top':'5px'}),
                            dbc.Button("/",id='btn_divide',style={'margin-right':'5px','margin-top':'5px'})
                        ],width=6),
                            
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("0",id='btn_0',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'}), 
                            dbc.Button(".",id='btn_dp',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'}), 
                            dbc.Button("=",id='btn_=',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'}),
                            dbc.Button("x",id='btn_multiply',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'})
                        ],width=6),
                    ])
                ])
            ])
        ],style={'background-color':'#f2f2f2','border-radius':'5px','box-shadow':'2px 2px #d2d2d2','width':'60%'})
    ])

    return body

app.layout = update_layout()

@app.callback(
    Output('test_box','value'),
    *[Input(f'btn_{i}','n_clicks') for i in range(10)],
    Input('btn_=', 'n_clicks'),
    Input('btn_dp', 'n_clicks')
)
def test(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n_eq,n_dp):
    trigger = dash.callback_context.triggered[0]['prop_id']
    return trigger.split(".")[0].split("_")[1]



if __name__ == "__main__":
    app.run_server(debug=True)