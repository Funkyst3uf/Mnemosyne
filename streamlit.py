# NOM : streamlit.py
# ROLE : application FastAPI sur le thème de la musique (playlist)
# AUTEUR : Jonathan Ntoula,  dans le cadre du cours Outils Collaboratifs (P. Kislin)
#  Université Paris 8, IED
# VERSION : 0.1 du 20/08/2022
# Exécution (w/ Uvicorn) : uvicorn ma-playlist-app --reload

import streamlit as st
from exif import Image
from PIL import Image as P_Image
from geopy.geocoders import Nominatim


# crée des conteneurs (colonnes)
col1, col2, col3 = st.columns(3)

# affiche l'image avec PIL
image = P_Image.open('mnemo.jpg')   # placez l'image dans le repertoire d'exécution de streamlit

with col2 : # place l'image dans le conteneur 2 (au cente de la page)
    st.image(image, caption='Mnemosyne, de D. G. Rossetti')
    
# appel de l'outil Nominatim (pour géolocation)
loc = Nominatim(user_agent="GetLoc")
 

# traitement de l'image (exif)
with open('./mnemo.jpg', 'rb') as img_file:
    img = Image(img_file)

st.title("Modifiez les tags EXIF de l'image")

# Création / modification des tags Exif selon saisie utilisateur
Make = st.text_input("Constructeur de l'appareil photo : ")
img.Make = Make

Model = st.text_input("Modèle de l'appareil : ")
img.Model = Model

DateTime = st.text_input("Date des dernières modifications (YYYY:MM:DD HH:MM:SS): " )
img.DateTime = DateTime

Description = st.text_input("Description de l'image : ")
img.Description = Description

Copyright = st.text_input("Copyright de l'image : ")
img.Copyright = Copyright

Artist = st.text_input("Artiste photographié ou auteur de l'oeuvre photgraphiée : ")
img.Artist = Artist

Comment = st.text_input("Commentaire : ")
img.Comment = Comment

adresse = st.text_input("Quelle est votre adresse (ville ou adresse complète) ? ")
getLoc = loc.geocode(adresse)
if adresse :
    img.GPSLatitude = getLoc.latitude
    img.GPSLongitude = getLoc.longitude

# Liste les tags Exif  de l'image (pour test)
#st.write(sorted(img.list_all()))

# Sauvegarde les modifications
with open(f'./mnemo.jpg', 'wb') as new_img_file:
    new_img_file.write(img.get_file())
    
    

# réouverture de l'image en mode lecture pour vérifier les métadonnées
with open('./mnemo.jpg', 'rb') as img_file:
    img = Image(img_file)
    
# Affiche les métadonnées à jour
st.write(f'Make: {img.get("Make")}')
st.write(f'Model : {img.get("Model")}')
st.write(f'DateTime : {img.get("DateTime")}')
st.write(f'Orientation : {img.get("Orientation")}')
st.write(f'Compression : {img.get("Compression")}')
st.write(f'Description : {img.get("Description")}')
st.write(f'Copyright : {img.get("Copyright")}')
st.write(f'Artist : {img.get("Artist")}')
st.write(f'Comment : {img.get("Comment")}')
st.write(f'GPSLatitude : {img.get("GPSLatitude")}')
st.write(f'GPSLongitude : {img.get("GPSLongitude")}')
