# NOM : streamlit.py
# ROLE : application streamlit, permettant notamment de modifier les metadatas EXIF d'une image
# AUTEUR : Jonathan Ntoula,  dans le cadre du cours Outils Collaboratifs (P. Kislin)
# Université Paris 8, IED
# VERSION : 0.1 du 20/08/2022
# Exécution (w/ streamlit) : streamlit run streamlit.py

import streamlit as st
from exif import Image
from PIL import Image as P_Image
from geopy.geocoders import Nominatim # pour récupérer les coordonnées GPS
import pandas as pd
import pydeck as pdk
from streamlit_folium import folium_static
import folium

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


# troisième partie de l'exercice

data = pd.DataFrame({
    #'awesome cities' : ['PloucLand'],
    'lat' : [img.get("gps_latitude")],
    'lon' : [img.get("gps_longitude")]
})

st.map(data)


st.write('') # saute une ligne
st.markdown("<h2 style='text-align: center; color: black;'>A travers le monde ...</h2>", unsafe_allow_html=True)


# Quatrième partie de l'exercice

# centre la carte en Turquie
m = folium.Map(location=[38.7322200, 35.4852800], zoom_start=2)

tooltip = "Cliquez"

folium.Marker( # Suresnes
    [48.87090530000104, 2.2255727000001513], popup="Suresnes", tooltip="Suresnes"
).add_to(m)

folium.Marker( # Pontivy
    [48.066152, -2.967056], popup="Pontivy", tooltip="Pontivy"
).add_to(m)

folium.Marker( # Hamamastu (Japon)
    [34.710834, 137.726126], popup="Hamamatsu", tooltip="Hamamatsu"
).add_to(m)

folium.Marker( # Toronto
    [43.653226, -79.3831843], popup="Toronto", tooltip="Toronto"
).add_to(m)

folium.Marker( # Hambourg
    [53.551085, 9.993682], popup="Hamburg", tooltip="Hambourg"
).add_to(m)

folium.Marker( # Barcelone
    [41.3887900, 2.1589900], popup="Barcelone", tooltip="Barcelone"
).add_to(m)

folium.Marker( # Wiesbaden
    [50.0782184, 8.2397608], popup="Wiesbaden", tooltip="Wiesbaden"
).add_to(m)

folium.Marker( # Prague
    [50.0755381, 14.4378005], popup="Prague", tooltip="Prague"
).add_to(m)

folium.Marker( # Londres
    [51.5073509, -0.1277583], popup="Londres", tooltip="Londres"
).add_to(m)

folium.Marker( # Les Açores
    [38.305542, -30.384108], popup="Les Açores", tooltip="Les Açores"
).add_to(m)

folium.Marker( # Belfort
    [47.639674, 6.863849], popup="Belfort", tooltip="Belfort"
).add_to(m)

folium.Marker( # Interlaken (Suisse)
    [46.6873837, 7.8695505], popup="Interlaken", tooltip="Interlaken"
).add_to(m)

folium.Marker( # Amsterdam
    [52.370216, 4.895168], popup="Amsterdam", tooltip="Amsterdam"
).add_to(m)

folium.Marker( # Ajaccio
    [41.919229, 8.738635], popup="Ajaccio", tooltip="Ajaccio"
).add_to(m)

folium.Marker( # Frankfurt
    [50.1109221, 8.6821267], popup="Frankfurt", tooltip="Frankfurt"
).add_to(m)

folium.Marker( # Les Arcs / Bourg Saint Maurice
    [45.618598, 6.769548], popup="Les Arcs", tooltip="Les Arcs"
).add_to(m)

folium.Marker( # Aurillac
    [44.9308, 2.44482], popup="Aurillac", tooltip="Aurillac"
).add_to(m)

folium.Marker( # Noirmoutier
    [46.9998997, -2.2438923], popup="Noirmoutier", tooltip="Noirmoutier"
).add_to(m)

folium.Marker( # Tokyo
    [35.6894, 139.692], popup="Tokyo", tooltip="Tokyo"
).add_to(m)

folium.Marker( # Bordeaux
    [44.8378, -0.594], popup="Bordeaux", tooltip="Bordeaux"
).add_to(m)


# affichage de la carte avec tous ses marqueurs
folium_static(m)
