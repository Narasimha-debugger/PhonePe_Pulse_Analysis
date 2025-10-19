from Functions.config import *
from Functions.State_Map import state_map 

def brand_user_engagement(sql_df):
        
        df=sql_df.copy()

        df=df[df['brand_row_number']==1]

        year=st.selectbox('Year',list(df['year'].unique()))

        # state=st.selectbox('State',list(df['state'].unique()))

        df=df[df['year']==year]
        # df=df[(df['year']==year)&(df['state']==state)]

        if df is not None and not df.empty :
            # st.write(df)
            df['user_brand'].fillna('No Brand',inplace=True)
            df=df.groupby(['user_brand'])[['dist_user_registrd_count','user_app_opens']].sum().reset_index()

            df=df.sort_values(by='user_app_opens',ascending=False)

            fig = go.Figure()

            ## First Metric User Registrations

            fig.add_trace(go.Bar(x=df['user_brand'],y=df['user_app_opens'],name='User App Opens',marker_color='skyblue'))
            # second metric user opens
            
            fig.add_trace(go.Bar(x=df['user_brand'],y=df['dist_user_registrd_count'],name='User Registrations',marker_color='#FF8C00'))
            st.plotly_chart(fig)

        else:
            st.write("Unfortunately Data is not Available 😢")