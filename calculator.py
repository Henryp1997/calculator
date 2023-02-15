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
                dbc.Row([
                    dbc.Row(html.Div(""),style={'height':'10px'}),
                    dbc.Col([
                        dbc.Textarea(id='test_box',style={'height':'150px','width':'104%','display':'block'}),
                    ])
                ]),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("(",id='btn_brack_left',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button(")",id='btn_brack_right',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("%",id='btn_%',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("AC",id='btn_AC',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("sin",id='btn_sin',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("cos",id='btn_cos',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("tan",id='btn_tan',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1')
                        ],width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("7",id='btn_7',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("8",id='btn_8',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("9",id='btn_9',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("+",id='btn_plus',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("ln",id='btn_ln',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("log\u2081\u2080",id='btn_log',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("log\u2093",id='btn_e',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                        ],width=12)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("4",id='btn_4',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("5",id='btn_5',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("6",id='btn_6',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("-",id='btn_minus',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("x\u00B2",id='btn_sup2',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("x\u02B8",id='btn_sup',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("\u221A",id='btn_sqrt',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                        ],width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("1",id='btn_1',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("2",id='btn_2',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'), 
                            dbc.Button("3",id='btn_3',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("/",id='btn_divide',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("x!",id='btn_factorial',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("\u03C0",id='btn_pi',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                            dbc.Button("",id='btn_sqrt2',style={'margin-right':'5px','margin-top':'5px'},className='gap-2 col-1'),
                        ],width=12),
                            
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("0",id='btn_0',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'), 
                            dbc.Button(".",id='btn_dp',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'), 
                            dbc.Button("=",id='btn_=',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'),
                            dbc.Button("*",id='btn_multiply',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'),
                            dbc.Button("",id='btn_factorial1',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'),
                            dbc.Button("Inv",id='btn_pi1',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'),
                            dbc.Button("Ans",id='btn_ans',style={'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'},className='gap-2 col-1'),
                        ],width=12),
                    ])
                ],width=12)
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