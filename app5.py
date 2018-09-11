import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import collections
from plotly.tools import FigureFactory as FF

app = dash.Dash()

df = pd.read_csv('/opt/app/omni-machine-learning/Model_DRF/train/data/case_withApplication_forTraining.csv',low_memory=False)

state = collections.Counter(df.loc[:,'avertackCase.caseApplicationRecordList.applicationRecord.fields.state'])
sales = collections.Counter(df.loc[:,'avertackCase.caseApplicationRecordList.applicationRecord.fields.salesChannel'])
case = collections.Counter(df.loc[:,'avertackCase.caseDisposition'])
customerType = collections.Counter(df.loc[:,'avertackCase.caseApplicationRecordList.applicationRecord.fields.customerType'])
banStatus = collections.Counter(df.loc[:,'avertackCase.caseApplicationRecordList.banStatus'])
rulesStr = collections.Counter(df.loc[:,'avertackCase.rulesStr'])


app.layout = html.Div([
    dcc.Graph(
        id='avertack-sys',
        figure={
            'data': [
                # go.Bar(x=['giraffes', 'orangutans', 'monkeys'],y=[20, 14, 23])
                go.Bar(x = case.keys() ,y = case.values()) #,go.Bar(x= case.keys() ,y=case.values())]
                #ff.create_distplot(hist_data, group_labels)
            ],
            'layout': go.Layout(
                xaxis={'title': 'Case Disposition'},
                yaxis={'title': 'Counts'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


