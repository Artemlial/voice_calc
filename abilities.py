import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',180)

def calc(strk):

    rev_dec_t ={
                0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 
                10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 
                17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 
                60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 
                500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот', 1000: 'тысяча'
                }
    
    b = 0
    s2 = ''

    for i in strk:
        if i.isdecimal():
            b+=int(i)
        elif b == 0:
            s2 += i
        else:
            s2 = s2+str(b)+i
            b = 0
    if b != 0:
        s2 +=str(b)

    a = eval(s2)
    sign = a//abs(a)
    a=abs(a)
    try:
        return 'минус '*((1-sign)//2) + rev_dec_t[a]
    except KeyError:
        p = 1
        intermed = []
        if a%100 in rev_dec_t.keys():
            intermed.append(rev_dec_t[a%100])
            p=3
            a-=a%100
        while a > 0:
            if (k:= a%10**p)>0:
                intermed.append(rev_dec_t[a%10**p])
            a -= k
            p+=1
         
        return 'минус '*((1-sign)//2) + ' '.join(intermed[::-1])


def speaker(stri):
    engine.say(stri)
    engine.runAndWait()


if __name__=='__main__':
    print(calc(input()))