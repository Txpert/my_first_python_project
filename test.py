import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Liniendiagramm erstellen
plt.plot(x, y, label='Lineare Funktion')

# Diagramm beschriften
plt.xlabel('x - Achse')
plt.ylabel('y - Achse')
plt.title('Einfaches Liniendiagramm')

# Legende hinzufügen
plt.legend()

# Diagramm anzeigen
plt.show()
