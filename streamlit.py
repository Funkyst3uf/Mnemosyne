# NOM : streamlit.py
# ROLE : application FastAPI sur le thème de la musique (playlist)
# AUTEUR : Jonathan Ntoula,  dans le cadre du cours Outils Collaboratifs (P. Kislin)
# Université Paris 8, IED
# VERSION : 0.1 du 20/08/2022
# Exécution (w/ Uvicorn) : uvicorn ma-playlist-app --reload

import streamlit as st
from exif import Image
from PIL import Image as P_Image
from geopy.geocoders import Nominatim

st.markdown("<h1 style='text-align: center; color: black;'>Outils Collaboratifs : TD 4</h1>", unsafe_allow_html=True)
st.write('') # saute une ligne

# crée des conteneurs (colonnes)
col1, col2, col3 = st.columns(3)

# affiche l'image avec PIL
image = P_Image.open('mnemo.jpg')   # placez l'image dans le repertoire d'exécution de streamlit

with col2 : # place l'image dans le conteneur 2 (au cente de la page)
    st.image(image, caption='Mnemosyne, D. G. Rossetti (1875-1881)')
    
# appel de l'outil Nominatim (pour géolocation)
loc = Nominatim(user_agent="GetLoc")
 

# traitement de l'image (exif)
with open('./mnemo.jpg', 'rb') as img_file:
    img = Image(img_file)

st.write('\n') # saute une ligne
st.markdown("<h2 style='text-align: center; color: black;'>Modifiez les tags EXIF de l'image</h2>", unsafe_allow_html=True)

# Création / modification des tags Exif selon saisie utilisateur
st.write('') # saute une ligne
copyright = st.text_input("Copyright de l'image : ")
if copyright : img.copyright = copyright

artist = st.text_input("Nom du photographe : ")
if artist : img.artist = artist

image_description = st.text_input("Description de l'image : ")
if image_description : img.image_description = image_description

datetime = st.text_input("Date des dernières modifications (YYYY:MM:DD HH:MM:SS): " )
if datetime : img.datetime = datetime

make = st.text_input("Constructeur de l'appareil photo utilisé : ")
if make : img.make = make

model = st.text_input("Modèle de l'appareil : ")
if model : img.model = model

software = st.text_input("Software de l'appareil : ")
if software : img.software = software

adresse = st.text_input("Quelle est votre adresse (ville ou adresse complète) ? ")
getLoc = loc.geocode(adresse)
if adresse :
    img.gps_latitude = getLoc.latitude
    img.gps_longitude = getLoc.longitude

# Liste les tags Exif  de l'image (pour test)
#st.write(sorted(img.list_all()))

# Sauvegarde les modifications
with open(f'./mnemo.jpg', 'wb') as new_img_file:
    new_img_file.write(img.get_file())
    
# réouverture de l'image en mode lecture pour vérifier les métadonnées
with open('./mnemo.jpg', 'rb') as img_file:
    img = Image(img_file)
    
# Affiche les métadonnées à jour
st.write('') # saute une ligne
st.header('Rappel des métadonnées enregistrées')

st.write(f'Copyright : {img.get("copyright")}')
st.write(f'Artiste : {img.get("artist")}')
st.write(f'Description de l\'image : {img.get("image_description")}')
st.write(f'Date de dernière modification : {img.get("datetime")}')
st.write(f'Marque de l\'appareil photo : {img.get("make")}')
st.write(f'Modèle de l\'appareil : {img.get("model")}')
st.write(f'Version du soft/firmware : {img.get("software")}')
st.write('') # saute une ligne

st.write('Coordonnées GPS du lieu de prise de vue :')
st.write(f'Latitude : {img.get("gps_latitude")}')
st.write(f'Longitude : {img.get("gps_longitude")}')
