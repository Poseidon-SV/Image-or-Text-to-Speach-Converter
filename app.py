import streamlit as st
from gtts import gTTS
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'
convert = False
language = 'en'

st.header("Image-to-Text / Text-to-Speech Converter 🔊")

inputText = st.text_area('Please enter english text here to convert it into a speach:')
st.markdown("### OR")
input_img = st.file_uploader("Upload an image containing text:" )

if input_img:
    st.image(input_img, caption='Your uploded image')

convert = st.button('Convert Text-to-Speach')

if convert:
    if input_img:
        inputText = pytesseract.image_to_string(Image.open(input_img))
    if not inputText or inputText == str() :
        inputText = 'Please enter text to convert it into speach'

    mytts = gTTS(text=inputText, lang=language, slow=False, tld='com.au')
    try:
        mytts.save("tts.ogg")

        tts_file = open('tts.ogg', 'rb')
        tts_audio = tts_file.read()

        st.write('Input text:',inputText)
        st.audio(tts_audio, format='audio/ogg')
    except:
        st.write(':red[There is no text or image file!]')
