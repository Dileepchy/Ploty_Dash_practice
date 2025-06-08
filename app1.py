# Import packages
from dash import Dash,html, dash_table, dcc
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


#Initialize the app
app = Dash()

#App Layout
app.layout = [
        html.Div(children='My First App with Data', style={'textAlign':'center', 'color':'red'}),
        dash_table.DataTable(data=df.to_dict('records'), page_size=10),
        dcc.Graph(figure=px.histogram(df, x='continet', y='lifeExp', histfunc='agv'))
        ]

if __name__ == '__main__':
    app.run(debug=True)