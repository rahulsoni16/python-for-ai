import os
from dotenv import load_dotenv
import streamlit as st

from GenerateReceipe import generate_receipe


load_dotenv()


st.title("Recipe Generator")

st.markdown("Enter ingredients (comma-separated), cuisine and dietary preference.")

ingredients_input = st.text_area("Ingredients (comma-separated)", height=120)
cuisine = st.text_input("Cuisine", value="Any")
diet = st.text_input("Dietary preference", value="Any")

if st.button("Generate recipe"):
    ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]
    if not ingredients:
        st.error("Please provide at least one ingredient.")
    else:
        with st.spinner("Generating recipe..."):
            try:
                recipe = generate_receipe(ingredients, cuisine, diet)
            except Exception as e:
                st.error(f"Error generating recipe: {e}")
            else:
                st.subheader("Recipe")
                st.text_area("", value=recipe, height=300)
                try:
                    with open("receipe_output.txt", "a") as f:
                        f.write(recipe + "\n\n")
                    st.success("Saved to receipe_output.txt")
                except Exception as e:
                    st.warning(f"Could not save to file: {e}")
