from Functions.config import *
from Functions.State_Map import state_map 

def top_10_states(year,quarter,state_trans_data):
    df=state_trans_data[(state_trans_data['year']==year)]
    df=df.groupby('state').sum().reset_index()

    df=state_map(df,'state') ## Mapping Clean Names for states

    df=df[['state','transaction_amount']]
    df=df.sort_values(by='transaction_amount',ascending=False).head(10)

    fig=px.bar(df,x='state',y='transaction_amount',color='transaction_amount',color_continuous_scale='Blues',
            title=f'Top 10 States')
    fig.update_layout(title_font=dict(family="Arial", size=24, color="orange"))
    fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_traces(marker_line_color='black', marker_line_width=1.5)
    st.plotly_chart(fig,use_container_width=True)