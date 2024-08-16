
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

st.title("Versuch 1")

st.write('In diesem Versuch misst ihr die Ausgangsleistung und Drehzahl einer Windkraftanlage für verschiedene Anzahlen an Flügeln. Wir betrachten dabei die Anordnung mit zwei, drei und vier Flügeln, wobei ihr nur für zwei und vier Flügel Messungen durchführt und auch nur Teile davon. Wichtiger ist der daraus folgende Graph und was ihr daraus lernen könnt. Der folgende Versuch ist in zwei Teile getrennt: die Messung der Ausgangsleistung und die Messung der Drehzahl. Dazu findet ihr zweimal hintereinander jeweils einen Teil "Aufbau" und einen Teil "Aufgabe". Bearbeitet diese jeweils hintereinander und kombiniert die Ergebnisse am Ende. Die Hinweise zur Einstellung der Multimeter findet ihr jeweils im Teil "Aufgabe".')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau')

st.write('Aufbau Messung Ausgangsleistung')

st.image('page_1_pic_1.png')
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Hinweis Strommessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 2000mA" oder "Rot mA".')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Hier verwendet ihr 4 Flügel. Wählt einen Winkel von 75°. Beginnt damit eine Tabelle auf einem Blatt anzulegen, die wie folgt aussieht:')

st.write('Tabelle Messung Ausgangsleistung')

st.image('page_1_pic_2.png')

st.write('Wenn ihr das Experiment aufgebaut habt und die Multimeter eingestellt habt, könnt ihr nun mit der Messung beginnen. Beachtet dabei, die Last korrekt einzustellen! Dabei reicht für euch zu wissen, dass ein Wert in der Spalte "R" dem Wert auf dem Drehregler geteilt durch zehn entspricht. Also gehört zu einem "R" Wert von 20 die Stellung 2, zu einem "R" Wert von 60 die Stellung 6, etc. Wenn ihr wissen wollt, was es mit dem Wert für "R" auf sich hat, fragt gerne einen Betreuer. Für das Experiment hat das Verständnis keinen Einfluss.')

st.write('---')

st.write('Wenn ihr alle Werte bestimmt habt, tragt diese in die entsprechenden Kästchen unten ein. Die Werte werden automatisch übernommen und am Ende in einem Diagramm dargestellt. Gebt dazu die Werte einzeln ein und drückt einmal auf die Taste "Enter".')

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

with col1:
    st.write('')
    
with col2:
    U_1 = st.number_input(label=('Spannung "R=0" in V'), min_value=0.0, max_value=3.0)
    U_2 = st.number_input(label=('Spannung "R=20" in V'), min_value=0.0, max_value=3.0)
    U_3 = st.number_input(label=('Spannung "R=40" in V'), min_value=0.0, max_value=3.0)
    U_4 = st.number_input(label=('Spannung "R=60" in V'), min_value=0.0, max_value=3.0)
    U_5 = st.number_input(label=('Spannung "R=80" in V'), min_value=0.0, max_value=3.0)
    U_6 = st.number_input(label=('Spannung "R=100" in V'), min_value=0.0, max_value=3.0)
    
with col3:
    I_1 = st.number_input(label=('Stromstärke "R=0" in mA'), min_value=0.0, max_value=100.0)
    I_2 = st.number_input(label=('Stromstärke "R=20" in mA'), min_value=0.0, max_value=100.0)
    I_3 = st.number_input(label=('Stromstärke "R=40" in mA'), min_value=0.0, max_value=100.0)
    I_4 = st.number_input(label=('Stromstärke "R=60" in mA'), min_value=0.0, max_value=100.0)
    I_5 = st.number_input(label=('Stromstärke "R=80" in mA'), min_value=0.0, max_value=100.0)
    I_6 = st.number_input(label=('Stromstärke "R=100" in mA'), min_value=0.0, max_value=100.0)
                          
with col4:
    st.write('')

U_val = [U_1, U_2, U_3, U_4, U_5, U_6]
I_val = [I_1, I_2, I_3, I_4, I_5, I_6]
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufbau')

st.write('Aufbau Messung Ausgangsleistung')

st.image('page_1_pic_3.png')
    
st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Aufgabe')

st.write('Hinweis Spannungsmessung: schaut bitte unter "Einstellung Multimeter" nach. Wir benötigen hier entweder "Schwarz 20V" oder "Rot V".')

st.write('Baut das Experiment entsprechend der Abbildung oben nach. Hier verwendet ihr 2 Flügel. Wählt einen Winkel von 75°. Achtet darauf, dass ihr jetzt das Multimeter an den Anschlüssen, die mit "Tachogenerator" beschriftet sind, anschließt! Beginnt damit eine Tabelle auf einem Blatt anzulegen, die wie folgt aussieht:')

st.write('Tabelle Messung Drehzahl')

st.image('page_1_pic_4.png')

st.write('Wenn ihr das Experiment aufgebaut habt und die Multimeter eingestellt habt, könnt ihr nun mit der Messung beginnen. Beachtet dabei, die Last korrekt einzustellen! Dabei reicht für euch zu wissen, dass ein Wert in der Spalte "R" dem Wert auf dem Drehregler geteilt durch zehn entspricht. Also gehört zu einem "R" Wert von 20 die Stellung 2, zu einem "R" Wert von 60 die Stellung 6, etc. Wenn ihr wissen wollt, was es mit dem Wert für "R" auf sich hat, fragt gerne einen Betreuer. Für das Experiment hat das Verständnis keinen Einfluss. Misst nun die Spannung U in V für die verschiedenen "R" Werte.')

st.write('Nachdem ihr nun die Spannung U bestimmt habt nutzt die Kennlinie unten um die Werte in eine Drehzahl in n/min umzurechnen. Dabei bezeichnet "n/min" Umdrehungen pro Minute. Ihr verwendet die Kennlinie wie folgt: nehmt einen Wert der Spannung und sucht diesen auf der x-Achse. Fährt nun gedanklich oder mit der Maus nach oben bis ihr die Kurve schneidet. Von dem Schnittpunkt fährt gedanklich oder mit der Maus nach links, bis ihr einen Punkt auf der y-Achse erreicht. Dieser Wert ist der dazugehörige Wert der Drehzahl zu einem vorgegebenen Wert der Spannung U.')

st.image('page_1_pic_5.png', width=600)

st.write('---')

st.write('Wenn ihr alle Werte bestimmt habt, tragt diese in die entsprechenden Kästchen unten ein. Die Werte werden automatisch übernommen und am Ende in einem Diagramm dargestellt.')

col1, col2, col3, col4 = st.columns([0.1, 0.4, 0.4, 0.1])

with col1:
    st.write('')
    
with col2:
    n_1 = st.number_input(label=('Drehzahl "R=0" in n/min'), min_value=0, max_value=2000)
    n_2 = st.number_input(label=('Drehzahl "R=20" in n/min'), min_value=0, max_value=2000)
    n_3 = st.number_input(label=('Drehzahl "R=40" in n/min'), min_value=0, max_value=2000)
    
with col3:
    n_4 = st.number_input(label=('Drehzahl "R=60" in n/min'), min_value=0, max_value=2000)
    n_5 = st.number_input(label=('Drehzahl "R=80" in n/min'), min_value=0, max_value=2000)
    n_6 = st.number_input(label=('Drehzahl "R=100" in n/min'), min_value=0, max_value=2000)
                          
with col4:
    st.write('')

n_val = [n_1, n_2, n_3, n_4, n_5, n_6]

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Auswertung')

st.write('Wenn ihr nun die Messung für die Ausgangsleistung und die Drehzahl durchgeführt habt und alle Werte eingetragen sind, drückt unten einmal auf "Zeichnen (Versuch 1)". Ihr seht drei Tabellen: eine für zwei, drei und vier Flügel jeweils mit den Werten für "R", "U", "I", "P", "U Tacho" und "Drehzahl" und euren Messungen nun eingefügt. Darunter ist ein Diagramm erstellt worden, dass die Ausgangsleistung in mW über der Drehzahl in n/min darstellt.')

# xxx #

if "Zeichnen (Versuch 1)" not in st.session_state:
    st.session_state["Zeichnen (Versuch 1)"] = False

if "Erklärung (Versuch 1)" not in st.session_state:
    st.session_state["Erklärung (Versuch 1)"] = False
 
# xxx #    
    
colA, colB, colC = st.columns([0.45, 0.1, 0.45])

with colA:
    st.write('')
    
with colB:
    if st.button(label='Zeichnen (Versuch 1)', type='primary'):
        st.session_state['Zeichnen (Versuch 1)'] = not st.session_state['Zeichnen (Versuch 1)']
    
with colC:
    st.write('')

data_2 = [[0, 0.03, 22, 0.66, 0.25, n_1], [20, 0.4, 20, 8.0, 0.59, n_2], [40, 0.72, 18, 12.9, 0.9, n_3], [60, 1.05, 17.5, 18.4, 1.26, n_4], [80, 1.83, 22.3, 40.8, 2.07, n_5], [100, 2.14, 21.1, 45.2, 2.38, n_6]]

data_3 = [[0, 0.05, 37.9, 1.9, 0.43, 287], [20, 0.64, 33.8, 21.6, 0.99, 660], [40, 1.86, 46.8, 87.0, 2.35, 1567], [60, 2.3, 37.5, 86.3, 2.66, 1733], [80, 2.5, 30.4, 76.0, 2.83, 1887], [100, 2.62, 25.8, 67.6, 2.91, 1940]]

data_4 = [[0, U_1, I_1, U_1*I_1, 0.61, 407], [20, U_2, I_2, U_2*I_2, 2.13, 1420], [40, U_3, I_3, U_3*I_3, 2.5, 1667], [60, U_4, I_4, U_4*I_4, 2.64, 1760], [80, U_5, I_5, U_5*I_5, 2.71, 1807], [100, U_6, I_6, U_6*I_6, 2.74, 1827]]

df_2 = pd.DataFrame(data_2, columns = ['R [Ohm]', 'U [V]', 'I [mA]', 'P [mW]', 'U Tacho [V]', 'Drehzahl [n/min]'])

df_3 = pd.DataFrame(data_3, columns = ['R [Ohm]', 'U [V]', 'I [mA]', 'P [mW]', 'U Tacho [V]', 'Drehzahl [n/min]'])

df_4 = pd.DataFrame(data_4, columns = ['R [Ohm]', 'U [V]', 'I [mA]', 'P [mW]', 'U Tacho [V]', 'Drehzahl [n/min]'])

drehzahl_2 = df_2.loc[:,'Drehzahl [n/min]']

drehzahl_3 = df_3.loc[:,'Drehzahl [n/min]']

drehzahl_4 = df_4.loc[:,'Drehzahl [n/min]']

leistung_2 = df_2.loc[:,'P [mW]']

leistung_3 = df_3.loc[:,'P [mW]']

leistung_4 = df_4.loc[:,'P [mW]']

fig = plt.figure(1)
plt.plot(drehzahl_2, leistung_2, label='2 Flügel')
plt.plot(drehzahl_3, leistung_3, label='3 Flügel')
plt.plot(drehzahl_4, leistung_4, label='4 Flügel')
plt.title('Ausgangsleistung über Drehzahl')
plt.xlabel('Drehzahl in n/min')
plt.ylabel('Ausgangsleistung in mW')
plt.legend()
plt.grid()

if st.session_state['Zeichnen (Versuch 1)']:
    
    st.write('---')
    
    colA, colB, colC = st.columns([0.3, 0.4, 0.3])
    
    with colA:
        st.write('')
        
    with colB:
        st.write('Tabelle für zwei Flügel:')
        
        st.markdown(df_2.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        
        st.write('')
        
        st.write('Tabelle für drei Flügel:')
        
        st.markdown(df_3.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        
        st.write('')
        
        st.write('Tabelle für vier Flügel:')
        
        st.markdown(df_4.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        
        st.write('')
        
        st.write('Diagramm Ausgangsleistung über Drehzahl:')
        
        st.pyplot(fig)
        
    with colC:
        st.write('')
    
    st.write('---')
    
    st.subheader('Frage')
    
    st.write('Wie verhalten sich die Kurven für die Ausgangsleistung über der Drehzahl? Wo liegt das Maximum? ')
    
    st.write('Zusatzfrage: die Windkraftanlagen die ihr draußen seht haben immer drei Flügel. Wenn ihr euch euer Diagramm anschaut, solltet ihr sehen, dass eine Windkraftanlage mit vier Flügeln eine höhere Ausgangsleistung erreicht. Warum verwendet man dann nur drei Flügel?')
    
    colA, colB, colC = st.columns([0.45, 0.1, 0.45])

    with colA:
        st.write('')
        
    with colB:
        
        st.write('')
        
        if st.button(label='Erklärung (Versuch 1)'):
            st.session_state['Erklärung (Versuch 1)'] = not st.session_state['Erklärung (Versuch 1)']
        
    with colC:
        st.write('')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

if st.session_state['Erklärung (Versuch 1)']:

    st.subheader('Erklärung')
    
    st.write('Wenn ihr das Diagramm nun erstellt habt, seht ihr wie sich die Ausgangsleistung gegenüber der Drehzahl verhält. Man sieht bei allen Kurven, dass das Maximum bei höheren Drehzahlen liegt. Außerdem fällt auf, dass die Ausgangsleistung für drei Flügel deutlich größer ist wie mit zwei Flügeln. Die Ausgangsleistung für vier Flügel ist nochmal größer wie für drei Flügel.')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image('page_1_pic_6.png')
        
    with col2:
        st.image('page_1_pic_7.png')
    
    st.write('Nun noch zur Erklärung der Zusatzfrage: es gibt mehrere Gründe warum man bei realen Anlagen nur drei Flügel verwendet, unter anderem liegt dies an den Kosten und geringeren mechanischen Belastungen der Bauteile.')
    
    st.write('Der erste Punkt ist eine reine Kostenfrage: ein einzelnes Rotorblatt kostet circa 200.000€ und da die erreichte Leistung mit vier gegenüber drei Rotorblättern nur um ungefähr 16% besser wird, die Kosten durch ein viertes Rotorblatt aber um 33% steigen, verzichtet man aus wirtschaftlichen Gründen darauf. In anderen Worten: man baut die Anlagen absichtlich weniger effizient, da es sich wirtschaftlich rechnet.')
    
    st.write('Der zweite Punkt bezieht sich auf die Stellung der Rotorblätter gegenüber dem Turm: bei vier Rotorblättern gibt es immer wieder Konfigurationen, bei denen ein Rotorblatt genau vor dem Turm steht und ein Rotorblatt am höchsten Punkt, also dort, wo am meisten Wind weht und die Kraft am höchsten ist. Dies führt zu einer hohen mechanischen Belastung. Mit nur drei Rotorblättern vermeidet man diese Situation: wenn ein Rotorblatt vor dem Turm steht sind die anderen weiter oben aber werden nicht maximal angetrieben und wenn ein Rotorblatt ganz oben steht, werden die beiden anderen weiter unten immer noch vom Wind erreicht. Dies ührt allgemein zu geringeren Belastungen, also leichteren Bauteilen und weniger Verschleiß und Wartungsaufwand.')

    st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

