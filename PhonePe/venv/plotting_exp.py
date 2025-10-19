import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title('Title')


data=pd.DataFrame(
    np.random.rand(100,3),
    columns=['A','B','C']
)

# st.write(data)

# st.line_chart(data,y=['A'])

# st.area_chart(data,y=['A'])
# st.bar_chart(data,y=['A'])

# fig,ax=plt.subplots()

# ax.scatter(data['A'],data['B'])

# st.pyplot(fig)

#altiar chart

# chart=alt.Chart(data).mark_circle().encode(x='A',y='B')

# st.altair_chart(chart,use_container_width=True)  ## to make size zoom in and zoom out

## Flow Chart

st.graphviz_chart("""

digraph{

watch -> like                  
like -> comment
comment -> share
share ->watch                                    

}

""")


# displaying Dataframe
data = pd.DataFrame({
    'lat': [37.7749, 40.7128, 34.0522, 41.8781, 47.6062],
    'lon': [-122.4194, -74.0060, -118.2437, -87.6298, -122.3321]
})

st.map(data)