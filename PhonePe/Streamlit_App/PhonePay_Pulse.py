from Functions.config import *
# from Functions.Data_Loader import sql_query_runner  
from init import *
# import warnings
# # warnings('ignore')
# warnings.filterwarnings('ignore')
# import streamlit as st

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
    
    query="""select *
                     from aggregated_trans
                     
                     order by 1,2,3"""
        ### running sql query runner function to get the dataframe for above sql query
    sql_df=sql_query_runner(query)
    sql_df.columns=sql_df.columns.str.lower() 
    
    col1,col2=st.columns([2,2])
    with col1:
            year = st.selectbox("Year", [2021, 2022, 2023, 2024])
            # st.write(year)
    with col2:
            quarter = st.selectbox("Quarter", [1, 2, 3, 4])
    
    df=sql_df.copy()
    df=df[(df['year']==year)&(df['quarter']==quarter)]

     ## Calling Quartellt India Map Functino Defined in transaction Dynamics folder
    quarterly_india_map_introduction_page(year,quarter,df)






elif rad_slctn=='Business Questions':

    drop_down=st.selectbox('Select the Question',['1. Decoding Transaction Dynamics on PhonePe'
                                                ,"2. Device Dominance and User Engagement Analysis"
                                                ,"3.Insurance Penetration and Growth Potential Analysis"
                                                ,"4.Insurance Engagement Analysis"
                                                ,"5.Transaction Analysis Across States and Districts"])

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

        ## Calling Quartellt India Map Functino Defined in transaction Dynamics folder
        quarterly_india_map(year,quarter,state_trans_data)

        ######################## Figure 2 Top 10 States in terms of total transaction amount ############################

        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        Top 10 States by Transaction Amount</h1>""",unsafe_allow_html=True)

        ## top 10 states figure function 
        top_10_states(year,quarter,state_trans_data)

        ################## Figure 3 trasactions by popular methods #################################### 
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
        Payment Method Popularity</h1>""",unsafe_allow_html=True)
         #calling pie char function defined in functions for first question
        trasaction_by_payment_method(year,quarter,state_trans_data) 

        ############################ Fig 4 Trend Analysis ###########################################
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
            Trend Analysis Transaction Amount & Count</h1>""",unsafe_allow_html=True)
        # calling quarterly function 
        quarterly_trend(year,quarter,state_trans_data)

        ############################ Fig 5 transactions by state and payment category ###############
        st.markdown("""<h1 style='color: red; font-size: 30px; font-family: Arial; text-align: left;'>
        Transaction by State and Payment Category</h1>""",unsafe_allow_html=True)
        #Calling State Level Function
        state_level_transaction(state_trans_data)

    elif drop_down=="2. Device Dominance and User Engagement Analysis":

        query="""select A.*
		,b.User_District_Name
		,b.User_App_Opens
        ,b.User_Registrd_Count as dist_User_Registrd_Count
        ,row_number() over(partition by state,year,quarter,user_brand order by user_brand) as brand_row_number
        ,row_number() over(partition by state,year,quarter,User_District_Name order by User_District_Name desc) as app_open_row_number

        from aggregated_user a 
        left join map_user b
        on a.state=b.state
        and a.year=b.year
        and a.quarter=b.quarter
        order by 1,2,3,4,11;"""
        ### running sql query runner function to get the dataframe for above sql query
        sql_df=sql_query_runner(query)
        sql_df.columns=sql_df.columns.str.lower()

        #################################### Figure 1 ################################################

        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        User Engagement Across Brands</h1>""",unsafe_allow_html=True)

        # brand lvl user engagement and registrations function 
        brand_user_engagement(sql_df)

        #################################### Figure 2 ################################################

        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        User Engagement Across States</h1>""",unsafe_allow_html=True)

        df=sql_df.copy()

        df=df[df['app_open_row_number']==1]

        year=st.selectbox('Year (State)',list(df['year'].unique()))
        # state=st.selectbox('State',list(df['state'].unique()))

        df=df[df['year']==year]
        ## Calling Statewise Function
        brand_statewise(year,df) 

        ############ Page 3 Business Question ####################
    elif drop_down=="3.Insurance Penetration and Growth Potential Analysis":

        #### SQL Query for Enitre Page ###############
        query="""SELECT * FROM phonepe_pulse.aggregated_insurance;"""

        ### running sql query runner function to get the dataframe for above sql query
        sql_df=sql_query_runner(query)
        sql_df.columns=sql_df.columns.str.lower()

        df=sql_df.copy() # making copy of original dataframe

        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        Insurance Penetration and Growth Potential Analysis</h1>""",unsafe_allow_html=True)

        ################################# Figure 1 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Insurance Transactions across states over Quarters</h2>""",unsafe_allow_html=True)

        year=st.selectbox('Year',list(df['year'].unique()))
        
        quarter=st.selectbox('Quarter',list(df['quarter'].unique()))

        # Calling Insurance Trend India Map Function
        insurance_trend_india_map(year,quarter,df)

        ################################# Figure 2 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Trend Over the Years for each State </h2>""",unsafe_allow_html=True)

        df1=df.copy()
        df1=state_map(df1,'state')

        state=st.selectbox('State',list(df1['state'].unique()))

        # Calling Insurance Trend Over the years Function\
        insurance_trend(df1,state)

        ################################# Figure 3 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Quarterly Transaction Amount for Each State </h2>""",unsafe_allow_html=True)

        year=st.selectbox('Year (Quarterly)',list(df1['year'].unique()))

        #calling Quarterly Trend Function
        insurance_trend_quarterly(year,df1)
    elif drop_down=="4.Insurance Engagement Analysis":
        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        Insurance Egnagement Analysis Across States and Districts</h1>""",unsafe_allow_html=True)

        #### SQL Query for Enitre Page ###############
        query="""SELECT * FROM phonepe_pulse.map_insurance;"""

        ### running sql query runner function to get the dataframe for above sql query
        sql_df=sql_query_runner(query)
        sql_df.columns=sql_df.columns.str.lower()


        df1=sql_df.copy()
        df1=state_map(df1,'state')

        ## cos for year and quarter filters 
        col1,col2=st.columns(2)
        with col1:
            state=st.selectbox('State',list(df1['state'].unique()))

            # st.write(year)
        with col2:
            year=st.selectbox('Year',list(df1['year'].unique()))

        ################################# Figure 1 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Insurance Engagement</h2>""",unsafe_allow_html=True)

        #calling Engagement Across States Function
        insurance_engagement(year,state,df1)

        ################################# Figure 2 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Insurance Engagement Trend</h2>""",unsafe_allow_html=True)
        #calling Engagement Trend Function
        insurance_trend_districts(year,state,df1)

    elif drop_down=="5.Transaction Analysis Across States and Districts":
        st.markdown("""<h1 style='color: blue; font-size: 30px; font-family: Arial; text-align: left;'>
        Top Performing States and Districts</h1>""",unsafe_allow_html=True)

        ##### Common SQL Query for Entire Page ###############
        # SELECT * FROM phonepe_pulse.top_transaction;
        #### SQL Query for Enitre Page ###############
        query="""SELECT * FROM phonepe_pulse.top_transaction;"""

        ### running sql query runner function to get the dataframe for above sql query
        sql_df=sql_query_runner(query)
        sql_df.columns=sql_df.columns.str.lower()



        ################################# Figure 1 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Top Performing Districts</h2>""",unsafe_allow_html=True)

        year=st.selectbox('Year',list(sql_df['year'].unique()))

        #calling Top 10 Districts Function
        top_10_districts(sql_df,year)

        ################################ Figure 2 #################################################
        st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        Top Performing States</h2>""",unsafe_allow_html=True)

        #calling Top 10 States Function
        top_states(sql_df,year)

        # ################################# Figure 3 #################################################
        # st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
        # Top Performing Pincodes</h2>""",unsafe_allow_html=True)

        # #calling Top 10 States Function
        # top_10_pincodes(sql_df,year)


            # ################################# Figure 4 #################################################
            # st.markdown("""<h2 style='color: red; font-size: 25px; font-family: Arial; text-align: left;'>
            # Top 10 States Trend</h2>""",unsafe_allow_html=True)

            # #calling Top 10 States Function
            # top_10_trend(sql_df)





        




