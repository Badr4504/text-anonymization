import spacy
import re
import streamlit as st
nlp=spacy.load('en_core_web_lg')
st.title('**Text Anonymization Tool**')
st.header('Welcome!')
user_input=st.text_input('_Write your input text:_')

def anonym_nlp(text):
    global fullanonymtext
    doc=nlp(text)
    entities=[]
    for token in doc:
        if token.ent_type:
            entity=f'<{token.ent_type_}>'
            entities.append(entity)
        else:
            entities.append(token.text)
    st.write('##### _The anonymized version of your text:_')
    fullanonymtext=' '.join(entities)    
    return  st.write(fullanonymtext)

def anonym_mail():
    global substitute
    email_pattern="[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{,3}"
    substitute=re.sub(email_pattern,'<email>',user_input)

def anonym_phone():
    global substitute
    phone_pattern="\+?\d{10,15}"
    substitute=re.sub(phone_pattern,'<phone>',substitute)

def main():
    anonym_mail()
    anonym_phone()
    anonym_nlp(substitute)
    st.write('###### Click the button below to save the anonymized version of your text:')
    pressed=st.download_button(label='download file',data=fullanonymtext,file_name='anonymtext.txt')

main()
