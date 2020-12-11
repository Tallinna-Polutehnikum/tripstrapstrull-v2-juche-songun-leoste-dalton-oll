# Trips-traps-trull
#
# Oll, Leoste, Dalton


import time, random
from os import system, name 

arvuti = False

esimesevoidud = teisevoidud = 0

esimene = teine = mangulaud = ''

mangulist = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
    #end 
#end

def scoreboard():
    global esimesevoidud, teisevoidud

    print('\n\nEsimese mängija võidud:', esimesevoidud)
    print('Teise mängija võidud:', teisevoidud)
#end

def uuesti():
    global mangulist

    while True:
        try:
            valik = str(input('\n\nKas te soovite uuesti mängida? (Jah/Ei) : '))
        except:
            sobilik()
            continue
        else:
            if valik == 'J' or valik == 'j' or valik == 'JAH' or valik == 'Jah' or valik == 'jah':
                clear()
                mangulist = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
                alusta()
                break
            elif valik == 'E' or valik == 'e' or valik == 'EI' or valik == 'Ei' or valik == 'ei':
                print('\n\n\nLõpetan mängu, nägemist! :)')
                time.sleep(5)
                break
            else:
                sobilik()
                continue
            #end
        #end
    #end
#end

def esimenevoitis(lauasuurus):
    global esimesevoidud

    time.sleep(1)
    clear()

    if lauasuurus == '3x3':
        laud('3x3')
    elif lauasuurus == '4x4':
        laud('4x4')
    elif lauasuurus == '5x5':
        laud('5x5')
    #end

    esimesevoidud = esimesevoidud + 1

    print('\n\nMäng lõppes ja esimene mängija võitis!')
    scoreboard()
    uuesti()
#end

def teinevoitis(lauasuurus):
    global teisevoidud

    time.sleep(1)
    clear()

    if lauasuurus == '3x3':
        laud('3x3')
    elif lauasuurus == '4x4':
        laud('4x4')
    elif lauasuurus == '5x5':
        laud('5x5')
    #end

    teisevoidud = teisevoidud + 1

    print('\n\nMäng lõppes ja teine mängija võitis!\n')
    scoreboard()
    uuesti()
#end

def viik(lauasuurus):
    time.sleep(3)
    clear()

    if lauasuurus == '3x3':
        laud('3x3')
    elif lauasuurus == '4x4':
        laud('4x4')
    elif lauasuurus == '5x5':
        laud('5x5')
    #end

    print('\n\nMäng lõppes ja tekkis viik!\n')
    uuesti()
#end

def sobilik():
    print('\nSee ei ole sobilik vastus!')

    time.sleep(1)
    clear()
#end

def paigutas1(lauasuurus, valik, number, numberlist):
    global esimene
    proov = 0

    if lauasuurus == '3x3':
        while proov < 9:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = esimene
                print('\nEsimene mängija paigutas enda tähemärgi kohale', valik)
                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    elif lauasuurus == '4x4':
        while proov < 16:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = esimene

                print('\nEsimene mängija paigutas enda tähemärgi kohale', valik)

                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    elif lauasuurus == '5x5':
        while proov < 25:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = esimene

                print('\nEsimene mängija paigutas enda tähemärgi kohale', valik)

                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    #end

    return False
#end

def paigutas2(lauasuurus, valik, number, numberlist):
    global teine
    proov = 0

    if lauasuurus == '3x3':
        while proov < 9:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = teine

                print('Teine mängija paigutas enda tähemärgi kohale', valik)

                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    elif lauasuurus == '4x4':
        while proov < 16:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = teine

                print('Teine mängija paigutas enda tähemärgi kohale', valik)

                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    elif lauasuurus == '5x5':
        while proov < 25:
            proov = proov + 1

            if valik == number and mangulist[numberlist] == '#':
                mangulist[numberlist] = teine

                print('Teine mängija paigutas enda tähemärgi kohale', valik)

                return True
            #end

            number = number + 1
            numberlist = numberlist + 1
        #end
    #end

    time.sleep(2)

    return False
#end

##########
############ Localed
##########



##########
############ Üldised funktsioonid
##########

def laud(lauasuurus):
    global mangulaud
    
    if lauasuurus == '3x3':
        print("       ║       ║       \n   {}   ║   {}   ║   {}   \n       ║       ║       \n═══════╬═══════╬═══════\n       ║       ║       \n   {}   ║   {}   ║   {}   \n       ║       ║       \n═══════╬═══════╬═══════\n       ║       ║       \n   {}   ║   {}   ║   {}   \n       ║       ║       ".format(mangulist[6], mangulist[7], mangulist[8], mangulist[3], mangulist[4], mangulist[5], mangulist[0], mangulist[1], mangulist[2]).translate({ord(i): ' ' for i in '#'}))
    elif lauasuurus == '4x4':
        print("       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ".format(mangulist[12], mangulist[13], mangulist[14], mangulist[15], mangulist[8], mangulist[9], mangulist[10], mangulist[11], mangulist[4], mangulist[5], mangulist[6], mangulist[7], mangulist[0], mangulist[1], mangulist[2], mangulist[3]).translate({ord(i): ' ' for i in '#'}))
    elif lauasuurus == '5x5':
        print("       ║       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ║       \n═══════╬═══════╬═══════╬═══════╬═══════\n       ║       ║       ║       ║       \n   {}   ║   {}   ║   {}   ║   {}   ║   {}   \n       ║       ║       ║       ║       ".format(mangulist[20], mangulist[21], mangulist[22], mangulist[23], mangulist[24], mangulist[15], mangulist[16], mangulist[17], mangulist[18], mangulist[19], mangulist[10], mangulist[11], mangulist[12], mangulist[13], mangulist[14], mangulist[5], mangulist[6], mangulist[7], mangulist[8], mangulist[9], mangulist[0], mangulist[1], mangulist[2], mangulist[3], mangulist[4]).translate({ord(i): ' ' for i in '#'}))
    #end
#end

def alusta():
    global esimene, teine, lauasuurus, arvuti

    while True:
        try:
            arvuti = str(input('Kas sa soovid mängida arvuti vastu? (Jah/Ei) : '))
        except:
            sobilik()
            continue
        else:
            if ((arvuti == 'J' or arvuti == 'j') or (arvuti == 'Jah' or arvuti == 'jah')):
                print('Selge, lisan mängu arvuti')
                arvuti = True
                break
            elif ((arvuti == 'E' or arvuti == 'e') or (arvuti == 'Ei' or arvuti == 'ei')):
                print('Selge, ei lisa mängu arvutit')
                arvuti = False
                break
            else:
                sobilik()
                continue
            #end
        #end
    #end

    time.sleep(1)
    clear()

    while True:
        try:
            esimene = str(input('Kas esimene mängija soovib olla X või O? (X/O) : '))
        except:
            sobilik()
            continue
        else:
            if esimene == 'X' or esimene == 'x':
                print('\nEsimene mängija valis X, seega teine mängija on O')
                esimene = 'X'
                teine = 'O'
                break
            elif esimene == 'O' or esimene == 'o':
                print('\nEsimene mängija valis O, seega teine mängija on X')
                esimene = 'O'
                teine = 'X'
                break
            else:
                sobilik()
                continue
            #end
        #end
    #end

    time.sleep(1)
    clear()

    while True:
        try:
            suurus = str(input('Kui suure laua peal te soovite mängida? (3x3/4x4/5x5) : '))
        except:
            sobilik()
            continue
        else:
            if suurus == '3x3' or suurus == '3X3':
                print('\nValisite laua suuruseks 3x3')
                tutorial('3x3')
                break
            elif suurus == '4x4' or suurus == '4X4':
                print('\nValisite laua suuruseks 4x4')
                tutorial('4x4')
                break
            elif suurus == '5x5' or suurus == '5X5':
                print('\nValisite laua suuruseks 5x5')
                tutorial('5x5')
                break
            else:
                sobilik()
                continue
            #end
        #end
    #end

    time.sleep(1)
    clear()
#end

def edasi(lauasuurus):
    clear()
    mang(lauasuurus)
#end

def tutorial(lauasuurus):
    time.sleep(1)
    clear()
    print("Õpetust on aega vaadata 30 sekundit\n\n")
    if lauasuurus == '3x3':
        print("       ║       ║       ")
        print("   7   ║   8   ║   9   ")
        print("       ║       ║       ")
        print("═══════╬═══════╬═══════")
        print("       ║       ║       ")
        print("   4   ║   5   ║   6   ")
        print("       ║       ║       ")
        print("═══════╬═══════╬═══════")
        print("       ║       ║       ")
        print("   1   ║   2   ║   3   ")
        print("       ║       ║       ")   
        print("\n\nÜleval on ruudustik numbritega, numbrid on samasugused nagu numpadil.")
        print("\nKui sa oled ära valinud kas sa oled 'X' või 'O', siis edaspidi sa saad enda käigu ajal vajutada numpadil vastavat nuppu kohaga kuhu sa soovid enda tähemärki paigutada.")
        print('\nVõitmiseks pead sa 3 tükki järjest saama kas horisontaalselt, vertikaalselt või diagonaalselt.')
        input('\n\nEdasi minemiseks vajuta ENTER')

        edasi(lauasuurus)
    elif lauasuurus == '4x4':
        print("       ║       ║       ║       ")
        print("   13  ║   14  ║   15  ║   16  ")
        print("       ║       ║       ║       ")
        print("═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ")
        print("   9   ║   10  ║   11  ║   12  ")
        print("       ║       ║       ║       ")
        print("═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ")
        print("   5   ║   6   ║   7   ║   8   ")
        print("       ║       ║       ║       ")   
        print("═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ")
        print("   1   ║   2   ║   3   ║   4   ")
        print("       ║       ║       ║       ")
        print("\n\nÜleval on ruudustik numbritega.")
        print("\nKui sa oled ära valinud kas sa oled 'X' või 'O', siis edaspidi sa saad enda käigu ajal kirjutada sisse vastava numbri kuhu sa soovid enda tähemärki paigutada.")
        print('\nVõitmiseks pead sa 4 tükki järjest saama kas horisontaalselt, vertikaalselt või diagonaalselt.')
        input('\n\nEdasi minemiseks vajuta ENTER')
        
        edasi(lauasuurus)
    elif lauasuurus == '5x5':
        print("       ║       ║       ║       ║       ")
        print("   21  ║   22  ║   23  ║   24  ║   25  ")
        print("       ║       ║       ║       ║       ")
        print("═══════╬═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ║       ")
        print("   16  ║   17  ║   18  ║   19  ║   20  ")
        print("       ║       ║       ║       ║       ")
        print("═══════╬═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ║       ")
        print("   11  ║   12  ║   13  ║   14  ║   15  ")
        print("       ║       ║       ║       ║       ")   
        print("═══════╬═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ║       ")
        print("   6   ║   7   ║   8   ║   9   ║   10  ")
        print("       ║       ║       ║       ║       ")
        print("═══════╬═══════╬═══════╬═══════╬═══════")
        print("       ║       ║       ║       ║       ")
        print("   1   ║   2   ║   3   ║   4   ║   5   ")
        print("       ║       ║       ║       ║       ")
        print("\n\nÜleval on ruudustik numbritega.")
        print("\nKui sa oled ära valinud kas sa oled 'X' või 'O', siis edaspidi sa saad enda käigu ajal kirjutada sisse vastava numbri kuhu sa soovid enda tähemärki paigutada.")
        print('\nVõitmiseks pead sa 5 tükki järjest saama kas horisontaalselt, vertikaalselt või diagonaalselt.')
        input('\n\nEdasi minemiseks vajuta ENTER')
        
        edasi(lauasuurus)
    #end
#end

### 3x3

def kontroll(lauasuurus, kaik):
    global mangulist, esimene, teine

    if lauasuurus == '3x3':
        if kaik >= 5:
            if (mangulist[0] == mangulist[1] == mangulist[2] == esimene) or (mangulist[3] == mangulist[4] == mangulist[5] == esimene) or (mangulist[6] == mangulist[7] == mangulist[8] == esimene) or (mangulist[0] == mangulist[3] == mangulist[6] == esimene) or (mangulist[1] == mangulist[4] == mangulist[7] == esimene) or (mangulist[2] == mangulist[5] == mangulist[8] == esimene) or (mangulist[0] == mangulist[4] == mangulist[8] == esimene) or (mangulist[2] == mangulist[4] == mangulist[6] == esimene):
                esimenevoitis(lauasuurus)
                return True
            elif (mangulist[0] == mangulist[1] == mangulist[2] == teine) or (mangulist[3] == mangulist[4] == mangulist[5] == teine) or (mangulist[6] == mangulist[7] == mangulist[8] == teine) or (mangulist[0] == mangulist[3] == mangulist[6] == teine) or (mangulist[1] == mangulist[4] == mangulist[7] == teine) or (mangulist[2] == mangulist[5] == mangulist[8] == teine) or (mangulist[0] == mangulist[4] == mangulist[8] == teine) or (mangulist[2] == mangulist[4] == mangulist[6] == teine):
                teinevoitis(lauasuurus)
                return True
            #end
        elif kaik == 9:
            viik(lauasuurus)
            return True
        #end
    elif lauasuurus == '4x4':
        if kaik >= 7:
            if (mangulist[0] == mangulist[1] == mangulist[2] == mangulist[3] == esimene) or (mangulist[4] == mangulist[5] == mangulist[6] == mangulist[7] == esimene) or (mangulist[8] == mangulist[9] == mangulist[10] == mangulist[11] == esimene) or (mangulist[12] == mangulist[13] == mangulist[14] == mangulist[15] == esimene) or (mangulist[0] == mangulist[4] == mangulist[8] == mangulist[12] == esimene) or (mangulist[1] == mangulist[5] == mangulist[9] == mangulist[13] == esimene) or (mangulist[2] == mangulist[6] == mangulist[10] == mangulist[14] == esimene) or (mangulist[3] == mangulist[7] == mangulist[11] == mangulist[15] == esimene) or (mangulist[0] == mangulist[5] == mangulist[10] == mangulist[15] == esimene) or (mangulist[3] == mangulist[6] == mangulist[9] == mangulist[12] == esimene):
                esimenevoitis(lauasuurus)
                return True
            elif (mangulist[0] == mangulist[1] == mangulist[2] == mangulist[3] == teine) or (mangulist[4] == mangulist[5] == mangulist[6] == mangulist[7] == teine) or (mangulist[8] == mangulist[9] == mangulist[10] == mangulist[11] == teine) or (mangulist[12] == mangulist[13] == mangulist[14] == mangulist[15] == teine) or (mangulist[0] == mangulist[4] == mangulist[8] == mangulist[12] == teine) or (mangulist[1] == mangulist[5] == mangulist[9] == mangulist[13] == teine) or (mangulist[2] == mangulist[6] == mangulist[10] == mangulist[14] == teine) or (mangulist[3] == mangulist[7] == mangulist[11] == mangulist[15] == teine) or (mangulist[0] == mangulist[5] == mangulist[10] == mangulist[15] == teine) or (mangulist[3] == mangulist[6] == mangulist[9] == mangulist[12] == teine):
                teinevoitis(lauasuurus)
                return True
            #end
        elif kaik == 16:
            viik(lauasuurus)
            return True
        #end
    elif lauasuurus == '5x5':
        if kaik >= 9:
            if (mangulist[0] == mangulist[1] == mangulist[2] == mangulist[3] == mangulist[4] == esimene) or (mangulist[5] == mangulist[6] == mangulist[7] == mangulist[8] == mangulist[9] == esimene) or (mangulist[10] == mangulist[11] == mangulist[12] == mangulist[13] == mangulist[14] == esimene) or (mangulist[15] == mangulist[16] == mangulist[17] == mangulist[18] == mangulist[19] == esimene) or (mangulist[20] == mangulist[21] == mangulist[22] == mangulist[23] == mangulist[24] == esimene) or (mangulist[0] == mangulist[5] == mangulist[10] == mangulist[15] == mangulist[20] == esimene) or (mangulist[1] == mangulist[6] == mangulist[11] == mangulist[16] == mangulist[21] == esimene) or (mangulist[2] == mangulist[7] == mangulist[12] == mangulist[17] == mangulist[22] == esimene) or (mangulist[3] == mangulist[8] == mangulist[13] == mangulist[18] == mangulist[23] == esimene) or (mangulist[4] == mangulist[9] == mangulist[14] == mangulist[19] == mangulist[24] == esimene) or (mangulist[0] == mangulist[6] == mangulist[12] == mangulist[18] == mangulist[24] == esimene) or (mangulist[20] == mangulist[16] == mangulist[12] == mangulist[8] == mangulist[4] == esimene):
                esimenevoitis(lauasuurus)
                return True
            elif (mangulist[0] == mangulist[1] == mangulist[2] == mangulist[3] == mangulist[4] == teine) or (mangulist[5] == mangulist[6] == mangulist[7] == mangulist[8] == mangulist[9] == teine) or (mangulist[10] == mangulist[11] == mangulist[12] == mangulist[13] == mangulist[14] == teine) or (mangulist[15] == mangulist[16] == mangulist[17] == mangulist[18] == mangulist[19] == teine) or (mangulist[20] == mangulist[21] == mangulist[22] == mangulist[23] == mangulist[24] == teine) or (mangulist[0] == mangulist[5] == mangulist[10] == mangulist[15] == mangulist[20] == teine) or (mangulist[1] == mangulist[6] == mangulist[11] == mangulist[16] == mangulist[21] == teine) or (mangulist[2] == mangulist[7] == mangulist[12] == mangulist[17] == mangulist[22] == teine) or (mangulist[3] == mangulist[8] == mangulist[13] == mangulist[18] == mangulist[23] == teine) or (mangulist[4] == mangulist[9] == mangulist[14] == mangulist[19] == mangulist[24] == teine) or (mangulist[0] == mangulist[6] == mangulist[12] == mangulist[18] == mangulist[24] == teine) or (mangulist[20] == mangulist[16] == mangulist[12] == mangulist[8] == mangulist[4] == teine):
                teinevoitis(lauasuurus)
                return True
            #end
        elif kaik == 25:
            viik(lauasuurus)
            return True
        #end
    #end
#end

def mang(lauasuurus):
    global esimene, teine, arvuti

    kaik = numberlist = 0
    number = 1
    valik = ''
    
    while True:
        time.sleep(1)
        clear()

        while True:
            try:
                if lauasuurus == '3x3':
                    laud('3x3')
                elif lauasuurus == '4x4':
                    laud('4x4')
                elif lauasuurus == '5x5':
                    laud('5x5')
                #end

                valik = int(input('\nMillisele kohale soovib esimene mängija enda tähemärgi paigutada? : '))
            except:
                sobilik()
                continue
            else:
                number = 1
                numberlist = 0

                if lauasuurus == '3x3':
                    if valik <= 9 and valik >= 1:
                        if paigutas1('3x3', valik, number, numberlist) == True:
                            break
                        else:
                            sobilik()
                            continue
                        #end
                    else:
                        sobilik()
                        continue
                    #end
                elif lauasuurus == '4x4':
                    if valik <= 16 and valik >= 1:
                        if paigutas1('4x4', valik, number, numberlist) == True:
                            break
                        else:
                            sobilik()
                            continue
                        #end
                    else:
                        sobilik()
                        continue
                    #end
                elif lauasuurus == '5x5':
                    if valik <= 25 and valik >= 1:
                        if paigutas1('5x5', valik, number, numberlist) == True:
                            break
                        else:
                            sobilik()
                            continue
                        #end
                    else:
                        sobilik()
                        continue
                    #end
                #end
            #end
        #end

        kaik = kaik + 1
        
        if lauasuurus == '3x3':
            if kontroll('3x3', kaik) == True:
                break
            #end
        elif lauasuurus == '4x4':
            if kontroll('4x4', kaik) == True:
                break
            #end
        elif lauasuurus == '5x5':
            if kontroll('5x5', kaik) == True:
                break
            #end
        #end

        time.sleep(1)
        clear()

        if arvuti == False:
            while True:
                try:
                    if lauasuurus == '3x3':
                        laud('3x3')
                    elif lauasuurus == '4x4':
                        laud('4x4')
                    elif lauasuurus == '5x5':
                        laud('5x5')
                    #end

                    valik = int(input('\nMillisele kohale soovib teine mängija enda tähemärgi paigutada? : '))
                except:
                    sobilik()
                    continue
                else:
                    number = 1
                    numberlist = 0

                    if lauasuurus == '3x3':
                        if valik <= 9 and valik >= 1:
                            if paigutas2('3x3', valik, number, numberlist) == True:
                                break
                            else:
                                sobilik()
                                continue
                            #end
                        else:
                            sobilik()
                            continue
                        #end
                    elif lauasuurus == '4x4':
                        if valik <= 16 and valik >= 1:
                            if paigutas2('4x4', valik, number, numberlist) == True:
                                break
                            else:
                                sobilik()
                                continue
                            #end
                        else:
                            sobilik()
                            continue
                        #end
                    elif lauasuurus == '5x5':
                        if valik <= 25 and valik >= 1:
                            if paigutas2('5x5', valik, number, numberlist) == True:
                                break
                            else:
                                sobilik()
                                continue
                            #end
                        else:
                            sobilik()
                            continue
                        #end
                    else:
                        sobilik()
                        continue
                    #end
                #end
            #end
        elif arvuti == True:
            while True:
                number = 1
                numberlist = 0

                if lauasuurus == '3x3':
                    laud('3x3')
                elif lauasuurus == '4x4':
                    laud('4x4')
                elif lauasuurus == '5x5':
                    laud('5x5')
                #end

                if lauasuurus == '3x3':
                    valik = random.randint(1, 9)

                    if paigutas2('3x3', valik, number, numberlist) == True:
                        break
                    else:
                        continue
                    #end
                elif lauasuurus == '4x4':
                    valik = random.randint(1, 16)

                    if paigutas2('4x4', valik, number, numberlist) == True:
                        break
                    else:
                        continue
                    #end
                elif lauasuurus == '5x5':
                    valik = random.randint(1, 25)

                    if paigutas2('5x5', valik, number, numberlist) == True:
                        break
                    else:
                        continue
                    #end
                #end
            #end
        #end

        kaik = kaik + 1

        if lauasuurus == '3x3':
            if kontroll('3x3', kaik) == True:
                break
            #end
        elif lauasuurus == '4x4':
            if kontroll('4x4', kaik) == True:
                break
            #end
        elif lauasuurus == '5x5':
            if kontroll('5x5', kaik) == True:
                break
            #end
        #end

    #end
#end



#########
########### Käivitamine
#########

alusta()