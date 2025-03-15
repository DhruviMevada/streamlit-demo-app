# import streamlit as st
# import pandas as pd
# import numpy as np

# st.write("Hello World")
# st.write("## This is a H2 Title!")
# x = st.text_input("Movie", "Star Wars")

# if st.button("Click Me"):
#     st.write(f"Your favorite movie is `{x}`")


# data = pd.read_csv("movies.csv")
# st.write(data)


# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.bar_chart(chart_data)

import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_path = "Week_6_Dependencies/Dependencies/voting_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Order to Delivery Time Prediction")
st.write("Enter order details to predict the expected delivery time.")

# Input Fields
product_category = st.selectbox("Product Category", ["Electronics", "Books", "Clothing", "Furniture", "Toys"]) # Example categories
customer_location = st.text_input("Customer Location (City)")
shipping_method = st.selectbox("Shipping Method", ["Standard", "Express", "Same-day"])

# Dummy preprocessing (Replace this with actual preprocessing as per dataset)
def preprocess_input(product_category, customer_location, shipping_method):
    return pd.DataFrame({
        'product_category': [product_category],
        'customer_location': [customer_location],
        'shipping_method': [shipping_method]
    })

if st.button("Predict Delivery Time"):
    input_data = preprocess_input(product_category, customer_location, shipping_method)
    prediction = model.predict(input_data)[0]
    st.success(f"Expected Delivery Time: {prediction} days")

