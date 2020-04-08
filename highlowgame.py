#High-Low party game by Adrian Bobrowski
#myfirstproject

import random
import snaps
import time


snaps.display_message('Zacznę losować kolejno liczby z zakresu od 1 do 10.',size=30)
time.sleep(5)
snaps.display_message('Waszym zadaniem jest odgadnąć czy następna liczba będzie większa czy mniejsza od poprzedniej',size=30)
time.sleep(5)
snaps.display_message('Na podjęcie decyzji macie 20 sekund, podzielcie się na dwie grupy!',size=30)
time.sleep(5)
snaps.display_message('Osoby obstawiające większą liczbę ustawią się po prawej, a mniejszą po lewej',size=30)
time.sleep(5)
snaps.display_message('Po prawidłowej odpowiedzi przechodzisz dalej, po nieprawidłowej odpadasz z gry, aż do wyłonienia zwycięzcy!',size=30)
time.sleep(5)
snaps.display_message('Jesteście gotowi? Zaczynamy! Pierwsza liczba to: 5',size=30)
time.sleep(20)
trafiona=False
while trafiona != 'Wygrałem' and trafiona != 'wygrałem':
    snaps.display_message(random.randint(1,10))
    time.sleep(10)
    snaps.display_message('Pozostało 10 sekund',size=30)
    time.sleep(10)
    snaps.display_message(random.randint(1,10))
    time.sleep(10)
    snaps.display_message('Uwaga, mam już kolejną',size=30)
    time.sleep(10)
    snaps.display_message(random.randint(1,10))
    time.sleep(10)
    snaps.display_message('Jesteście gotowi?',size=30)
    time.sleep(10)
    snaps.display_message(random.randint(1,10))
    time.sleep(10)
    snaps.display_message('Jeżeli macie zwycięzce, wpisz "Wygrałem" w przeciwnym wypadku, wpisz "Losuj"',size=30)
    time.sleep(5)
    trafiona=input('Gramy dalej? : ')

if trafiona=='Wygrałem' or 'wygrałem':
        snaps.display_message('GRATULACJE! May the force be with You!',size=30)
