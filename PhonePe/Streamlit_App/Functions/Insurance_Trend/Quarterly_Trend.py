from Functions.config import *
from Functions.State_Map import state_map 

def insurance_trend_quarterly(year,df):

    df1=df.copy()

    df1.columns=df1.columns.str.lower()

    df1=df[(df1['year']==year)]

    # df1=state_map(df1,'state')

    # state=st.selectbox('Select State',list(df1['state'].unique()))

    # year=st.selectbox('Year(State Wise)',list(df['year'].unique()))
    # df1=df1[df1['state']==state]
    # df=df[(df['year']==year)*(df['state']==state)]

    #grouping at year and quarter
    df2=df1[['state','quarter','insurance_amount','insurance_count']].groupby(['state','quarter']).sum().reset_index()

    df2=df2.sort_values(by=['insurance_amount'],ascending=False)

    # adding percentage column
    # df2['percentage'] = df2.groupby('state')['insurance_amount'].apply(lambda x: (x / x.sum()) * 100)
    df2['percentage'] = (df2['insurance_amount'] / df2.groupby('state')['insurance_amount'].transform('sum') * 100)



    fig=px.bar(df2,x='state',y='insurance_amount',labels={'insurance_amount':'Total Insurance Amount','quarter':'Quarter'}
               ,color='quarter',barmode='group',height=500,title=f'Quarterly Insurance Amount Trend for {year}'
               ,category_orders={'Quarter': [1, 2, 3, 4]}
            #    ,hover_data={'insurance_amount': ':.2f', 'percentage': False})
            )
        #        ,hover_data={
        # 'quarter': True,
        # 'insurance_amount': ':.2f',
        # 'percentage': ':.2f'+'%',   # show percentage with 2 decimals
        # 'state': False} )
    fig.update_traces(hovertemplate=(
        'State: %{x}<br>'
        'Quarter: %{customdata[0]}<br>'
        'Insurance Amount: %{y:.2f}<br>'
        'Percentage: %{customdata[1]:.2f}%<extra></extra>'),customdata=df2[['quarter', 'percentage']])
    st.plotly_chart(fig) #showing line graph