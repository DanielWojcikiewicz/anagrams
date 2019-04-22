# gra polegajaca na zgadnieciu slowa z podanych liter

print('Witaj w programie anagramy. Twoim zadaniem jest odgadniecie wyrazu\
\nz podanych liter. Powodzenia!')

import random

WORDS = ('oczko', 'lokomotywa', 'metoda', 'python', 'proca', 'anagram', 'funkcja', 'kolorowanka', 'praca')

word = random.choice(WORDS)
correct = word
anagram = ''
points = 10

while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position +1):]

# poczatek gry

print('aby zakonczyc zgadywanie, nacisnij enter bez odpowiedzi')
print('jezeli potrzebujesz podpowiedzi, wpisz komende hint')
print('zgadnij jakie to slowo:', anagram)

guess = input('podaj odpowiedz: ')

while guess != correct and guess != '':
    if guess == 'hint':
        points -= 1
        x = int(input('podaj nr pozycji w wyrazie, ktora chcesz poznac: '))
        
        while x < 1 or x > len(correct):
            x = int(input('podaj istniejaca pozycje: '))
                    
        print('litera na pozycji', x, 'to', correct[x-1])
    guess = input('sprobuj jeszcze raz: ')
      

if guess == correct:
    print('brawo, odgadles slowo.')
    print('twoja ilosc punktow to:', points)
    print('dziekujemy za udzial w grze')

    
input('\n\nnacisnij enter aby zakonczyc')
