from Functions.config import *
from Functions.State_Map import state_map 

def top_10_trend(df):

    df1=df.copy()

    df1=df1[(df1['level']=='State')]

    df1['state']=df1['state'].str.title()

    state=st.selectbox('Select State',list(df1['state'].unique()))

    # year=st.selectbox('Year(State Wise)',list(df['year'].unique()))
    df1=df1[df1['state']==state]

    st.write(df1.head())
    # df=df[(df['year']==year)*(df['state']==state)]

    #grouping at district level
    df2=df1[['year','transaction_amount','transaction_count']].groupby(['year']).sum().reset_index()

    # df2['year']=df2['district_pincode_name'].str.title()

    
    st.write(df2    .head())

    fig=px.line(df2,x='year',y='transaction_amount',labels={'transaction_amount':'Total Insurance Transaction Amount'
                                                                                       ,'year':'Year'
                                                                                       })
    st.plotly_chart(fig) #showing line graph