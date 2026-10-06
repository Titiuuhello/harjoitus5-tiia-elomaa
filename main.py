# Tiia Elomaa
# 04.10.2026
# FoCar 

from machine import Pin, PWM
from time import sleep

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)


# Määritetään FoCar:lle funktiot

def eteenpain(nopeus, aika):
    # Aja eteenpäin
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def vasen(nopeus, aika):
    # Käänny vasemmalle, tätä voidaan käyttää myös 180° käännöksessä
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def oikea(nopeus, aika):
    # Käänny oikealle, tätä voidaan käyttää myös 180° käännöksessä
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def taaksepain(nopeus, aika):
    # Aja taaksepäin
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

# Suoritetaan tehtäväannossa pyydetyt toiminnot

# Odotetaan 5 sekuntia ennen lähtöä
sleep(5)

# yritä avata data.txt
try:
    with open("data.txt", "r") as file:

        for rivi in file:
            komento = rivi.strip()

            if komento == "eteenpain":
                eteenpain(35000, 2.5)

            elif komento == "taaksepain":
                taaksepain(35000, 2.5)

            elif komento == "oikea":
                oikea(40000, 1.7)

            elif komento == "vasen":
                vasen(40000, 1.7)


except FileNotFoundError:
    print("Tiedostoa ei löytynyt, kokeile uudestaan.")