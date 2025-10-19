import streamlit as st
import pandas as pd

# st.title('Streamlit Session')

# st.header("Header")
# st.subheader('Sub Header')

# st.markdown("""

# # h1 tag
# ## h2 tag
# ### h3 tag
            
# :sun: <br>
# :joy:
# :sunglasses:

            
# **time**
# _time_                   
            
# """,True)

# st.write('The Numbers are',1,2,3,4)
# st.write('## There is a text',':joy:')

# # Display Dictionary

# dic={
#     'name':'Naga',
#     'age':25,
#     'Place':'Hyderabad'
# }
# st.write(dic)

## displaying Dataframe
# data = pd.DataFrame({
#     'lat': [37.7749, 40.7128, 34.0522, 41.8781, 47.6062],
#     'lon': [-122.4194, -74.0060, -118.2437, -87.6298, -122.3321]
# })

# st.write(data)

# st.dataframe(data)

## Json file

data_json={
    "user_id": 12345,
    "user_info": {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 29
    },
    "purchases": [
        {
            "item_id": "A001",
            "item_name": "Laptop",
            "price": 1200.99,
            "quantity": 1
        },
        {
            "item_id": "B002",
            "item_name": "Mouse",
            "price": 25.50,
            "quantity": 2
        }
    ],
    "timestamp": "2024-08-11T15:30:00Z"
}

# st.json(data_json,expanded=False)

st.metric("TCS Stock",value=889,delta=12.5)

st.metric("TCS Stock",value=889,delta=12.5,delta_color='normal')