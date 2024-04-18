import streamlit as st
import spacy
from spacy import displacy

import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper.article import Article


st.title("Named Entity Recognizer")


status = st.radio("Select One Option: ", ('Write A Paragraph', 'Enter a URL'))

if (status == 'Write A Paragraph'):
    
    text = st.text_area("Type Your Paragraph Below")

    if(st.button("Process")):
      doc = nlp(text)
      ent_html = displacy.render(doc, style="ent")
      # Display the entity visualization in the browser:
      st.markdown(ent_html, unsafe_allow_html=True)

    

else:

    url_input = st.text_input("Enter The URL Below:")
    if st.button("Process"):
        article = Article (url_input)
        article.download()
        article.parse()
        doc = nlp(article.text)
        displacy.render(doc, style='ent')
        st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)


