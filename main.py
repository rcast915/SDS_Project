import streamlit as st
import google.generativeai as genai


# Configure Streamlit
st.set_page_config(page_title="Recipes By Gemini")

# Configure generative AI
genai.configure(api_key='AIzaSyBoP5ZEPXCPxujMViMzm4GXTtPop0NGxiA')  # API key
model = genai.GenerativeModel('gemini-pro')

# Initialize list to store ingredients
if 'all_ingredients' not in st.session_state:
    st.session_state.all_ingredients = []

# Streamlit UI components
st.title("Recipes By Gemini")


# Text input for ingredients
ingredient = st.text_input('Enter Ingredient', key='ingredient_input')
if ingredient:
    st.session_state.all_ingredients.append(ingredient)
    st.write('The last added ingredient was:', ingredient)



# Button to display all ingredients
if st.button("Display Ingredients"):
    if st.session_state.all_ingredients:
        st.write("All Ingredients:")
        for i in st.session_state.all_ingredients:
            st.write(i)
    else:
        st.write("No ingredients added yet.")

# Button to reset ingredients list
if st.button("Reset Ingredients"):
    st.session_state.all_ingredients = []

# Function to generate recipe
def generate_recipe(ingredients):
    ingredients = ', '.join(ingredients)
    response = model.generate_content("Generate recipe from the following ingredients: " + ingredients)
    return response.text

if st.button("Generate Recipe"):
    if st.session_state.all_ingredients:
        recipe = generate_recipe(st.session_state.all_ingredients)
        st.write(recipe)
    else:
        st.write('Please provide the ingredients so I can generate a recipe for you.')