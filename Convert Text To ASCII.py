'''
Print your name in Symbols
author: Dena, Rene

I chose the vertical output of character because it horizontally will not check correctly.

apdate 1.1: Add to function:
            1. Lists for the formation of the letters.
            2. Processing errors in text_input.

apdate 1.2: Change Z symbol.
apdate 1.3: Change Lists for the formation of the letters.

apdate 1.4: Print in a horizontal line.(in the phone does not display correctly).
            if you want to try, to add a function parameter TRUE. an example of a function call:

            print_text_in_symbol(text_input, rand_ch, rand_bg, inline = True)

            At the bottom I commented this function

apdate 1.5: Change Lists for the formation of the letters.

apdate 1.6: Add to function output: 1 Space .
                                    2 Numbers 0-9 .
                                    3 Symbols ?!,.-+ .

Thanks for more than 1000 likes, and thanks for the comments.
'''
# Enter only your name in input bar

from random import randrange


# --------------Function print_text_in_symbol-----------------
def print_text_in_symbol(text_input, symbol_char='X', symbol_bg='-', inline=False):
    # ---------Lists for the formation of the letters----------
    a = ['000000000000',
         '000111111000',
         '011000000110',
         '011000000110',
         '011111111110',
         '011000000110',
         '011000000110',
         '011000000110']

    b = ['000000000000',
         '011111111000',
         '011000000110',
         '011000000110',
         '011111111000',
         '011000000110',
         '011000000110',
         '011111111000']

    c = ['000000000000',
         '000111111000',
         '011000000110',
         '011000000000',
         '011000000000',
         '011000000000',
         '011000000110',
         '000111111000']

    d = ['000000000000',
         '011111111000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '011111111000']

    e = ['000000000000',
         '011111111110',
         '011000000000',
         '011000000000',
         '011111111100',
         '011000000000',
         '011000000000',
         '011111111110']

    f = ['000000000000',
         '011111111110',
         '011000000000',
         '011000000000',
         '011111111100',
         '011000000000',
         '011000000000',
         '011000000000']

    g = ['000000000000',
         '000111111000',
         '011000000110',
         '011000000000',
         '011000000000',
         '011000011110',
         '011000000110',
         '000111111000']

    h = ['000000000000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011111111110',
         '011000000110',
         '011000000110',
         '011000000110']

    i = ['000000000000',
         '000111111000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000111111000']

    j = ['000000000000',
         '000001111110',
         '000000011000',
         '000000011000',
         '000000011000',
         '000000011000',
         '011000011000',
         '000111100000']

    k = ['000000000000',
         '011000000110',
         '011000011000',
         '011001100000',
         '011110000000',
         '011001100000',
         '011000011000',
         '011000000110']

    l = ['000000000000',
         '011000000000',
         '011000000000',
         '011000000000',
         '011000000000',
         '011000000000',
         '011000000000',
         '011111111110']

    m = ['000000000000',
         '011000000110',
         '011110011110',
         '011001100110',
         '011001100110',
         '011000000110',
         '011000000110',
         '011000000110']

    n = ['000000000000',
         '011000000110',
         '011000000110',
         '011110000110',
         '011001100110',
         '011000011110',
         '011000000110',
         '011000000110']

    o = ['000000000000',
         '000111111000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '000111111000']

    p = ['000000000000',
         '011111111000',
         '011000000110',
         '011000000110',
         '011111111000',
         '011000000000',
         '011000000000',
         '011000000000']

    q = ['000000000000',
         '000111111000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011001100110',
         '011000011000',
         '000111100110']

    r = ['000000000000',
         '011111111000',
         '011000000110',
         '011000000110',
         '011111111000',
         '011001100000',
         '011000011000',
         '011000000110']

    s = ['000000000000',
         '000111111110',
         '011000000000',
         '011000000000',
         '000111111000',
         '000000000110',
         '000000000110',
         '011111111000']

    t = ['000000000000',
         '011111111110',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000']

    u = ['000000000000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '000111111000']

    v = ['000000000000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011000000110',
         '000110011000',
         '000110011000',
         '000001100000']

    w = ['000000000000',
         '011000000110',
         '011000000110',
         '011000000110',
         '011001100110',
         '011001100110',
         '011001100110',
         '000110011000']

    x = ['000000000000',
         '011000000110',
         '011000000110',
         '000110011000',
         '000001100000',
         '000110011000',
         '011000000110',
         '011000000110']

    y = ['000000000000',
         '011000000110',
         '011000000110',
         '000110011000',
         '000001100000',
         '000001100000',
         '000001100000',
         '000001100000']

    z = ['000000000000',
         '011111111110',
         '000000000110',
         '000000011000',
         '000001100000',
         '000110000000',
         '011000000000',
         '011111111110']

    sp = ['000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000']

    n0 = ['000000000000',
          '000111111000',
          '011000000110',
          '011000011110',
          '011001100110',
          '011110000110',
          '011000000110',
          '000111111000']

    n1 = ['000000000000',
          '000001100000',
          '000111100000',
          '000001100000',
          '000001100000',
          '000001100000',
          '000001100000',
          '000111111000']

    n2 = ['000000000000',
          '000111111000',
          '011000000110',
          '000000000110',
          '000000011000',
          '000001100000',
          '000110000000',
          '011111111110']

    n3 = ['000000000000',
          '011111111110',
          '000000011000',
          '000001100000',
          '000000011000',
          '000000000110',
          '011000000110',
          '000111111000']

    n4 = ['000000000000',
          '000000011000',
          '000001111000',
          '000110011000',
          '011000011000',
          '011111111110',
          '000000011000',
          '000000011000']

    n5 = ['000000000000',
          '011111111110',
          '011000000000',
          '011111111000',
          '000000000110',
          '000000000110',
          '011000000110',
          '000111111000']

    n6 = ['000000000000',
          '000001111000',
          '000110000000',
          '011000000000',
          '011111111000',
          '011000000110',
          '011000000110',
          '000111111000']

    n7 = ['000000000000',
          '011111111110',
          '000000000110',
          '000000011000',
          '000001100000',
          '000110000000',
          '000110000000',
          '000110000000']

    n8 = ['000000000000',
          '000111111000',
          '011000000110',
          '011000000110',
          '000111111000',
          '011000000110',
          '011000000110',
          '000111111000']

    n9 = ['000000000000',
          '000111111000',
          '011000000110',
          '011000000110',
          '000111111110',
          '000000000110',
          '000000011000',
          '000111100000']

    s0 = ['000000000000',
          '000111111000',
          '011000000110',
          '000000000110',
          '000000011000',
          '000001100000',
          '000000000000',
          '000001100000']

    s1 = ['000000000000',
          '000001100000',
          '000001100000',
          '000001100000',
          '000001100000',
          '000001100000',
          '000000000000',
          '000001100000']

    s2 = ['000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000001100000',
          '000001100000']

    s3 = ['000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '000001100000']

    s4 = ['000000000000',
          '000000000000',
          '000000000000',
          '000000000000',
          '001111111100',
          '000000000000',
          '000000000000',
          '000000000000']

    s5 = ['000000000000',
          '000000000000',
          '000001100000',
          '000001100000',
          '011111111110',
          '000001100000',
          '000001100000',
          '000000000000']

    ascii_alph = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
                  sp, n0, n1, n2, n3, n4, n5, n6, n7, n8, n9,
                  s0, s1, s2, s3, s4, s5, s5]

    # ---END------Lists for the formation of the letters----------------

    res = ''
    dont_use = ''
    alph = 'abcdefghijklmnopqrstuvwxyz 0123456789?!,.-+'
    text_error = 'Print Successful.\n Your text :'

    text_input = text_input.lower()
    your_text = text_input

    # -----------Processing errors in text_input-----------------
    # 1. If nothing is entered
    if text_input == '':
        text_input = 'none text'
        your_text = "You don't input text."

    # 2. Checking for a character in the alphabet
    try:
        for char in text_input.lower():
            # 3. if there is no character in the alphabet function returns an error(ValueError)
            alph.index(char)

    # ------error Processing(ValueError)----
    except ValueError:
        text_error = '''
Error input. 
1. Use A-Z a-z, 0-9, ?!,.-+, for your input.
Your text: '''
        # changing text_input
        text_input = 'error'
    # ---END---error Processing(ValueError)------

    finally:
        # Outputs the generated string
        print(text_error + your_text + dont_use)

        if inline:
            res = ''
            print_res = ''
            for i in range(0, 8):
                for char in text_input:
                    ch_ascii = ascii_alph[alph.index(char)]
                    res += ch_ascii[i]
                res += '\n'
            for char in res:
                if char == '0':
                    print_res += symbol_bg
                elif char == '1':
                    print_res += symbol_char
                elif char == '\n':
                    print_res += '\n'
            print(print_res)
        else:
            for char in text_input:
                ch_ascii = ascii_alph[alph.index(char)]
                for i in ch_ascii:
                    for t in i:
                        for char in t:
                            if char == '0':
                                res += symbol_bg
                            elif char == '1':
                                res += symbol_char
                    print(res)
                    res = ''
                    # ---END-----Processing errors in input-----------------


# -----END---------Function print_text_in_symbol------------

# ---Set for select characters-------------------------------
ch = 'XO#@'
ch_bg = '.`'
# ---Random selection of a set of characters----------------
rand_ch = ch[randrange(len(ch))]
rand_bg = ch_bg[randrange(len(ch_bg))]

# User input----------------------------------------
text_input = input("\t\t\t\n\nPlease Enter Your Text: ")

print("\nPrinting in a horizontal line".upper())
print_text_in_symbol(text_input, rand_ch, rand_bg, inline = True)

# print("\nPrinting in a vertical line".upper())
# print_text_in_symbol(text_input, rand_ch, rand_bg, inline=False)
