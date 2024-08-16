
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

st.title("Versuch 4")

st.write('In diesem Versuch beschäftigen wir uns mit dem Savonius Generator. Dabei testet ihr zwei verschiedene Konfigurationen der Turbine, einmal mit offenem und einmal mit geschlossenem Luftspalt. Wir bestimmen die Leistung für beide Konfiguratioenn bei einer festen Windgeschwindigkeit und bestimmen so die bessere Betriebsart. Außerdem lernt ihr hier über Begriffe wie zum Beispiel Aerodynamik.')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau')

col1, col2 = st.columns(2)

with col1:
    st.write('Aufbau Messung offener Spalt')
    st.image('page_4_pic_1.png')
    
with col2:
    st.write('Aufbau Messung geschlossener Spalt')
    st.image('page_4_pic_2.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Achtet auf die richtige Konfiguration damit ihr die Ergebnisse vergleichen könnt! Stellt die Last dazu auf Stufe fünf ein. Beginnt damit eine Tabelle auf einem Blatt anzulegen, die wie folgt aussieht: ')

st.image('page_4_pic_3.png')

st.write('Ihr bestimmt hier die Werte für die Spannung U und die Stromstärke I und berechnet die Leistung P. Dabei ergibt sich die Leistung als Produkt aus Stromstärke und Spannung (das heißt ihr multipliziert die Werte miteinander). Misst dazu einmal Spannung U und Stromstärke I für offenen und geschlossenen Luftspalt und betrachtet euch die Ergebnisse.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Frage')

st.write('Welche Konfiguration des Savonius Generators erzeugt eine größere Ausgangsleistung? Wodurch könnte der Unterschied entstehen?')

st.write('Welchen Vorteil hat ein Vertikalläufer wie unser Savonius Generator hier im Vergleich zu herkömmlichen Horizontalläufern?')

# xxx #

if "Erklärung (Versuch 4)" not in st.session_state:
    st.session_state["Erklärung (Versuch 4)"] = False
 
# xxx #    
    
colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    st.write('')
    if st.button(label='Erklärung (Versuch 4)'):
        st.session_state['Erklärung (Versuch 4)'] = not st.session_state['Erklärung (Versuch 4)']
    
with colC:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 4)']:
    
    st.subheader('Erklärung')
    
    st.write('In der Tabelle unten seht ihr die Werte für beide Konfigurationen. Man sieht klar, dass die Leistung bei offenem Luftspalt deutlich größer ist. Warum dies der Fall ist, könnt ihr mit den Skizzen unten nachvollziehen.')

    st.image('page_4_pic_4.png', width=500)

    st.write('Die beiden Skizzen unten zeigen euch den Luftstrom durch rote Pfeile an und die blauen Pfeile geben die Richtung der Bewegung bzw. der Kräfte an. Man sieht bei der Variante mit dem offenen Luftspalt, dass der Luftstrom durch die Mitte strömt und auf die abgewandte Seite des Savonius Generators trifft und dort eine zusätzliche Kraft generiert, die dem Luftstrom, welcher von außen auf die untere Schaufel trifft und die Bewegung eher abbremst, entgegen wirkt und so die Bewegung eher unterstützt. EInfacher nachzuvollziehen ist der Effekt bei geschlossenem Luftspalt: in diesem Fall gibt es keinen Luftstrom durch die Mitte und die Luft, die von außen auf die untere Hälfte des Savonius Generators trifft, bremst diese nur ab und wirkt der Bewegung entgegen. So wird ersichtlich, dass die Konfiguration mit offenem Luftspalt besser ist, da der Luftstrom hier nicht nur die obere Schaufel nutzt um eine Bewgung zu erzeugen, sondern auch der Luftstrom in der unteren Hälfte einen Effekt bewirkt, der die Bewgung unterstützt oder zumindest nicht abschwächt.')

    col1, col2 = st.columns(2)

    with col1:
        st.write('Skizze Luftstrom offener Luftspalt')
        st.image('page_4_pic_5.png', width=400)
        
    with col2:
        st.write('Skizze Luftstrom geschlossener Luftspalt')
        st.image('page_4_pic_6.png', width=400)
        
    st.write('Die Frage nach dem Vorteil des Savonius Generators als Vertikalläufer gegenüber einem Horizontalläufer ist mit den Skizzen oben auch zu beantworten: egal aus welcher Richtung der Wind auf den Generator trifft, er bewirkt eine Bewegung genau wie sie hier zu sehen ist, sodass ein Vertikalläufer keine Nachführung benötigt um eine sich ändernde Windrichtung auszugleichen.')
    
    st.write('---')

