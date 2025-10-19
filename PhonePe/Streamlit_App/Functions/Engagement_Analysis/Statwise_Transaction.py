from Functions.config import *
from Functions.State_Map import state_map 

def brand_statewise(year,df):
    df=df[df['year']==year]

# df=df[(df['year']==year)&(df['state']==state)]

    df=df.groupby(['state','user_brand']).sum().reset_index() 

    top_states = df.groupby('state')['user_app_opens'].sum().nlargest(10).index
    df = df[df['state'].isin(top_states)]

    df=df.sort_values(by=['user_app_opens'],ascending=False)
    # st.write(df)
    df=state_map(df,'state')

    total_opens = df['user_app_opens'].sum()
    df['percent_of_total'] = (df['user_app_opens'] / total_opens * 100).round(2)

    # fig = go.Figure()

    ## First Metric User Registrations

    fig=px.bar(df,x='state',y='user_app_opens',color='user_brand',labels={'user_app_opens':'User App Opens','user_app_opens':'User App Opens'
                                                                        ,"user_brand":'User Brand','state':'State'}
                        ,category_orders={'state': df['state'].tolist()}
                        ,hover_data={
                                        'user_app_opens': True,
                                        'percent_of_total': ':.2f',
                                        'user_brand': True,
                                        'state': True} )
    fig.update_traces(
        customdata=df[['user_brand', 'percent_of_total']],
            hovertemplate='<b>%{x}</b><br>Brand: %{customdata[0]}<br>'
                        'User App Opens: %{y}<br>'
                        'Percent of Total: %{customdata[1]}%'
        )

    st.plotly_chart(fig)