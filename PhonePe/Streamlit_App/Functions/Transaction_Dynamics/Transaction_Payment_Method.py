from Functions.config import *
# from Functions.State_Map import state_map 

def trasaction_by_payment_method(year,quarter,state_trans_data):
    #makign copy of the dataframe
        df=state_trans_data.copy()

        year=st.selectbox('Year (Payment Method)',list(state_trans_data['year'].unique()))

        col1,col2=st.columns([2,2])
        ## filtering for the year
        df=df[(df['year']==year)]

        #grouping at transaction type
        df2=df[['transaction_type','transaction_amount','transaction_count']].groupby(['transaction_type']).sum().reset_index()

        #### Pie Chart for transaction Amount
        fig=px.pie(df2,values='transaction_amount',names='transaction_type',title='Transaction Amout Distribution')
        fig.update_layout(title_font=dict(family="Arial", size=20, color="orange"))
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_traces(textposition='inside', hovertemplate='%{label}: %{percent} <br>Amount: %{value}<extra></extra>')
        col1.plotly_chart(fig,use_container_width=False)

        #### Pie Chart for transaction count
        fig=px.pie(df2,values='transaction_count',names='transaction_type',title='Transaction Count Distribution')
        fig.update_layout(title_font=dict(family="Arial", size=20, color="orange"))
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_traces(textposition='inside', hovertemplate=' %{percent} <br>Amount: %{value}<extra></extra>')
        col2.plotly_chart(fig,use_container_width=True)