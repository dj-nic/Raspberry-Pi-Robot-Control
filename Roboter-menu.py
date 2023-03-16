# RPi GPIO Bibliothek importieren
import RPi.GPIO as GPIO
import time

# GPIO modus festlegen - in diesem Fall BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Menüdarstellung - Auflistung der Fahrtrichtungen
print(16*"#","MENÜ",16*"#")
print()
print(" vorwärts: 		fwd")
print(" rückwärts: 		bwd")
print(" linksdrehen: 		left")
print(" rechtsdrehen: 		right")
print()
print(38*"#")
print()

# Benutzereingabe - deklariert als userdirection
# Eine while-Schleife wird verwendet, um eine gültige Benutzereingabe zu erhalten.
# Die if-Anweisung überprüft, ob die Eingabe in der Liste ["fwd", "bwd", "left", "right"] enthalten ist.
# Wenn die Eingabe gültig ist, wird die Schleife mit break beendet.
while True:
    userdirection = input("Wählen Sie eine Fahrtrichtung durch \nEingabe des jeweiligen Kürzels aus: ")
    if userdirection in ["fwd", "bwd", "left", "right"]:
        break
    else:
        print("Ungültige Eingabe! Bitte wählen Sie eine der folgenden Optionen: fwd, bwd, left oder right.")


# Alogrithmus zur Auswahl der Fahrtrichtung
if userdirection == "fwd":
    GPIO.output(17, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(17, GPIO.LOW)
elif userdirection == "bwd":
    GPIO.output(27, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(27, GPIO.LOW)
elif userdirection == "left":
    GPIO.output(22, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(22, GPIO.LOW)
elif userdirection == "right":
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()
GPIO.cleanup()


# Hier steht noch nichts relevantes... aber bald bestimmt!
