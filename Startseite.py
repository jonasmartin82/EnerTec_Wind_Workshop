
import streamlit as st

st.set_page_config(page_title = "EnerTec Wind Workshop", layout = "wide")

st.logo('Logo_EnerTec_ohne_Hintergrund.png')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('Logo_Stiftung_ohne_Hintergrund.png', width=250)
    
with col2:
    st.image('Logo_EnerTec_ohne_Hintergrund.png', width=250)
    
with col3:
    st.image('Logo_AES_ohne_Hintergrund.png', width=250)
    
# ------------------------------------------------------------------------------------------------------------------------ #

st.title("Startseite")

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Bitte lesen!')

st.write('Herzlich Willkommen im EnerTec!')

st.write('Ihr befindet euch auf der Startseite des Wind Workshops.')

st.write('Diese Internetseite ist interaktiv aufgebaut. Ihr könnt in der Seitenleiste links die verschiedenen Seiten auswählen und entsprechend verwenden. Diese Webseite enthält mehrere Versuche aus denen ihr auswählen könnt, je nachdem was euch am meisten interessiert. Eine Übersicht über den Inhalt der Versuche findet ihr weiter unten.')

st.write('Zusätzlich gibt es noch weitere Seiten mit Zusatzinformationen und Erklärungen, wenn ihr euch intensiver mit einem Thema beschäftigen möchtet. Außerdem findet ihr auf der Seite "Aufbau Versuchskoffer" eine detaillierte Erklärung, wie ihr den Versuchskoffer für die Experimente aufbauen müsst. Auf jeder Seite eines Versuches findet ihr nochmals ein Bild zur Kontrolle des Aufbaus.')

st.write('Bei Fragen meldet euch gerne bei den Betreuern. Ansonsten: jetzt seid ihr dran, viel Spaß beim Experimentieren!')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Übersicht Versuche')

st.write('Hier findet ihr eine Übersicht der angebotenen Versuche mit dem Titel und einer kurzen Beschreibung')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 1: Ausgangsleistung einer Windkraftanlage in Abhängigkeit der Flügelanzahl')

st.write('In diesem Versuch bestimmt ihr die Ausgangsleistung einer Windkraftanlage für verschiedene Anzahlen an Flügeln. Wir betrachten die Ergebnisse , bestimmen die optimale Flügelanzahl und diskutieren, warum reale Windkraftanlagen oftmals drei Flügel besitzen. Ein weiterführendes Experiment dazu ist Versuch 2, in dem ihr den Anstellwinkel der Flügel variiert.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 2: Ausgangsleistung einer Windkraftanlage in Abhängigkeit des Anstellwinkels')

st.write('Dieser Versuch beschäftigt sich mit dem Anstellwinkel der Flügel einer Windkraftanlage. Neben der Anzahl der Flügel und der Windgeschwindigkeit hat der Winkel einen großen Einfluss auf die Effizienz beziehungsweise Leistung der Windkraftanlage. Dazu führt ihr eine Messreihe durch um den optimalen Winkel zu bestimmen und fomruliert eure Gedanken, warum das so ist.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 3: Ausgangsleistung einer Windkraftanlage in Abhängigkeit der Windgeschwindigkeit')

st.write('Hier soll es um den Einfluss der Windgeschwindigkeit auf die Ausgangsleistung gehen. Wenn es nicht mehr möglich ist, eine Windkraftanlage an sich zu optimieren, geht es an die Suche nach dem besten Standort. Um diesen Prozess und den Einfluss der Windgeschwindigkeit besser verstehen zu können, testet ihr hier mit verschiedenen Windgeschwindigkeiten und betrachtet eine Windkarte von Deutschland um nachvollziehen zu können, wo man am besten Windkraftanlagen platziert.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 4: Messungen am Savonius-Generator')

st.write('Im Gegensatz zu den übrigen Versuchen betrachten wir hier eine Windkraftanlage mit einer vertikalen Achse. Ihr untersucht die Funktion dieses Typs der Anlage, bestimmt das Verhalten mit und ohne Spalt und zeichnet eine Strom-Spannungs-Kennlinie auf.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #







