# coding: utf-8
import sys
import docx2txt


# def cipher():
#     tab = []
#     for el in sys.argv[1]:
#         l = ord(el)
#         tab.append(l)
#     cipherTab = []
#     j = 0
#     with open('papa.txt') as file:
#         for line in file.readlines():
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
# cipher()

#
# def cipher_reverse():
#     tab = []
#     for el in sys.argv[1]:
#         l = ord(el)
#         tab.append(l)
#     cipherTab = []
#     j = 0
#     with open('papa.txt') as file:
#         line = file.read()
#         cipherText = ''
#         for i in line:
#             l = ord(i) - tab[j % len(tab)]
#             if l > 127:
#                 while l > 127:
#                     l = l - 127
#             elif l < 0:
#                 while l < 0:
#                     l = l  + 127
#             cipherText = cipherText + chr(l)
#             j += 1
#         cipherTab.append(cipherText)
#         with open('papa.txt', 'w') as reader:
#             reader.write(cipherText)
#
#         print(cipherText)
#
#
# cipher_reverse()

# print(sys.argv[1])
# def cipher2():
#     tab = []
#     j = 0
#     cipherTab = []
#     with open(sys.argv[1], 'r', encoding="utf-8") as file:
#         for i in file.read():
#             l = ord(i)
#             tab.append(l)
#     with open(sys.argv[2], 'r', encoding="utf-8") as file:
#         for line in file.readlines():
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
#     with open(sys.argv[2], 'w', encoding="utf-8") as reader:
#         reader.writelines(cipherTab)
#
#     print(cipherText)
#
#
# cipher2()

# # read in word file
# result = docx2txt.process(sys.argv[1])
# print(result)

def cipher2_reverse():
    tab = []
    j = 0
    with open(sys.argv[1], 'r',encoding="utf-8") as file:
        for i in file.read():
            l = ord(i)
            tab.append(l)
    with open(sys.argv[2], 'r',encoding="utf-8") as file:
        line = file.read()
        cipherText = ''
        for i in line:
            l = ord(i) - tab[j % len(tab)]
            if l > 127:
                while l > 127:
                    l = l - 127
            elif l < 0:
                while l < 0:
                    l = l + 127
            cipherText = cipherText + chr(l)
            j += 1
    with open(sys.argv[2], 'w', encoding="utf-8") as reader:
        reader.write(cipherText)



cipher2_reverse()
