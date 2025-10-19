from Functions.config import *
from Functions.State_Map import state_map 

def insurance_trend_india_map(year,quarter,df):

    df.columns=df.columns.str.lower()

    df=df[(df['year']==year)*(df['quarter']==quarter)]

    df=state_map(df,'state')

    # st.write(df.shape)
    df_rows=df.shape[0]
    if df_rows==0:
        st.warning(f'No Data Available for Year {year} and Quarter {quarter}')
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

    color_scales = ['Blues']

    #grouping at state level
    df2=df[['state','insurance_count','insurance_amount']].groupby(['state']).sum().reset_index()

    # fig=px.choropleth(df2,locationmode='India states',locations='state',
    #                   color='insurance_count',
    #                   hover_data=['insurance_count','insurance_count'],
    #                   color_continuous_scale='Blues',
    #                   labels={'insurance_count':'Total Insurance Transactions','state':'State','insurance_amount':'Total Insurance Amount'},
    #                   title=f'Insurance Transactions and Amount Distribution Across States for Year {year} Quarter {quarter}'
    #                  )
    # st.plotly_chart(fig) #showing choropleth map
    for scale in color_scales:
            fig = px.choropleth(
                df,geojson=india_geo,locations='state',featureidkey="properties.st_nm",
                color='insurance_amount',color_continuous_scale=scale,title=f'PhonePe Insurance Amount by State')
            fig.update_layout(title_font=dict(family="Arial", size=24, color="blue"))
            fig.update_geos(fitbounds="locations", visible=False)
            # fig.update_traces(marker_line_color='black', marker_line_width=1.5)
            st.plotly_chart(fig,use_container_width=False)