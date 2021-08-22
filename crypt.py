# # print(chr(ord('a')+1))
# import random
#
#
# def cipher1():
#     plaintext = input()
#     cipherText = ''
#     key = random.randint(0,100)
#     print(key)
#     # key = int(input())
#     for el in plaintext:
#         l = ord(el) + key
#         if ord(el) in range(65, 91):
#             if l > 90:
#                 while l > 90:
#                     l = l - 90 + 64
#             cipherText = cipherText + chr(l)
#
#         elif ord(el) in range(97, 123):
#             if l > 122:
#                 while l > 122:
#                     l = l - 122 + 96
#             cipherText = cipherText + chr(l)
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
# cipher1()
#
# def cipher2():
#     plaintext = input()
#     cipherText = ''
#     key = int(input())
#     for el in plaintext.lower():
#         l = ord(el) + key
#         if ord(el) in range(65, 91):
#             if l > 90:
#                 while l > 90:
#                     l = l - 90 + 64
#             cipherText = cipherText + chr(l)
#
#         elif ord(el) in range(97, 123):
#             if l > 122:
#                 while l > 122:
#                     l = l - 122 + 96
#             cipherText = cipherText + chr(l)
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
# cipher2()
#
# def cipher2_reverse():
#     plaintext = input()
#     cipherText = ''
#     key = int(input())
#     for el in plaintext.lower():
#         l = ord(el) - key
#         if ord(el) in range(65, 91):
#             if l <65:
#                 while l <65:
#                     l = l + 90 - 64
#             cipherText = cipherText + chr(l)
#
#         elif ord(el) in range(97, 123):
#             if l <97:
#                 while l<97:
#                     l = l + 122 - 96
#             cipherText = cipherText + chr(l)
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
# cipher2_reverse()
# #
# def vigenere():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el.upper()) - 65
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) + tab[j % len(tab)]
#         if ord(el) in range(65, 91):
#             if l > 90:
#                 while l > 90:
#                     l = l - 90 + 64
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         elif ord(el) in range(97, 123):
#             if l > 122:
#                 while l > 122:
#                     l = l - 122 + 96
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
#
# vigenere()
#
#
# def vigenere_reverse():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el.upper()) - 65
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) - tab[j % len(tab)]
#         if ord(el) in range(65, 91):
#             if l < 65:
#                 while l < 65:
#                     l = l + 90 - 64
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         elif ord(el) in range(97, 123):
#             if l < 97:
#                 while l < 97:
#                     l = l + 122 - 96
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
#
# vigenere_reverse()

# def vigenere2():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el) - 65
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) + tab[j % len(tab)]
#         if ord(el) in range(65, 91):
#             if l > 90:
#                 while l > 90:
#                     l = l - 90 + 64
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         elif ord(el) in range(97, 123):
#             if l > 122:
#                 while l > 122:
#                     l = l - 122 + 96
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
#
# vigenere2()
#
#
# def vigenere_reverse2():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el) - 65
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) - tab[j % len(tab)]
#         if ord(el) in range(65, 91):
#             if l < 65:
#                 while l < 65:
#                     l = l + 90 - 64
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         elif ord(el) in range(97, 123):
#             if l < 97:
#                 while l < 97:
#                     l = l + 122 - 96
#             cipherText = cipherText + chr(l)
#             j += 1
#
#         else:
#             cipherText = cipherText + el
#
#     print(cipherText)
#
#
# vigenere_reverse2()

#
# def vigenere3():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el)
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) + tab[j % len(tab)]
#         if l > 127:
#             while l > 127:
#                 l = l - 127 + 31
#         elif l < 32:
#             while l < 32:
#                 l = l - 31 + 127
#
#         cipherText = cipherText + chr(l)
#         j += 1
#
#     print(cipherText)
#
#
# vigenere3()

#
# def vigenere3_reverse():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el)
#         tab.append(l)
#     plaintext = input()
#     cipherText = ''
#     j = 0
#     for el in plaintext:
#         l = ord(el) - tab[j % len(tab)]
#         if l > 127:
#             while l > 127:
#                 l = l - 127 + 31
#         elif l < 32:
#             while l < 32:
#                 l = l - 31 + 127
#
#         cipherText = cipherText + chr(l)
#         j += 1
#
#     print(cipherText)
#
#
# vigenere3_reverse()
#
# def cipher():
#     key = input()
#     tab = []
#     for el in key:
#         l = ord(el)
#         tab.append(l)
#     cipherTab = []
#     j = 0
#     with open('papa.txt') as file:
#         for line in file.readlines():
#             print(line)
#             # line = line.strip()
#             cipherText = ''
#             for i in line:
#                 l = ord(i) + tab[j % len(tab)]
#                 if l > 127:
#                     while l > 127:
#                         l = l - 127
#                 elif l < 0:
#                     while l < 0:
#                         l = l + 127
#                 cipherText = cipherText + chr(l)
#                 j += 1
#             cipherTab.append(cipherText)
#     with open('papa.txt', 'w') as reader:
#         reader.writelines(cipherTab)
#
#     print(cipherText)
#
#
# cipher()


def cipher_reverse():
    key = input()
    tab = []
    for el in key:
        l = ord(el)
        tab.append(l)
    cipherTab = []
    j = 0
    with open('papa.txt') as file:
        line = file.read()
        cipherText = ''
        for i in line:
            l = ord(i) - tab[j % len(tab)]
            if l > 127:
                while l > 127:
                    l = l - 127
            elif l < 0:
                while l < 0:
                    l = l  + 127
            cipherText = cipherText + chr(l)
            j += 1
        cipherTab.append(cipherText)
        with open('papa.txt', 'w') as reader:
            reader.write(cipherText)

        print(cipherText)


cipher_reverse()
