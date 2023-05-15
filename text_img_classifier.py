import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import time
import tensorflow as tf
from tensorflow.keras.utils import img_to_array, load_img
from tensorflow import keras
import io
from PIL import ImageOps, Image


# @st.cache(allow_output_mutation=True)
page = st.sidebar.selectbox(
    'MENU',
    ('Main', 'About', 'Categorizing')
)
if page == 'Main':
    st.markdown('<p class="font"> Be a Best Seller! </p>', unsafe_allow_html=True)
    st.title('Where My Product To Be Displayed?')
    st.markdown(""" <style> .font {font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.subheader("Find out in which shopping mall category your products should be.")
    st.image("image/images_1.jpeg")


elif page == 'About':
    st.title('Why Proper Categorization is Important?')
    st.write("About 60% of consumers use search engines to research the item before making a purchase. [link](https://www.google.com/search?q=DuplicateWidgetID&rlz=1C1RXQR_enUS1052US1052&oq=DuplicateWidgetID&aqs=chrome..69i57.1336j0j7&sourceid=chrome&ie=UTF-8)") 
    st.write("You can make your product show up not by only updating your product name and preparing your product listing, but also should categorize your products correctly.")
    # st.write("Product categorization is how a marketplace or ad platform put  your products into hierarchical categories.")
    st.write("Proper categorization plays an important role in how well your products are discoverable and how often you can reach out to right shoppers.")
    st.image("image/download.jpeg", width= 100)
    st.caption("Copyright Kozzi.com")

elif page =='Categorizing':
    st.title("Let's find where to display your items in an online mall.")
    st.write("Categories: Apparel & Accessories, Arts & Entertainment, Baby & Toddler, Business & Industrial, Cameras & Optics, Cell Phones, Computers & Tablets, Consumer Electronics, Health & Beauty, Home & Garden, Jewelry & Watches, Media, Pet Supplies, Sporting Goods, Toys & Games, Vehicles")
    model_1, model_2, model_3 = st.tabs(["Product Title", "Product Image", "Product Title & Image"])

    with model_1:

        st.write("Please type your product title descrbing your product.")
    
        product_title = st.text_input("Enter the product name.", key = "<1>") 

        st.write("Your product name is:")
        st.title(product_title)

        if st.button("Category of Product", key = "<8>"):
       
            text_model = pickle.load(open('text_model_lgr.pkl','rb'))
            input=[product_title]
            result = text_model.predict(input)
            st.text(f"Your product category is: {result}")


    with model_2:
       
        def load_model():
            model = tf.keras.models.load_model('./image_modelfl15.hdf5')
            return model

        def predict_class(image, model):
            image = tf.cast(image, tf.float32)
            image = tf.image.resize(image, [150, 150])
            image = np.expand_dims(image, axis = 0)
            prediction = model.predict(image)
            return prediction

        model = load_model()
        
        file = st.file_uploader("Please upload an item image file", type=["jpg", "png"], key = "<9>")

        if file is None:
            st.text('Waiting for upload....')

        else:
            slot = st.empty()
            slot.text('Running...')
            test_image = Image.open(file)
            st.image(test_image, caption="Input Image", width = 400)
            pred = predict_class(np.asarray(test_image), model)
            class_names = ['Apparel_Accessories', 'Arts_Entertainment', 'Baby_Toddler', 'Business_Industrial', 'Cameras_Optics', 'Cell Phones', 'Computers_Tablets', 'Consumer Electronics', 'Health_Beauty', 'Home_Garden', 'Jewelry_Watches', 'Pet Supplies', 'Sporting Goods', 'Toys_Games', 'Vehicles']
            result = class_names[np.argmax(pred)]

            output = 'Your item category is: ' + result
            slot.text('Done')
            st.success(output)


       
    with model_3:
     
        product_name = st.text_input("Enter the product name.", key = "<3>") 

        st.write("Your product name is:")
        st.title(product_name)

 
        def load_model():
            model = tf.keras.models.load_model('./image_modelfl15.hdf5')
            return model

        def predict_class(image, model):
            image = tf.cast(image, tf.float32)
            image = tf.image.resize(image, [150, 150])
            image = np.expand_dims(image, axis = 0)
            prediction = model.predict(image)
            return prediction

        model = load_model()
        
        # st.subheader('Find where to display your items in an online mall.')
        file = st.file_uploader("Please upload an item image file", type=["jpg", "png"], key = "<10>")

        if file is None:
            st.text('Waiting for upload....')

        else:
            slot = st.empty()
            slot.text('Running...')
            test_image = Image.open(file)
            st.image(test_image, caption="Input Image", width = 400)
            pred = predict_class(np.asarray(test_image), model)
            class_names = ['Apparel_Accessories', 'Arts_Entertainment', 'Baby_Toddler', 'Business_Industrial', 'Cameras_Optics', 'Cell Phones', 'Computers_Tablets', 'Consumer Electronics', 'Health_Beauty', 'Home_Garden', 'Jewelry_Watches', 'Pet Supplies', 'Sporting Goods', 'Toys_Games', 'Vehicles']
            result_im = class_names[np.argmax(pred)]
            # im_prob = model.predict(test_image)[0][0]*100
            # output = f'Your item category is: ' + result
            # slot.text('Done')
            # st.success(output)


        if st.button("Category of Product", key = "<6>"):
    
            text_model = pickle.load(open('text_model_lgr.pkl','rb'))
            input=[product_title]
            result = text_model.predict(input)[0]
            # text_prob = text_model.predict_proba(input)[0][0]*100

            # if text_prob >= im_prob:
            st.text(f"Your product category based on prodcut title is {result}.")
            # else:
            st.text(f"The category of your product based on the image is {result_im}.")

        st.set_option('deprecation.showfileUploaderEncoding', False)