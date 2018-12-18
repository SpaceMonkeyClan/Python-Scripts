## Morse Code Conversion Calculator - V 1.0.0
## Author: Dena, Rene
## Last Modified: 8/12/17

#________________________________________________________Misc.__________________________________________________________

a = ' .-'
b = ' -...'
c = ' -.-.'
d = ' -..'
e = ' .'
f = ' ..-.'
g = ' --.'
h = ' ....'
i = ' ..'
j = ' .---'
k = ' -.-'
l = ' .-..'
m = ' --'
n = ' -.'
o = ' ---'
p = ' .--.'
q = ' --.-'
r = ' .-.'
s = ' ...'
t = ' -'
u = ' ..-'
v = ' ...-'
w = ' .--'
x = ' -..-'
y = ' -.--'
z = ' --..'
space = ' /'
one = ' .----'
two = ' ..---'
three = ' ...--'
four = ' ....-'
five = ' .....'
six = ' -....'
seven = ' --...'
eight = ' ---..'
nine = ' ----.'
zero = ' -----'

#________________________________________________________Functions______________________________________________________

def mainConsole():
    print('\n\n\t\t\tWelcome to the MAIN CONSOLE!')
    morseCoseList = []
    usersText = input('\nPlease ENTER your text:\n')
    usersTextNew = usersText.lower()
    for x in usersTextNew:
        if x == 'a':
            morseCoseList.append(a)
        elif x == 'b':
            morseCoseList.append(b)
        elif x == 'c':
            morseCoseList.append(c)
        elif x == 'd':
            morseCoseList.append(d)
        elif x == 'e':
            morseCoseList.append(e)
        elif x == 'f':
            morseCoseList.append(f)
        elif x == 'g':
            morseCoseList.append(g)
        elif x == 'h':
            morseCoseList.append(h)
        elif x == 'i':
            morseCoseList.append(i)
        elif x == 'j':
            morseCoseList.append(j)
        elif x == 'k':
            morseCoseList.append(k)
        elif x == 'l':
            morseCoseList.append(l)
        elif x == 'm':
            morseCoseList.append(m)
        elif x == 'n':
            morseCoseList.append(n)
        elif x == 'o':
            morseCoseList.append(o)
        elif x == 'p':
            morseCoseList.append(p)
        elif x == 'q':
            morseCoseList.append(q)
        elif x == 'r':
            morseCoseList.append(r)
        elif x == 's':
            morseCoseList.append(s)
        elif x == 't':
            morseCoseList.append(t)
        elif x == 'u':
            morseCoseList.append(u)
        elif x == 'v':
            morseCoseList.append(v)
        elif x == 'w':
            morseCoseList.append(w)
        elif x == 'x':
            morseCoseList.append(x)
        elif x == 'y':
            morseCoseList.append(y)
        elif x == 'z':
            morseCoseList.append(z)
        elif x == '1':
            morseCoseList.append(one)
        elif x == '2':
            morseCoseList.append(two)
        elif x == '3':
            morseCoseList.append(three)
        elif x == '4':
            morseCoseList.append(four)
        elif x == '5':
            morseCoseList.append(five)
        elif x == '6':
            morseCoseList.append(six)
        elif x == '7':
            morseCoseList.append(seven)
        elif x == '8':
            morseCoseList.append(eight)
        elif x == '9':
            morseCoseList.append(nine)
        elif x == '0':
            morseCoseList.append(zero)
        elif x == ' ':
            morseCoseList.append(space)

    for x in morseCoseList:
        print(x)


#________________________________________________________Strictly Script________________________________________________

print('\n\t\t\tWelcome to the "Morse Code Conversion" script!')

print('\nThis script will essentially take in a text, then output such text into Morse Code.')

while True:
    usersName = input('\nIn starting, please ENTER you name: ')
    if usersName.isalpha() or ' ' in usersName and len(usersName) > 0:
        print('\nAwesome! We may now continue {}.'.format(usersName.title()))
        break
    else:
        print('\nPlease only ENTER characters a-z! >:|')

print('\nNow heading to the Main Console........')
print('\nLOADING...............&nd DONE!!!')

mainConsole()
