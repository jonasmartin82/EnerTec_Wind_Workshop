
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

st.title("Versuch 3")

st.write('In diesem Versuch bestimmen wir die Ausgangsleistung in Abhängigkeit der Windgeschwindigkeit. Dabei betrachten wir eine Konfiguration mit drei geraden Flügeln und einem Winkel von 45° und nutzen die Skaleneinteilung der Windmaschine um eine Messreihe zu erstellen.')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau')

st.image('page_3_pic_1.png')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Achtet auf die richtige Konfiguration damit ihr die Ergebnisse vergleichen könnt! Beginnt damit eine Tabelle auf einem Blatt anzulegen, die wie folgt aussieht: ')

st.image('page_3_pic_2.png')

st.write('Ihr müsst hier die Werte für die Windgeschwindigkeit, für die Spannung U und die Stromstärke I bestimmen. Die Leistung P wird für euch berechnet.')

st.write('---')

st.write('Wenn ihr alle Werte bestimmt habt, tragt diese in die entsprechenden Kästchen unten ein. Die Werte werden automatisch übernommen und am Ende in einem Diagramm dargestellt. Gebt dazu die Werte einzeln ein und drückt einmal auf die Taste "Enter".')

col1, col2, col3, col4, col5 = st.columns([0.05, 0.3, 0.3, 0.3, 0.05])

with col1:
    st.write('')

with col2:
    v_1 = st.number_input(label='Windgeschwindigkeit "0" in m/s', min_value=0.0, max_value=15.0)
    v_2 = st.number_input(label='Windgeschwindigkeit "1" in m/s', min_value=0.0, max_value=15.0) 
    v_3 = st.number_input(label='Windgeschwindigkeit "2" in m/s', min_value=0.0, max_value=15.0) 
    v_4 = st.number_input(label='Windgeschwindigkeit "3" in m/s', min_value=0.0, max_value=15.0) 
    v_5 = st.number_input(label='Windgeschwindigkeit "4" in m/s', min_value=0.0, max_value=15.0) 
    v_6 = st.number_input(label='Windgeschwindigkeit "5" in m/s', min_value=0.0, max_value=15.0) 
    v_7 = st.number_input(label='Windgeschwindigkeit "6" in m/s', min_value=0.0, max_value=15.0) 
    v_8 = st.number_input(label='Windgeschwindigkeit "7" in m/s', min_value=0.0, max_value=15.0) 
    v_9 = st.number_input(label='Windgeschwindigkeit "8" in m/s', min_value=0.0, max_value=15.0) 
    v_10 = st.number_input(label='Windgeschwindigkeit "9" in m/s', min_value=0.0, max_value=15.0) 
    v_11 = st.number_input(label='Windgeschwindigkeit "10" in m/s', min_value=0.0, max_value=15.0) 

with col3:
    U_1 = st.number_input(label=('Spannung "0" in V'), min_value=0.0, max_value=2.0)
    U_2 = st.number_input(label=('Spannung "1" in V'), min_value=0.0, max_value=2.0)
    U_3 = st.number_input(label=('Spannung "2" in V'), min_value=0.0, max_value=2.0)
    U_4 = st.number_input(label=('Spannung "3" in V'), min_value=0.0, max_value=2.0)
    U_5 = st.number_input(label=('Spannung "4" in V'), min_value=0.0, max_value=2.0)
    U_6 = st.number_input(label=('Spannung "5" in V'), min_value=0.0, max_value=2.0)
    U_7 = st.number_input(label=('Spannung "6" in V'), min_value=0.0, max_value=2.0)
    U_8 = st.number_input(label=('Spannung "7" in V'), min_value=0.0, max_value=2.0)
    U_9 = st.number_input(label=('Spannung "8" in V'), min_value=0.0, max_value=2.0)
    U_10 = st.number_input(label=('Spannung "9" in V'), min_value=0.0, max_value=2.0)
    U_11 = st.number_input(label=('Spannung "10" in V'), min_value=0.0, max_value=2.0)
    
with col4:
    I_1 = st.number_input(label=('Stromstärke "0" in mA'), min_value=0.0, max_value=40.0)
    I_2 = st.number_input(label=('Stromstärke "1" in mA'), min_value=0.0, max_value=40.0)
    I_3 = st.number_input(label=('Stromstärke "2" in mA'), min_value=0.0, max_value=40.0)
    I_4 = st.number_input(label=('Stromstärke "3" in mA'), min_value=0.0, max_value=40.0)
    I_5 = st.number_input(label=('Stromstärke "4" in mA'), min_value=0.0, max_value=40.0)
    I_6 = st.number_input(label=('Stromstärke "5" in mA'), min_value=0.0, max_value=40.0)
    I_7 = st.number_input(label=('Stromstärke "6" in mA'), min_value=0.0, max_value=40.0)
    I_8 = st.number_input(label=('Stromstärke "7" in mA'), min_value=0.0, max_value=40.0)
    I_9 = st.number_input(label=('Stromstärke "8" in mA'), min_value=0.0, max_value=40.0)
    I_10 = st.number_input(label=('Stromstärke "9" in mA'), min_value=0.0, max_value=40.0)
    I_11 = st.number_input(label=('Stromstärke "10" in mA'), min_value=0.0, max_value=40.0)
                          
with col5:
    st.write('')

# xxx #

if "Zeichnen (Versuch 3)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 3)"] = False

if "Erklärung (Versuch 3)" not in st.session_state:
    st.session_state["Erklärung (Versuch 3)"] = False
 
# xxx #    
    
colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    st.write('')
    if st.button(label='Zeichnen (Versuch 3)', type='primary'):
        st.session_state['Zeichnen (Versuch 3)'] = not st.session_state['Zeichnen (Versuch 3)']
    
with colC:
    st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

windgeschwindigkeit = [v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11]

leistung = [U_1*I_1, U_2*I_2, U_3*I_3, U_4*I_4, U_5*I_5, U_6*I_6, U_7*I_7, U_8*I_8, U_9*I_9, U_10*I_10, U_11*I_11]

fig = plt.figure(1)
plt.plot(windgeschwindigkeit, leistung)
plt.title('Ausgangsleistung über Windgeschwindigkeit')
plt.xlabel('Windgeschwindigkeit in m/s')
plt.ylabel('Ausgangsleistung in mW')
plt.grid()

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

if st.session_state['Zeichnen (Versuch 3)']:
    with col1:
        st.write('')
    with col2:
        st.pyplot(fig)
    with col4:
        st.write('')

    st.write('---')
    
    st.subheader('Frage:')    
    
    st.write('Wie verhält sich die Ausgangsleistung in Abhängigkeit der Windgeschwindigkeit? Wie ist der Kurvenverlauf?')
    
    st.write('Anhand der Messkurve: wie ist der Zusammenhang zwischen Ausgangsleistung und Windgeschwindigkeit? Könnt ihr eine Ausage über Proportionalität und deren Verhältnis treffen?')
    
    st.write('Nachdem ihr die Kurven nun bestimmt habt: wo sollte man die Anlagen am besten platzieren? (Hinweis: schaut euch dazu unter "Erklärung Windenergie" die Windkarte für Deutschland und/oder Europa an und überlegt, wo man die Anlagen entsprechend aufbauen sollte)')

col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

if st.session_state['Zeichnen (Versuch 3)']:
    with col1:
        st.write('')
    with col2:
        st.write('')
        if st.button(label='Erklärung (Versuch 3)'):
            st.session_state['Erklärung (Versuch 3)'] = not st.session_state['Erklärung (Versuch 3)']
    with col3:
        st.write('')
    
    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 3)']:
    
    st.subheader('Erklärung')
    
    st.write('Wenn ihr das Diagramm nun erstellt habt, seht ihr, wie sich die Ausgangsleistung gegenüber der Windgeschwindigkeit verhält. Die Kurve steigt erst langsam und dann immer steiler an. Die Kurve beginnt erst ab circa vier bis fünf m/s zu steigen. Das bedeutet auch, ähnlich wie bei realen Anlagen, dass eine Windkraftanlage erst aber einer bestimmten Windgeschwindigkeit sinnvoll Energie produzieren kann. Demgegenüber steigt die erzeugte Leistung sehr schnell an, wenn dieses Minimum überschritten wurde.')

    col1, col2 = st.columns(2)

    with col1:
        st.image('page_3_pic_3.png')
        
    with col2:
        st.image('page_3_pic_4.png')
    
    st.write('Wenn man sich die Kurve betrachtet kann man auch einen Zusammenhang zwischen Windgeschwindigkeit und Ausgangsleistung bestimmen. Die Kurve ist nicht linear, scheint aber mit einer bestimmten Potenz zu steigen. Man kann sich den Zusammenhang schön herleiten, wenn man sich die Werte für 5 m/s und 10 m/s betrachtet: bei 5 m/s  erreicht die Anlage circa 5 mW und für 10 m/s erreicht die Anlage schon 40 mW. Das heißt, wenn sich die Windgeschwindigkeit verdoppelt, verachtfacht sich die Ausgangsleistung. Dies bedeutet, dass die Ausgangsleistung mit der dritten Potenz der Windgeschwindigkeit wächst (als Erinnerung für den Zusammenhang: 2^3 ergibt 8, dass heißt P = v^3. In diesem Fall entspricht v der Windgeschwindigkeit und P der Ausgangsleistung).')
    
    st.write('Damit sollte sich auch die Frage nach der Platzierung der WIndkraftanlagen beantworten: wenn ihr die Windkarte unter "Erklräung Windenergie" betrachtet, seht ihr, dass sich die Platzierung von windkraftanlagen in Deutschland vor allem an der Küste lohnt. Je weiter ihr nach Süden bzw. Süd-Osten geht, desto geringer wird die durchschnittliche Windgeschwindigkeit. Dass Saarland selbst liegt dabei mit 4-5 m/s am unteren Ende dessen, was für die Erzeugung von Windenergie möglich ist. Abgesehen davon, dass die durchschnittliche Windgeschwindigkeit geringer ist, sind auch die Beständigkeit oder Häufigkeit des Windes geringer sowie weniger Tage mit höheren Windstärken, da wir weit weg von der Küste liegen. Umgekehrt lohnt sich bei uns im Saarland die Solarenergie mehr wie an der Küste, was ihr im Workshop Solarenergie lernen könnt.')
    
    st.write('---')