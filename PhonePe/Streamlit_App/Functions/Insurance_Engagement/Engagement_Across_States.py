from Functions.config import *
from Functions.State_Map import state_map 

def insurance_engagement(year,state,df):
    df.columns=df.columns.str.lower()

    # df=df[df['engagement_type']=='insurance']

    df=df[(df['state']==state)&(df['year']==year)]

    # df=state_map(df,'state')

    # st.write(df.shape)
    df_rows=df.shape[0]
    if df_rows==0:
        st.warning(f'No Data Available for Insurance Engagement')
        return

    india_map_path=os.getenv("india_geo")

    ### using geopandas json to take unique values
    gdf = gpd.read_file(india_map_path)

    # Merge all districts into single state geometries
    state_gdf = gdf.dissolve(by="st_nm")

    # Save to a new file
    state_gdf.to_file(india_map_path, driver="GeoJSON")

    with open(india_map_path, "r") as f:
        india_geo = json.load(f)

    color_scales = ['Greens']

    #grouping at state level
    df2=df[['district_name','insurance_amount','insurance_count']].groupby(['district_name']).sum().reset_index()

    df2=df2.sort_values(by=['insurance_amount'],ascending=False)

    fig=px.bar(df2,x='district_name',y='insurance_amount',labels={'insurance_amount':'Total Insurance Amount','district_name':'District Name'}
               ,barmode='group',height=500,title=f'Insurance Amount Across States for {year}'
            #    ,category_orders={'Quarter': [1, 2, 3, 4]}
            #    ,hover_data={'insurance_amount': ':.2f', 'percentage': False})
            )
    st.plotly_chart(fig,use_container_width=False)