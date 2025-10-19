from Functions.config import *
# from Functions.Data_Loader import sql_query_runner  
from init import *
# import warnings
# # warnings('ignore')
# warnings.filterwarnings('ignore')
import streamlit as st

env_path = r"C:\Users\nagan\OneDrive\Desktop\Guvi\Project\PhonePe\.env"
load_dotenv(env_path)

st.sidebar.title('Navigation')

rad_slctn=st.sidebar.radio('Go to Page',['Project Introduction','Business Questions'])

if rad_slctn=='Project Introduction':
    # st.image()
    col1,col2=st.columns([1,3])
    col1.image(r"C:\Users\nagan\OneDrive\Desktop\Guvi\Project\PhonePe\PhonePe-Logo.png",width=140,use_container_width=True)
    col2.title(' PhonePe Pulse Analysis')
    st.subheader(' Home Page')

    st.write("""
    This project analyzes different datasets of Phonepe across diffent states in India

    **Features:**
             
    1) View different analysis done for different business questions  
            """)


elif rad_slctn=='Business Questions':

    drop_down=st.selectbox('Select the Question',['1. Decoding Transaction Dynamics on PhonePe'])

    if drop_down=='1. Decoding Transaction Dynamics on PhonePe':

        ### Figure 1 India map for total transaction amount state wise for a selected year and quarter
        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        PhonePe Total Transactions Amount Dynamics</h1>""",unsafe_allow_html=True)
        st.markdown('---')
        query="""select *
                     from aggregated_trans
                     
                     order by 1,2,3"""
        ### running sql query runner function to get the dataframe for above sql query
        state_trans_data=sql_query_runner(query)
        state_trans_data.columns=state_trans_data.columns.str.lower()  ## converting columns to lower case
        ## cos for year and quarter filters 
        col1,col2=st.columns(2)
        with col1:
            year=st.selectbox('Year',list(state_trans_data['year'].unique()))
            # st.write(year)
        with col2:
            quarter=st.selectbox('Quarter',list(state_trans_data['quarter'].unique()))

        quarterly_india_map(year,quarter,state_trans_data)

        # # filteting the datafrane for the given year and quarter
        # df=state_trans_data[(state_trans_data['year']==year)&(state_trans_data['quarter']==quarter)]
        # df=df.groupby('state').sum().reset_index()
        # df=df[['state','transaction_amount']]

        # # reading the GeoJson File
        # new_df=df.copy()
        # new_df=state_map(new_df,'state')
        # india_map_path=os.getenv("india_geo")

        # ### using geopandas json to take unique values
        # gdf = gpd.read_file(india_map_path)

        # # Merge all districts into single state geometries
        # state_gdf = gdf.dissolve(by="st_nm")

        # # Save to a new file
        # state_gdf.to_file(india_map_path, driver="GeoJSON")

        # with open(india_map_path, "r") as f:
        #     india_geo = json.load(f)

        # color_scales = ['Blues']
        #     # 'Reds', 'Blues', 'Greens', 'Viridis', 'Cividis', 'Plasma', 'Inferno', 'Magma', 'Oranges', 'PuRd', 'YlGnBu', 'RdYlBu']

        # for scale in color_scales:
        #     fig = px.choropleth(
        #         new_df,geojson=india_geo,locations='state',featureidkey="properties.st_nm",
        #         color='transaction_amount',color_continuous_scale=scale,title=f'PhonePe Transaction by State')
        #     fig.update_layout(title_font=dict(family="Arial", size=24, color="blue"))
        #     fig.update_geos(fitbounds="locations", visible=False)
        #     # fig.update_traces(marker_line_color='black', marker_line_width=1.5)
        #     st.plotly_chart(fig,use_container_width=False)

            ### Figure 2 Top 10 States in terms of total transaction amount
        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        Top 10 States by Transaction Amount</h1>""",unsafe_allow_html=True)

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

        # st.write(df)

        ### Figure 3 trasactions by popular methods 
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
        Payment Method Popularity</h1>""",unsafe_allow_html=True)
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

        ### Fig 4 Trend Analysis
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
            Trend Analysis Transaction Amount & Count</h1>""",unsafe_allow_html=True)

        year=st.selectbox('Select Year',list(state_trans_data['year'].unique()))

        #makign copy and filteting for the selected year
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

        ## Fig 5 transactions by state and payment category
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
        Transaction by State and Payment Category</h1>""",unsafe_allow_html=True)

        

        #makign copy and filteting for the selected year
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