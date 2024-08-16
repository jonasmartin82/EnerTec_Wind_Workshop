
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

st.title("Versuch 2")

st.write('In diesem Versuch bestimmen wir die Ausgangsleistung einer Windkraftanlage in Abhängigkeit des Anstellwinkels. Der optimale Anstellwinkel hängt von der Windgeschwindigkeit ab, also betrachten wir hier zwei verschiedene Windgeschwindigkeiten und sieben verschiedene Winkel. Damit die Messung nicht zu lange dauert, werden euch die Messwerte für 10 m/s zur Verfügung gestellt.')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau')

st.image('page_2_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Wir verwenden hier drei gerade Flügel für das Experiment. Achtet auf die richtige Konfiguration damit ihr die Ergebnisse vergleichen könnt! Beginnt damit eine Tabelle auf einem Blatt anzulegen, die wie folgt aussieht: ')

st.image('page_2_pic_2.png')

st.write('Dabei ist für euch die Tabelle für 10 m/s bereits ausgefüllt. Orientiert euch gerne daran. Ihr müsst hier nur die Werte für die Spannung U und die Stromstärke I bestimmen. Die Leistung P wird für euch berechnet')

st.write('---')

st.write('Wenn ihr alle Werte bestimmt habt, tragt diese in die entsprechenden Kästchen unten ein. Die Werte werden automatisch übernommen und am Ende in einem Diagramm dargestellt. Gebt dazu die Werte einzeln ein und drückt einmal auf die Taste "Enter".')

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

with col1:
    st.write('')
    
with col2:
    U_1 = st.number_input(label=('Spannung "0°" in V'), min_value=0.0, max_value=2.0)
    U_2 = st.number_input(label=('Spannung "15°" in V'), min_value=0.0, max_value=2.0)
    U_3 = st.number_input(label=('Spannung "30°" in V'), min_value=0.0, max_value=2.0)
    U_4 = st.number_input(label=('Spannung "45°" in V'), min_value=0.0, max_value=2.0)
    U_5 = st.number_input(label=('Spannung "60°" in V'), min_value=0.0, max_value=2.0)
    U_6 = st.number_input(label=('Spannung "75°" in V'), min_value=0.0, max_value=2.0)
    U_7 = st.number_input(label=('Spannung "90°" in V'), min_value=0.0, max_value=2.0)
    
with col3:
    I_1 = st.number_input(label=('Stromstärke "0°" in mA'), min_value=0.0, max_value=20.0)
    I_2 = st.number_input(label=('Stromstärke "15°" in mA'), min_value=0.0, max_value=20.0)
    I_3 = st.number_input(label=('Stromstärke "30°" in mA'), min_value=0.0, max_value=20.0)
    I_4 = st.number_input(label=('Stromstärke "45°" in mA'), min_value=0.0, max_value=20.0)
    I_5 = st.number_input(label=('Stromstärke "60°" in mA'), min_value=0.0, max_value=20.0)
    I_6 = st.number_input(label=('Stromstärke "75°" in mA'), min_value=0.0, max_value=20.0)
    I_7 = st.number_input(label=('Stromstärke "90°" in mA'), min_value=0.0, max_value=20.0)
                          
with col4:
    st.write('')

U_val = [U_1, U_2, U_3, U_4, U_5, U_6, U_7]
I_val = [I_1, I_2, I_3, I_4, I_5, I_6, I_7]
 
# xxx #

if "Zeichnen (Versuch 2)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 2)"] = False

if "Erklärung (Versuch 2)" not in st.session_state:
    st.session_state["Erklärung (Versuch 2)"] = False
 
# xxx #    
    
colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    st.write('')
    if st.button(label='Zeichnen (Versuch 2)', type='primary'):
        st.session_state['Zeichnen (Versuch 2)'] = not st.session_state['Zeichnen (Versuch 2)']
    
with colC:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

winkel_1 = [0, 15, 30, 45, 60, 75, 90]
winkel_2 = [0, 15, 30, 45, 60, 75, 90]

leistung_1 = [U_1*I_1, U_2*I_2, U_3*I_3, U_4*I_4, U_5*I_5, U_6*I_6, U_7*I_7]
leistung_2 = [0.0, 7.13, 15.81, 34.07, 62.32, 106.33, 0.0]

fig = plt.figure(1)
plt.plot(winkel_1, leistung_1, label='7 m/s')
plt.plot(winkel_2, leistung_2, label='10 m/s')
plt.title('Ausgangsleistung über Drehzahl')
plt.xlabel('Drehzahl in n/min')
plt.ylabel('Ausgangsleistung in mW')
plt.legend()
plt.grid()

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

if st.session_state['Zeichnen (Versuch 2)']:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig)
    with col4:
        st.write('')

    st.write('---')
    
    st.subheader('Frage:')    
    
    st.write('Wie verhält sich die Ausgangsleistung in Abhängigkeit des Anstellwinkels? Wie ist der Kurvenverlauf und wo das Maximum?')
    
    st.write('Anhand dieser beiden Messkurven: wie ist der Zusammenhang zwischen Anstellwinkel und Windgeschwindigkeit?')
    
    st.write('Wird eine Windkraftanlage mit einem festen Anstellwinkel für alle Windgeschwindigkeiten optimal funktionieren? Wenn nein, wie kann man dieses Problem in der Realität lösen?')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 2)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 2)'):
            st.session_state['Erklärung (Versuch 2)'] = not st.session_state['Erklärung (Versuch 2)']
    with col3:
        st.write('')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 2)']:
    
    st.subheader('Erklärung')
    
    st.write('Wenn ihr das Diagramm nun erstellt habt, seht ihr, wie sich die Ausgangsleistung gegenüber dem Anstellwinkel verhält. Beide Kurven steigen bis zu ihrem Maximum an und fallen dann rapide ab. Die optimalen Winkel sind dabei bei 60° und 75° zu finden. Man sieht hier auch, dass die Ausgangsleistung für größere Windgeschwindigkeiten allgemein höher ist wie für geringere Windgeschwindigkeiten bei Verwendung des selben Winkels.')

    col1, col2 = st.columns(2)

    with col1:
        st.image('page_2_pic_3.png')
        
    with col2:
        st.image('page_2_pic_5.png')
    
    st.write('Auch sollte der Zusammenhang zwischen Anstellwinkel und Windgeschwindigkeit sichtbar sein: für höhere Windgeschwindigkeiten wird der Anstellwinkel größer. Daraus folgt auch, dass es keinen Sinn macht, eine Windkraftanlage mit einem festen Anstellwinkel zu betreiben, da die Windgeschwindigkeit über das Jahr und sogar über den tag betrachtet nie gleich ist und eine Windkraftanlage so nicht optimal arbeiten kann. In der Realität löst man das Problem, indem man eine sogenannte Rotorblattverstellung oder Pitchsystem verwendet. Diese könnt ihr im Bild unten sehen.')
    
    st.image('page_2_pic_4.png')
    
    st.write('Quelle: https://www.windkraft-journal.de/2016/09/26/moogs-neues-pitchsystem-steigert-die-zuverlaessigkeit-in-windenergieanlagen-gegenueber-herkoemmlichen-systemen-um-das-dreifache/92589')

    st.write('Dabei sieht ihr hier einen Zahnkranz an der Nabe, also dem Bauteil, an dem die drei Rotorblätter befestigt werden und insgesamt drei Motoren, die die Blätter entsprechend aurichten. Neben dieser Verstellung der Blätter kann auch die gesamte Gondel eienr Windkraftanlage gedreht und zum Wind ausgerichtet werden, was hier aber nicht weiter behandelt werden soll. Wichtig ist hier nur zu wissen, dass die Verwendung einer Rotorblattverstellung die Energieausbeute einer Anlage deutlich erhöht, da so bei fast jeder Windgeschwindigkeit die Anlage sinnvoll betrieben werden kann. ')

    st.write('---')

