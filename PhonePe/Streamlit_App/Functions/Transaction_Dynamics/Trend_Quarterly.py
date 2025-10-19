from Functions.config import *

def quarterly_trend(year,quarter,state_trans_data):
        
        year=st.selectbox('Select Year',list(state_trans_data['year'].unique()))

        df=state_trans_data.copy()

        df=df[(df['year']==year)]

        #grouping at quarter type
        df2=df[['quarter','transaction_amount','transaction_count']].groupby(['quarter']).sum().reset_index()

        ##Line Chart with Mulitpel Y axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # addign first Y axis
        fig.add_trace(go.Scatter(x=df2['quarter'],y=df2['transaction_amount'],name='Transaction Amount'),secondary_y=False)
        # adding second y axis\
        fig.add_trace(go.Scatter(x=df2['quarter'],y=df2['transaction_count'],name='Transaction Count'),secondary_y=True)
        fig.update_layout(title_text='Transaction Trend') # adding title
        fig.update_xaxes(title_text='Quarter') # adding x axis
        fig.update_yaxes(title_text="Transaction Amount", secondary_y=False)
        fig.update_yaxes(title_text=" transaction Count", secondary_y=True)        
        st.plotly_chart(fig)