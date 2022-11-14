import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',180)

def calc(strk):
    
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
    return str(a)


def speaker(stri):
    engine.say(stri)
    engine.runAndWait()


if __name__=='__main__':
    a = input().split()
    print(c := calc(a))
    speaker(c)