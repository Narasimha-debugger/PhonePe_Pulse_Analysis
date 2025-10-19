from Functions.config import *
from Functions.State_Map import state_map 

def state_level_transaction(state_trans_data):

    df=state_trans_data.copy()

    df=state_map(df,'state')

    state=st.selectbox('Select State',list(df['state'].unique()))

    # year=st.selectbox('Year(State Wise)',list(df['year'].unique()))
    df=df[df['state']==state]
    # df=df[(df['year']==year)*(df['state']==state)]

    #grouping at quarter type
    df2=df[['year','transaction_amount','transaction_type']].groupby(['year','transaction_type']).sum().reset_index()

    fig=px.bar(df2,x='year',y='transaction_amount',color='transaction_type',labels={'transaction_amount':'Total Transaction Amount','year':'Year'
                                                                                    ,'transaction_type':'Transaction Type'})
    st.plotly_chart(fig) #showing bar graph