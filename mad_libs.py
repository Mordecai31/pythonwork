import streamlit as st
import random

#Title
st.title("Mad Libs game")
st.subheader("Create your own story")

theme=st.selectbox("Choose a story:",["Adventure","Mystery","Fantasy"])
# User inputs
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")
emotion = st.text_input("Enter an emotion:")
# Story templates
stories = {
    "Adventure": [
          f"Once upon a time, a {adjective} {noun} {verb} across the {place} with a {animal}. It was a truly {emotion} adventure!",
        f"In the heart of the {place}, a {adjective} {noun} decided to {verb} with a {animal}. The crowd was filled with {emotion}!"
    ],
    "Mystery": [
        f"A {adjective} {noun} was found {verb} near the {place}. Detectives believed the {animal} knew something. Everyone felt {emotion}.",
        f"The lights flickered in the {place}. A {noun} was missing, and only a {adjective} {animal} was seen {verb}. People whispered in {emotion}."
    ],
    "Fantasy": [
        f"In the magical land of {place}, a {adjective} {noun} and their {animal} had to {verb} to save the kingdom. Their {emotion} was their strength.",
        f"Legends say a {adjective} {noun} once {verb} across {place} riding a flying {animal}. It was the start of a(n) {emotion} era."
    ]
}
#Generate story
if st.button("create story"):
    if all([noun,verb,adjective,place,animal,emotion]):
        story=random.choice(stories[theme])
        st.markdown("This is your mab story:")
        st.write(story)

        #option to save file
        if st.checkbox("save story to file"):
            with open("your mab_libs story.txt","w") as file:
                file.write(story)
            st.success("story saved as your mab_libs.txt")
    else:
        st.warning("Please fill all the filed to generate your story")