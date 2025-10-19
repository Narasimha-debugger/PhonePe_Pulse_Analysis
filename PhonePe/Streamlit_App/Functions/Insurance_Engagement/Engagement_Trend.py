from Functions.config import *
from Functions.State_Map import state_map 

def insurance_trend_districts(year,state,df):

    df.columns=df.columns.str.lower()
    df=df[(df['state']==state)]
    

    #grouping at state level
    df2=df[['district_name','year','insurance_amount','insurance_count']].groupby(['district_name','year']).sum().reset_index()

    #sorting df
    df2=df2.sort_values(by=['insurance_amount'],ascending=False)


    # fig = px.histogram(df, x="district_name", y="totainsurance_amountl_bill",color='quarter', barmode='group',height=400)
    

    fig=px.histogram(df2,x='district_name',y='insurance_amount',labels={'insurance_amount':'Total Insurance Amount','district_name':'District Name'
                                                            ,"year":"Year"}
                                                            ,color='year'
               ,barmode='group',height=500,title=f'Insurance Amount Across Districts and Years for {state}'
            #    ,category_orders={'Quarter': [1, 2, 3, 4]}
            #    ,hover_data={'insurance_amount': ':.2f', 'percentage': False})
            )
    st.plotly_chart(fig,use_container_width=False)
