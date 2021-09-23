<<<<<<< current
import yfinance as yf
import datetime
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Graph"),
    html.Div(children='Ticker: '),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),


])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    Input(component_id='input', component_property='value')
)
def update_graph(input_tick: str):
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.today()
    df = yf.Ticker(input_tick).history(start=start, end=end)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    return dcc.Graph(
        id='Stock Graph',
        figure={
            'data': [{'x': df.index, 'y': df['Close'], 'type': 'line',
            'layout': {
                'title': f'{input_tick}'.upper()
                }
            }
    )


if __name__ == "__main__":
    app.run_server(debug=True)
=======
import yfinance as yf
import datetime
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Graph"),
    html.Div(children='Ticker: '),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),


])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    Input(component_id='input', component_property='value')
)
def update_graph(input_tick: str):
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.today()
    df = yf.Ticker(input_tick).history(start=start, end=end)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    return dcc.Graph(
        id='Stock Graph',
        figure={
            'data': [{'x': df.index, 'y': df['Close'], 'type': 'line',
                      'name': 'stock price graph', 'color': 'red'}],
            'layout': {
                'title': f'{input_tick}'.upper()
                }
            }
    )


if __name__ == "__main__":
    app.run_server(debug=True)
>>>>>>> before discard
