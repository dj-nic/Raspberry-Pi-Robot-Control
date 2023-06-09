# Please give credit if you use my Code <3


# RPi GPIO Bibliothek importieren
import RPi.GPIO as GPIO
import time

dc = 0  # duty cycle (0-100) für PWM

Echo = 23  # Für den Ultraschallsensor
Trig = 24

LED = 18  # Rote LED

MotorLF = 26  # Links Rückwärts
MotorRF = 20  # Rechts Rückwärts

MotorLB = 19  # Links Vorwärts
MotorRB = 21  # Rechts Vorwärts

# Sensor einheiten definieren
speed_of_sound = 34300 # in cm/s

# def für den Ultraschallsensor
def get_distance():
    # 10 Impulse zum triggern senden
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)

    # Auf das Echo warten
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(Echo) == 0:
        start_time = time.time()

    while GPIO.input(Echo) == 1:
        stop_time = time.time()

    # Die distanz in cm ausrechnen
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * speed_of_sound) / 2
    return distance

# def für die Motoren
def motorvorwaerts():
    pwmMotorLB.start(50)
    pwmMotorRB.start(50)
    pwmMotorRB.ChangeDutyCycle(100)
    pwmMotorLB.ChangeDutyCycle(100)

def motorlinks():
    pwmMotorLB.start(50)
    pwmMotorRB.start(50)
    pwmMotorRB.ChangeDutyCycle(0)
    pwmMotorLB.ChangeDutyCycle(100)

def motorrechts():
    pwmMotorLB.start(50)
    pwmMotorRB.start(50)
    pwmMotorRB.ChangeDutyCycle(100)
    pwmMotorLB.ChangeDutyCycle(0)

def motorrueckwerts():
    pwmMotorLF.start(50)
    pwmMotorRF.start(50)
    pwmMotorRF.ChangeDutyCycle(100)
    pwmMotorLF.ChangeDutyCycle(100)

def motorstop():
    pwmMotorLF.stop()
    pwmMotorRF.stop()
    pwmMotorLB.stop()
    pwmMotorRB.stop()

# GPIO-Modus festlegen - in diesem Fall BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)  # LED Pin
GPIO.setup(MotorRF, GPIO.OUT)  # Motor Pin
GPIO.setup(MotorRB, GPIO.OUT)  # Motor Pin
GPIO.setup(MotorLF, GPIO.OUT)  # Motor Pin
GPIO.setup(MotorLB, GPIO.OUT)  # Motor Pin

pwmMotorRB = GPIO.PWM(MotorRB, 50)  # Motor mit 50Hz ansteuern
pwmMotorRF = GPIO.PWM(MotorRF, 50)
pwmMotorLB = GPIO.PWM(MotorLB, 50)
pwmMotorLF = GPIO.PWM(MotorLF, 50)

# Menüdarstellung - Auflistung der Fahrmodi
print(10 * "#", "MENÜ", 10 * "#")
print()
print(" Autonom: \tauto")
print(" Manuell: \tmanu")
print()
print(26 * "#")
print()

while True:
    userdirection = input("Wählen Sie eine Fahrmodi durch \nEingabe des jeweiligen Kürzels aus: ")
    if userdirection in ["auto", "manu"]:
        break
    else:
        print("Ungültige Eingabe! Bitte wählen Sie eine der folgenden Optionen: auto, manu.")

# Menüdarstellung - Auflistung der Fahrtrichtungen
print(16 * "#", "MENÜ", 16 * "#")
print()
print(" vorwärts: \t\tfwd")
print(" rückwärts: \tbwd")
print(" linksdrehen: \tleft")
print(" rechtsdrehen: \tright")
print(" stop: \t\t\tstop")
print()
print(38 * "#")
print()

# Benutzereingabe - deklariert als userdirection
# Eine while-Schleife wird verwendet, um eine gültige Benutzereingabe zu erhalten.
# Die if-Anweisung überprüft, ob die Eingabe in der Liste ["fwd", "bwd", "left", "right"] enthalten ist.
# Wenn die Eingabe gültig ist, wird die Schleife mit break beendet.
while True:
    userdirection = input("Wählen Sie eine Fahrtrichtung durch \nEingabe des jeweiligen Kürzels aus: ")
    if userdirection in ["fwd", "bwd", "left", "right", "stop"]:
        break
    else:
        print("Ungültige Eingabe! Bitte wählen Sie eine der folgenden Optionen: fwd, bwd, left oder right.")

# Algorithmus zur Auswahl der Fahrtrichtung -- Muss noch überarbeitet werden
if userdirection == "fwd":
  motorvorwaerts()
  time.sleep(5)
elif userdirection == "bwd":
  motorrueckwerts()
  time.sleep(5)
elif userdirection == "left":
    motorlinks()
    time.sleep(5)
elif userdirection == "right":
    motorrechts()
    time.sleep(5)

try:
    while True:
        distance = get_distance()
        print("Distance: %.2f cm" % distance)

        if distance < 30:
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

pwmMotorLB.stop()  # PWM beenden
pwmMotorLF.stop()
pwmMotorRB.stop()
pwmMotorRF.stop()
GPIO.cleanup()  # GPIO Pins freigeben
