from Functions.config import *
from Functions.State_Map import state_map 

def insurance_trend(df,state):

    df1=df.copy()

    df1=df[(df1['state']==state)]

    # df1=state_map(df1,'state')

    # state=st.selectbox('Select State',list(df1['state'].unique()))

    # year=st.selectbox('Year(State Wise)',list(df['year'].unique()))
    # df1=df1[df1['state']==state]
    # df=df[(df['year']==year)*(df['state']==state)]

    #grouping at year 
    df2=df1[['year','insurance_amount','insurance_count']].groupby(['year']).sum().reset_index()

    # fig=px.line(df2,x='quarter',y='insurance_transaction_amount',labels={'insurance_transaction_amount':'Total Insurance Transaction Amount','quarter':'Quarter'})
    # st.plotly_chart(fig) #showing line graph
    ##Line Chart with Mulitpel Y axis
    ##Line Chart with Mulitpel Y axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # addign first Y axis
    fig.add_trace(go.Scatter(x=df2['year'],y=df2['insurance_amount'],name='Insurance Transaction Amount'),secondary_y=False)
    # adding second y axis\
    fig.add_trace(go.Scatter(x=df2['year'],y=df2['insurance_count'],name='Insurance Transaction Count'),secondary_y=True)
    fig.update_layout(title_text='Transaction Trend') # adding title
    fig.update_xaxes(title_text='Year') # adding x axis
    fig.update_yaxes(title_text="Transaction Amount", secondary_y=False)
    fig.update_yaxes(title_text=" Transaction Count", secondary_y=True)        
    st.plotly_chart(fig)