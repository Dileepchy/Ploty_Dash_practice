# Import packages
from dash import Dash,html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)


#App Layout
app.layout = [
        html.Div(className='row', children='My first app  with data, Graph and controls',
                 style={'textAlign': 'center', 'color':'blue', 'fontSize':30}),
        
        html.Div(className='row', children=[
                dcc.RadioItems(options=['pop','lifeExp', 'gdpPercap'],
                               value='lifeExp',
                               inline=True,
                               id='my-radio-buttons-final')
        ]),
        
        html.Div(className='row', children=[
                html.Div(className='six columns', children=[
                        dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
                ]),
                html.Div(className='six colums', children=[
                        dcc.Graph(figure={}, id='hist-chart-final')
                ])
        ])
]

# Add controls to build the interaction
@callback(
    Output(component_id='hist-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig


if __name__ == '__main__':
    app.run(debug=True)