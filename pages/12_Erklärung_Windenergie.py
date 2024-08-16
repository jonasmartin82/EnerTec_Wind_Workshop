
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

st.title('Erklärung Windenergie')

st.write('Auf dieser Seite soll die Windenergie erklärt werden. Dabei beschäftigen wir uns mit der Quelle der Energie, ihrer Verbreitung und deren Nutzung.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Quelle')

st.image('page_12_pic_1.png', width=600)

st.write('Quelle: https://blog.otthydromet.com/de/wind-gust-messung-mit-lufft-ventus-und-v200a/')

st.write('Wind kennt ihr aus eurem Alltag sicherlich. Sei es die leichte Sommerbrise oder wie im Bild oben ein Sturm mit starken Winden. Dabei gibt man die Windgeschwindigkeit an um die Stärke des Winds zu messen. Denn mehr ist Wind auch nicht, als bewegte Luftmassen. Typische Einheiten sind km/h (Kilometer pro Stunde) oder m/s (Meter pro Sekunde).')

st.write('Die eigentliche Quelle für Wind ist dabei auch die Sonne: die Strahlung der Sonne erwärmt die Luftmassen und setzt diese damit in Beweung. Wind ist dann schließlich die Bewegung von Luft zwischen Gebieten mit verschiedenem Druck. Der Luftdruck bedeutet in dem Fall, wie viele Teilchen Luft pro Volumen vorhanden sind. In einem Hochdruckgebiet ist damit also mehr Luft in dem selben Gebiet im Vergleich zu einem Tiefdruckgebiet. Aus dem Wetterbericht kennt ihr diese Begriffe sicherlich, häufig mit einem "H" für ein Hochdruckgebiet und einem "T" für ein Tiefdruckgebiet gekennzeichnet.')

st.image('page_12_pic_2.png')

st.write('Quelle: https://o.quizlet.com/3P46TpaCM-.sb4LfQT4zrw.png')

st.write('Das Bild oben beschreibt einen typischen Aufbau von Windsystemen. Aufgrund der unterschiedlichen Einstrahlung auf der Erde erwärmt sich die Luft am Äquator zum Beispiel stärker wie an den Polen. Nehmen wir als Beispiel das Windsystem am Äquator an: durch die starke Sonneneinstrahlung erwärmt sich die Luft mehr und steigt auf. Diesen Effekt könnt ihr zum Beispiel bei einem Heißluftballon beobachten: wenn Luft wärmer wird, wird sie "leichter" und steigt deswegen auf. Das gleiche passiert hier auch. Da mehr und mehr Luft aufsteigt (Mitte des Bilds) fehlt diese am Boden, ein Tiefdruckgebiet entsteht. Die Luft die aufsteigt, bewirkt in der Höhe ein Hochdruckgebiet. Die Luftmassen verteilen sich dabei zu den Seiten, in dem Beispiel nach Norden und Süden, da nach Osten und Westn hin genauso ein Hochdruckgebiet vorherrscht. Auch am Boden bewegen sich Luftmassen: diese strömen von Norden und Süden zum Äquator um den niedrigen Druck auszugleichen. Dadurch entsteht wie ihr seht eine Zirkulation, also zwei Kreise. Dieses Verhalten findet man nicht nur am Äquator sondern mehrfach auf unserer Erde. Das Bild unten zeigt wie sich die Windsysteme ausbilden. Mit dem Prinzip von oben lässt sich das Bild unten gut erklären.')

st.image('page_12_pic_3.png', width=800)

st.write('Quelle: https://de.wikipedia.org/wiki/Passat_%28Windsystem%29#/media/Datei:Earth_Global_Circulation_-_de.svg')

st.write('Mit der Erklärung von oben lässt sich das Bild verstehen: über dem Äquator erwärmen sich die Luftmassen, steigen auf und strömen nach Norden und Süden. Über dem Nord- und Südpol hingegen kühlen die Luftmassen aus und sinken ab, es bildet sich ein Hochdruckgebiet am Boden. Diese Luftmassen streben zum Äquator. Da sich die Luftmassen, die vom Äquator weg streben, mit der Zeit abkühlen, sinken diese um den 30igsten Breitengrad ab und bilden dort Hochdruckgebiete aus. Dies formt die Zellen bzw. Zirkulationen am Äquator. Die Luft die von den Polen weg strömt erwärmt sich mit der Zeit und beginnt um den 60igsten Breitengrad herum wieder aufzusteigen. Dies formt die Zelle an den Polen. Da zwischen dem 30igsten und 60igsten Breitengrad eine Lücke ist, wird die dort befindliche Luft von der Zelle am Äquator und den Polen beeinflusst: am 60igsten Breitengrad steigen Luftmassen auf, am 30igsten Breitengrad ab, dass heißt das Teile der Luft von Süden nach Norden fließen (auf der Nordhlabkugel, auf der Südhalbkugel umgekehrt). Der letzte Aspekt ist die Ablenkung der Winde nach Osten oder Westen aufgrund der Coreoliskraft, was ihr auch in der Abbildung sehen könnt. Dies entsteht durch die Drehung der Erde, führt aber hier zu weit. Wenn euch das interessiert sucht im Internet nach weiterführenden Informationen. ')

st.write('Mit einem Blick auf die Abbildung solltet ihr sehen, dass die Winde in unserer Region in Europa meistens von Westen nach Osten wehen, deswegen auch Westwinde genannt. Da die Windsysteme aber nie konstant sind, verschieben sie sich immer ein wenig und deswegen weht der Wind auch mal aus einer anderen Richtung. Dies folgt auch aus den kleineren Hoch- und Tiefdruckgebieten die ihr in der Abildung unten seht.')

st.image('page_12_pic_4.png')

st.write('Quelle: https://uebermedien.de/35732/die-ard-gibt-dem-hessischen-rundfunk-das-wetter-zurueck/')

st.write('Das Bild oben zeigt einen Ausschnitt aus einem Wetterbericht wie ihr ihn aus dem Fernsehen kennt. Wie die die kleinen Hoch- und Tiefdruckgebiete entstehen ist dabei nicht so wichtig. Ihr solltet aber verstehen, dass diese kleineren Druckgebiete die Windrichtung beeinflussen können. Erinnert euch daran wie sich Luftmassen bewegen: immer vom höheren Druck zum niedrigeren Druck. Das heißt, in diesem Fall weht der Wind über England nach Nordwesten (das würde Südost Wind genannt werden, also immer die Richtung, aus der die Luft kommt). Da das Hochdruckgebiet über Deutschland verharrt, wird es keine größeren Winde geben. Was ihr euch auch noch merken könnt: ein Hochdruckgebiet bringt in aller Regel gutes Wetter, höhere Temperaturen, Sonnenschein und kaum Wolken. Umgekehrt bedeutet ein Tiefdruckgebiet häufig kältere Temperaturen, mehr Wind, Wolken und Regen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Verbreitung')

st.write('Hier möchten wir uns mit der Verbreitung von Wind bzw. dessen Windgeschwindigkeit befassen. Wie ihr in einem der Experimente noch sehen werdet, spielt die Windgeschwindigkeit eine große Rolle bei der Effizienz  und dem Ertrag einer Windkraftanlage. Dazu schauen wir uns einmal zwei Karten an, eine für Deutschland und eine für Europa und erklären daran ein paar Effekte.')

st.image('page_12_pic_5.png')

st.write('Quelle: https://pbs.twimg.com/media/Fp-kLehWcAELFbL.jpg')

st.write('Die Karte oben zeigt die Verteilung der Windgeschwindigkeiten über Deutschland. Zu beachten ist hier, dass die Geschwindigkeit in einer Höhe von 120 Metern über Grund gemessen wurde und nicht am Boden. Zu sehen ist klar die Verteilung von Norden nach Süden hin, wobei die Werte im Norden am höchsten sind. Grund dafür ist die Nähe zum Meer und das flache Gebiet. Da Land und Wasser in der Regel unterschiedliche Temperaturen haben, kommt es zu verschiedenen lokalen Druckgebieten und damit zu Winden. Außerdem hilft das flache Gebiet: neben Bauwerken stören auch Wälder und Gebirge den Wind und können lokal die Windstärke verstärken oder meistens eher reduzieren. Deswegen ist die Windgeschwindigkeit im Süden von Deutschland generell geringer.')

st.image('page_12_pic_6.png', width=800)

st.write('Quelle: https://uol.de/fileadmin/_processed/c/f/csm_wind_langjahriges_mittel_075a181779.png')

st.write('Ein weiteres Beispiel ist hier die Karte von Europa. Hier kann man auch einige Effekte beobachten: man beachte die hohe Windgeschwindigkeit über dem Atlantik oder der eher geringen Windgeschwindigkeit in Norditalien. Über dem Meer gibt es keine störenden Objekte und durch die Alpen wird Norditalien von einem Großteil der Winde abgeschirmt. So kann man sich viele Aspekte der Karte erklären. Fallen euch weitere Besonderheiten auf? Wie kann man sich diese erklären?')

st.write('---')
   
# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Nutzung')

st.write('Nun soll es um die Nutzung der Windenergie gehen. Dazu betrachten wir uns nur die modernen Typen von Anlagen. Auch in der Vergangenheit gibt es Anwendungen die ihr kennt: ein Segelschiff wird durch die Kraft des Windes angetrieben, genau wie eine Getreidemühle den Wind nutzt um Mehl herzustellen. Moderne Anwendungen nutzen die Energie des Windes dagegen rein zur Erzeugung von elektrischen Strom. Unten seht ihr im folgenden drei Bilder: eine kommerzielle Anlage mit horizontalem Läufer und zwei Anlagen mit vertikalem Läufer (erst Savonius Rotor, danach Darrieus Rotor).')

st.image('page_12_pic_7.png')

st.write('Quelle: https://www.deutschlandfunk.de/windkraftanlagen-mit-dem-wartungsfahrstuhl-ganz-nach-oben-100.html')

st.image('page_12_pic_8.png')

st.write('Quelle: https://www.klein-windkraftanlagen.com/technik/vertikale-windkraftanlagen/')

st.image('page_12_pic_9.png')

st.write('Quelle: https://www.klein-windkraftanlagen.com/technik/vertikale-windkraftanlagen/')

st.write('Die drei oben genannten Typen lassen sich in zwei Kriterien unterscheiden: Vertikalläufer und Horizontalläufer sowie in Widerstandsläufer und Auftriebsläufer. Die erste Unterscheidung betrifft die Lage der Rotationsachse, die im ersten Bild horizontal liegt und in den Bildern zwei und drei vertikal liegt. Grundsätzlich hat keine der beiden Varianten einen Vorteil. Der Grund warum ihr im Alltag nur Horizontalläufer seht, ist der höhere Wirkungsgrad und die bessere Skalierbarkeit, dass heißt man kann einfacher größere Anlagen bauen. Vertikalläufer haben prinzipbedingt einen schlechteren Wirkungsgrad. Auf der anderen Seite sind Vertikalläufer unabhängig von der Windrichtung und können auf kleinem Raum betrieben werden. Deswegen sieht man diese gelegentlich auf Dächern von Häusern oder anderen exponierten Punkten, um die Wirkung des Windes zu nutzen.')

st.write('Das zweite Kriterium zur Unterscheidung ist das Funktionsprinzip: Widerstandsläufer oder Auftriebsläufer. Dabei funktionieren beide Typen ganz anders. Das Bild unten links beschreibt einen Widerstandsläufer. Wie der Name sagt, stellt die Fläche A einen Widerstand für den Wind dar. Die Luft wird vor der Fläche gestaut und erzeugt einen Druck, der die Fläche in Bewegung setzt. Der Auftriebsläufer im Bild unten rechts funktioniert anders: durch die unterschiedliche Krümmung der Ober- und Unterseite des Flügels strömt die Luft unterschiedlich schnell. Auf der Unterseite strömt sie langsamer, die Luft staut sich und es entsteht ein Überdruck der den Flügel nach oben drücken will. Auf der Oberseite strömt die Luft schneller, es kommt zu einer Verringerung der Dichte und damit zu einem Unterdruck, der den Flügel nach oben saugt. Dadurch entsteht eine Kraft nach oben. Dieses Prinzip kennt ihr auch von Vögeln oder einem Flugzeug. Dabei verwendete der Horizontalläufer im ersten Bild das Auftriebsprinzip genau wie der Darrieus Rotor im dritten Bild, wohingegen der Savonius Rotor mim zweiten Bild das Widerstandsprinzip verwendet.')

col1, col2 = st.columns(2)

with col1:
    st.image('page_12_pic_10.png', width=600)
    st.write('Quelle: https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/widerstandlaeufer-auftriebslaeufer/')
    
with col2:
    st.image('page_12_pic_11.png')
    st.write('Quelle: https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/widerstandlaeufer-auftriebslaeufer/')

st.write('Das Bild unten zeigt eine Windkraftanlage als Horizontalläufer mit den typischen Bauteilen. Die Anlage steht auf einem Fundament aus Beton welches im Boden versteckt ist. Darauf steht der Turm oder Mast der die Gondel trägt. In der Gondel selbst sind als größte Bauteile das Getriebe und der Generator untergebracht. Das Getriebe dient zur Anpassung der Drehzahl und dem Drehmoment wobei der Generator die mechanische Energie in elektrische Energie umwandelt. Um die Anlage bei hohen Windstärken vor Beschädigung zu schützen verfügt die Anlage über eine Bremse. Die Rotorblätter sind an der Nabe befestigt, welche über eine Welle mit dem Getriebe verbunden ist. Wie in der Zeichnung dargestellt lassen sich die Rotorblätter verstellen (also den Anstellwinkel anpassen) sowie die Gondel drehen, um sie entsprechend der Windrichtung auszurichten.')

st.image('page_12_pic_14.png')

st.write('Quelle: https://www.lehrerfreund.de/technik/1s/stromerzeugung-mit-windenergieanlagen1/4042')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Anteil am Strommix')

st.write('Im folgenden beschäftigen wir uns mit dem Anteil der Windenergie an der Stromerzeugung beziehungsweise dem Anteil des Stroms an der Gesamtenergie.')

st.image('page_12_pic_12.png', width=800)

st.write('Quelle: https://www.unendlich-viel-energie.de/mediathek/grafiken/der-strommix-in-deutschland-im-jahr-2023')

st.write('Die Abbildung oben zeigt den Strommix in Deutschland im Jahr 2023. Man sieht, dass die erneuerbaren Energien einen Anteil von 52% an der gesamten Stromerzeugung haben. Die Windenergie nimmt mit 26,8% an der Gesamtstromerzeugung den größten Anteil ein. Auch wenn diese Zahlen vielversprechend aussehen, ist noch ein großer Bedarf vorhanden erneuerbare Energien weiter auszubauen damit unser Strom irgendwann zu 100% aus erneuerbaren Energiequellen gewonnen werden kann.')

st.image('page_12_pic_13.png', width=800)

st.write('Quelle: https://www.umweltbundesamt.de/daten/energie/primaerenergieverbrauch#definition-und-einflussfaktoren')

st.write('Ein weiterer Aspekt ist der Primärenergieverbrauch, der neben dem Stromverbrauch auch sämtliche anderen Formen der Energie beinhaltet wie zum Beispiel Benzin oder Diesel für Autos und LKW oder Gas für euere Heizung. Betrachtet man hier den Gesamtanteil der erneuerbaren Energien am Primärenergieverbrauch sieht man, dass der Anteil wesentlich geringer ist und nur 19,6% in 2023 betrug. Ohne weiter auf diese Thematik eingehen zu wollen, sollte erwähnt werden, dass auch nach und nach andere Bereiche elektrifiziert werden, also vorhandene Technologien durch Strom ersetzt werden. So geschieht dies bereits durch E-Autos im Verkehrsbereich oder durch Wärmepumpen im Bereich der Heizung. Diese Faktoren bedeuten, dass wir nicht nur 100% des jetzigen Stromverbrauches durch erneuerbare Energien decken müssen, sondern langfristig einen Großteil, wenn nicht sogar den ganzen Primärenergieverbrauch. Man sieht also, dass uns noch eine Menge Arbeit bevorsteht, um unsere Gesellschaft langfristig auf erneuerbare Energien umzustellen.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

