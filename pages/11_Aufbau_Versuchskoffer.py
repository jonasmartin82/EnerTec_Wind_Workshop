
import streamlit as st
import matplotlib.pyplot as plt

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

st.title('Aufbau Versuchskoffer')

st.write('Auf dieser Seite soll der Aufbau des Versuchskoffers beschrieben werden.')

st.write('---')

st.write('Auf dem ersten Bild seht ihr den geöffneten Koffer mit Schaumstoff im Deckel.')

st.image('page_11_pic_1.png')

st.write('---')

st.write('Im Deckel des Koffers ist die Grundplatte verstaut (siehe Bild unten). Nehmt diese aus dem Koffer und platziert sie auf dem Tisch. Richtet sie so aus, dass die rechteckige Aussparung nach links zeigt. So ist der spätere Aufbau einfacher.')

st.image('page_11_pic_2.png')

st.write('---')

st.write('Im nächsten Bild seht ihr einmal alle Komponenten des Koffers. Das Poster an der Wand enthält eine beschriftete Version.')

st.image('page_11_pic_3.png')

st.write('---')

st.write('Auf dem nächsten Bild seht ihr die Grundplatte mit markierten Bohrungen. Die rot markierte Aussparung dient der Aufnahme der Windmaschine, die blau markierten Führungen nehmen den Fuß des Windrads auf und die grün markierten Schlitze dienen der Befestigung der Schutzkappe.')

st.image('page_11_pic_4.png')

st.write('---')

st.write('Im folgenden Bild seht ihr die fertig aufgebaute Station. Dabei sind an dem Windrad noch keine Flügel montiert. Beachtet dabei, dass ihr die Schutzkappe verwendet und so ausrichtet, dass die Winkelskala nach vorne zeigt.')

st.image('page_11_pic_5.png')

st.write('---')

st.write('Hier seht ihr wie die Flügel am Windrad montiert werden. Dazu müsst ihr mit dem Schraubenzieher (im Koffer unter dem Windrad) die schwarzen Schrauben ein Stück weit lösen. Die Flügel steckt ihr dann in die Bohrungen am Umfang und dreht die Schraube wieder an bis das Blatt nicht mehr wackelt. Dabei habt ihr verschiedene Bohrungen, die in einem bestimmten Winkel angeordnet sind. Ihr könnt entweder zwei, drei oder vier Rotorblätter montieren. Achtet darauf, dass ihr sie symmetrisch ausrichtet.')

col1, col2, col3, col4 = st.columns([0.15, 0.35, 0.35, 0.15])

with col1:
    st.write('')

with col2:
    st.image('page_11_pic_6.png')
    
with col3:
    st.image('page_11_pic_7.png')
    
with col4:
    st.write('')
    
st.write('---')

st.write('Im folgenden seht ihr den kompletten Aufbau mit Flügeln. Je nach Experiment benötigt ihr entsprechend noch weitere Bauteile aus dem Koffer.')

st.image('page_11_pic_8.png')

st.write('---')


