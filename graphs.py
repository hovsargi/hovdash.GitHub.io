#Graph 1
from plotly.offline import iplot,plot
import pandas as pd
import numpy as np
import plotly.graph_objs as go
trace1=go.Bar(x=[15,50,15,20],y=["x8","x7","x6","x5"],orientation = 'h',marker=dict(color="lightcoral"),name="Positive")
trace2=go.Bar(x=[-15,-45,-5,-35],y=["x4","x3","x2","x1"],orientation = 'h',marker=dict(color="maroon"),name="Negative")
layout  = dict(title="Correlation with employees probability of churn",yaxis=dict(title="Variable"),showlegend=True)
figure1 =dict(data=[trace1,trace2],layout=layout)

#Graph 2
import quandl
quandl.ApiConfig.api_key = "TGvmj32UM_sW2Utn1utg"
data = quandl.get("FRED/GDP")

from plotly.offline import plot, iplot
import plotly.graph_objs as go

import pandas as pd

x_values = pd.to_datetime(data.index.values)
y_values = data["Value"]
trace = go.Scatter(x=x_values,y=y_values,mode="lines",fill='tozeroy')
       
layout = go.Layout(title='<b>US GDP over time</b>')
data = [trace]
figure2 = dict(data=data,layout=layout)


#Graph3
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np

import quandl
quandl.ApiConfig.api_key = "TGvmj32UM_sW2Utn1utg"
googl= quandl.get("WIKI/GOOGL")
btc=quandl.get("BCHARTS/ABUCOINSUSD")

header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )

df1=googl.Open.pct_change()
df2=btc.Open.pct_change()
df3=df1.ix[:5]
rounded1=np.round(df3, decimals=3)
df4=df2.ix[:5]
rounded2=np.round(df4, decimals=3)
cells = dict(values=[rounded1,
                     rounded2],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
trace5 = go.Table(header=header, cells=cells)
data = [trace5]
layout = dict(width=500, height=310)
figure3 = dict(data=data, layout=layout)


#Graph4
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np

import quandl
quandl.ApiConfig.api_key = "TGvmj32UM_sW2Utn1utg"
googl= quandl.get("WIKI/GOOGL")
btc=quandl.get("BCHARTS/ABUCOINSUSD")

Google = go.Box(x=btc.Open.pct_change(), name="Google")
Bitcoin= go.Box(x=googl.Open.pct_change(), name="Bitcoin")
data = [Google, Bitcoin]
figure4 = dict(data=data)


#Graph5
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31',Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-15', Resource='Team Formation'),
      dict(Task="Task 3", Start='2018-04-15', Finish='2018-09-30', Resource='Prototyping')]

colors = ['#7a0509', (0.1, 0.8, 0.1), 'rgb(254,224,144)']

figure5 = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True,title="Startup Roadmap")

