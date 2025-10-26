
import streamlit as st
from datetime import date

# Language options
languages = {"English": "en", "Français": "fr"}

# Translations
t = {
    "en": {
        "title": "Daily Pain Tracker",
        "date": "Date",
        "pain_level": "Pain level today (0 = none, 10 = worst)",
        "pain_location": "Where is the pain located?",
        "pain_type": "Type of pain",
        "worsened_by": "What made it worse today?",
        "helped_by": "What helped reduce the pain?",
        "medications": "Medications used today",
        "mood": "Mood (1 = low, 5 = good)",
        "sleep": "Sleep quality (1 = poor, 5 = restful)",
        "summary": "Summary of Today’s Pain Log"
    },
    "fr": {
        "title": "Suivi Quotidien de la Douleur",
        "date": "Date",
        "pain_level": "Niveau de douleur aujourd'hui (0 = aucune, 10 = maximale)",
        "pain_location": "Où se situe la douleur ?",
        "pain_type": "Type de douleur",
        "worsened_by": "Qu'est-ce qui a aggravé la douleur ?",
        "helped_by": "Qu'est-ce qui a aidé à soulager la douleur ?",
        "medications": "Médicaments utilisés aujourd'hui",
        "mood": "Humeur (1 = basse, 5 = bonne)",
        "sleep": "Qualité du sommeil (1 = faible, 5 = reposant)",
        "summary": "Résumé du journal de la douleur d'aujourd'hui"
    }
}

# Language selection
lang_choice = st.sidebar.selectbox("Language / Langue", list(languages.keys()))
lang = languages[lang_choice]
labels = t[lang]

st.title(labels["title"])

# Inputs
today = st.date_input(labels["date"], date.today())
pain_level = st.slider(labels["pain_level"], 0, 10, 0)
pain_locations = st.multiselect(labels["pain_location"], ["Head", "Neck", "Upper back", "Lower back", "Hips", "Knees"] if lang == "en" else ["Tête", "Cou", "Haut du dos", "Bas du dos", "Hanches", "Genoux"])
pain_types = st.multiselect(labels["pain_type"], ["Aching", "Burning", "Sharp", "Throbbing", "Electric"] if lang == "en" else ["Douloureux", "Brûlante", "Aiguë", "Pulsatile", "Électrique"])
worsened_by = st.text_input(labels["worsened_by"])
helped_by = st.text_input(labels["helped_by"])
medications = st.text_input(labels["medications"])
mood = st.slider(labels["mood"], 1, 5, 3)
sleep = st.slider(labels["sleep"], 1, 5, 3)

# Display summary
st.markdown("---")
st.subheader(labels["summary"])
st.markdown(f"**{labels['date']}:** {today}")
st.markdown(f"**{labels['pain_level']}:** {pain_level}")
st.markdown(f"**{labels['pain_location']}:** {', '.join(pain_locations)}")
st.markdown(f"**{labels['pain_type']}:** {', '.join(pain_types)}")
st.markdown(f"**{labels['worsened_by']}:** {worsened_by}")
st.markdown(f"**{labels['helped_by']}:** {helped_by}")
st.markdown(f"**{labels['medications']}:** {medications}")
st.markdown(f"**{labels['mood']}:** {mood} / 5")
st.markdown(f"**{labels['sleep']}:** {sleep} / 5")
