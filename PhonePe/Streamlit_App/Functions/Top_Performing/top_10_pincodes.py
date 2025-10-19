from Functions.config import *
from Functions.State_Map import state_map 

def top_10_pincodes(df,year):

    df1=df.copy()

    df1=df1[(df1['level']=='Pincode')*(df1['year']==year)]

    # st.write(df1.head())

    #grouping at district level
    df2=df1[['district_pincode_name','transaction_amount','transaction_count']].groupby(['district_pincode_name']).sum().reset_index()

    df2['district_pincode_name']=df2['district_pincode_name'].str.title()

    #sorting values based on insurance amount
    df2=df2.sort_values(by='transaction_amount',ascending=False).head(10)

    fig=px.bar(df2,x='district_pincode_name',y=['transaction_amount','transaction_count'],barmode='group',
               labels={'value':'Amount/Count','district_pincode_name':'Pincode','transaction_amount':'Transaction Amount','transaction_count':'Transaction Count'},
               title=f'Top 10 States the year {year} based on Transactions')

    st.plotly_chart(fig) #showing bar graph