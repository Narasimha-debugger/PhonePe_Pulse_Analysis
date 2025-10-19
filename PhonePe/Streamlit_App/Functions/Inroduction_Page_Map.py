# import streamlit as 
from Functions.config import *
from Functions.State_Map import state_map 

def quarterly_india_map_introduction_page(year,quarter,state_trans_data):
    # filteting the datafrane for the given year and quarter
        df=state_trans_data[(state_trans_data['year']==year)&(state_trans_data['quarter']==quarter)]
        df=df.groupby('state').sum().reset_index()
        df=df[['state','transaction_amount']]

        # reading the GeoJson File
        new_df=df.copy()
        new_df=state_map(new_df,'state')
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
            # 'Reds', 'Blues', 'Greens', 'Viridis', 'Cividis', 'Plasma', 'Inferno', 'Magma', 'Oranges', 'PuRd', 'YlGnBu', 'RdYlBu']

        for scale in color_scales:
            fig = px.choropleth(
                new_df,geojson=india_geo,locations='state',featureidkey="properties.st_nm",
                color='transaction_amount',color_continuous_scale=scale,title=f'PhonePe Transaction by State'
                ,hover_name='state',hover_data={'transaction_amount':':,.2f'},)
            fig.update_layout(title_font=dict(family="Arial", size=24, color="blue"))
            fig.update_geos(fitbounds="locations", visible=False)
            # fig.update_traces(marker_line_color='black', marker_line_width=1.5)
            st.plotly_chart(fig,use_container_width=False)

        # fig = go.Figure()

        # #  Choropleth base (colored states)
        # fig.add_trace(go.Choroplethmapbox(
        #     geojson=india_geo,
        #     locations=new_df['state'],
        #     z=new_df['transaction_amount'],
        #     featureidkey="properties.st_nm",
        #     colorscale="Purples",
        #     zmin=0, zmax=new_df['transaction_amount'].max(),
        #     marker_opacity=0.6,
        #     marker_line_width=0
        # ))

        # # Overlay 3D-like bubbles/bars
        # fig.add_trace(go.Scattermapbox(
        #     lat=df['lat'],
        #     lon=df['lon'],
        #     mode='markers',
        #     marker=go.scattermapbox.Marker(
        #         size=df['transaction_amount'] / df['transaction_amount'].max() * 50,
        #         color=df['transaction_amount'],
        #         colorscale='Purples',
        #         sizemode='area',
        #         opacity=0.9
        #     ),
        #     text=df['state'],
        #     hoverinfo='text+lat+lon'
        # ))

        # fig.update_layout(
        #     mapbox_style="carto-positron",
        #     mapbox_zoom=4,
        #     mapbox_center={"lat": 22, "lon": 78},
        #     height=700,
        #     margin={"r":0,"t":30,"l":0,"b":0}
        # )

        # st.plotly_chart(fig, use_container_width=True)