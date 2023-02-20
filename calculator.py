import dash
from dash import dcc
from dash import html
from dash import no_update as nop
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import math
import numpy as np

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Calculator'

majority_style = {'margin-right':'5px','margin-top':'5px'}
bottom_row_style = {'margin-right':'5px','margin-top':'5px','margin-bottom':'5px'}

sqrt_symb = '\u221A'

def update_layout():
    body = dbc.Container([
        html.Div(id="memory_div",style={'display':'none'}),
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
                            dbc.Button("(",id='btn_brackleft',style=majority_style,className='gap-2 col-1'),
                            dbc.Button(")",id='btn_brackright',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("\U0001F82C",id='btn_backspace',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("AC",id='btn_AC',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("sin",id='btn_sin',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("cos",id='btn_cos',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("tan",id='btn_tan',style=majority_style,className='gap-2 col-1')
                        ],width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("7",id='btn_7',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("8",id='btn_8',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("9",id='btn_9',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("+",id='btn_plus',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("ln",id='btn_ln',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("log\u2081\u2080",id='btn_log10',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("log\u2093",id='btn_log',style=majority_style,className='gap-2 col-1'),
                        ],width=12)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("4",id='btn_4',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("5",id='btn_5',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("6",id='btn_6',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("-",id='btn_minus',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("x\u00B2",id='btn_sup2',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("x\u02B8",id='btn_sup',style=majority_style,className='gap-2 col-1'),
                            dbc.Button(sqrt_symb,id='btn_sqrt',style=majority_style,className='gap-2 col-1'),
                        ],width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("1",id='btn_1',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("2",id='btn_2',style=majority_style,className='gap-2 col-1'), 
                            dbc.Button("3",id='btn_3',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("/",id='btn_divide',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("x!",id='btn_factorial',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("\u03C0",id='btn_pi',style=majority_style,className='gap-2 col-1'),
                            dbc.Button("e",id='btn_e',style=majority_style,className='gap-2 col-1'),
                        ],width=12),
                            
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button("0",id='btn_0',style=bottom_row_style,className='gap-2 col-1'), 
                            dbc.Button(".",id='btn_dp',style=bottom_row_style,className='gap-2 col-1'), 
                            dbc.Button("=",id='btn_=',style=bottom_row_style,className='gap-2 col-1'),
                            dbc.Button("*",id='btn_multiply',style=bottom_row_style,className='gap-2 col-1'),
                            dbc.Button("%",id='btn_%',style=bottom_row_style,className='gap-2 col-1'),
                            dbc.Button("Inv",id='btn_inv',style=bottom_row_style,className='gap-2 col-1'),
                            dbc.Button("Ans",id='btn_ans',style=bottom_row_style,className='gap-2 col-1'),
                        ],width=12),
                    ])
                ],width=12)
            ])
        ],style={'background-color':'#f2f2f2','border-radius':'5px','box-shadow':'2px 2px #d2d2d2','width':'60%'})
    ])
    return body

app.layout = update_layout()

btn_names = [0,1,2,3,4,5,6,7,8,9,'=','backspace','dp','%','multiply','factorial','divide','pi','e','ans','inv','sqrt','sup','sup2','minus','plus','ln','log10','log','brackleft','brackright','AC','sin','cos','tan']
symbol_dict = {
    'dp': '.', 'multiply': '*', 'factorial': '!', 'divide': '/',
    'pi': '\u03c0', 'sqrt': f'{sqrt_symb}(', 'sup': '^', 'sup2': '^2', 'minus': '-',
    'plus': '+', 'ln': 'ln(', 'log10': 'log\u2081\u2080(', 'log': 'log[](',
    'brackleft': '(', 'brackright': ')', 'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan('
}
@app.callback(
    [
        Output('test_box','value'),
        Output('memory_div','children')
    ],
    Input('test_box','value'),
    *[Input(f'btn_{i}','n_clicks') for i in btn_names],
)
def test(value, *btns):
    trigger = dash.callback_context.triggered[0]['prop_id']
    if trigger != '.':
        if 'test_box' in trigger:
            return value, value
        if '=' in trigger:
            print(calculate_result(value))
            value += '='
            return value, value
        if 'backspace' in trigger:
            value = value[:-1]
            return value, value
        if value is None:
            value = ""
        if 'AC' in trigger:
            value = ""
        else:
            btn = trigger.split("_")[1].split(".")[0]
            if btn in list(symbol_dict.keys()):
                to_add = symbol_dict[btn]
            else:
                to_add = btn
            value += to_add
        return value, value
    return nop, nop

def calculate_result(text):
    
    replace_strs = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'tan': 'np.tan',
        'ln': 'np.log',
        'log\u2081\u2080': 'np.log10',
        # figure out log[b]
        '\u03c0': 'np.pi',
        sqrt_symb: 'math.sqrt',
        'e': 'np.e'
    }

    text = "".join(text.split(" "))
    if '=' in text:
        text = text.split("=")[0]
    
    for string in list(replace_strs.keys()):
        if string in text:
            text = text.replace(string, replace_strs[string])

    print(text)

    return exec(f'print({text})')


if __name__ == "__main__":
    app.run_server(debug=True)
