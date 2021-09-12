import sys
from queue import Queue

#
# def enigma3():
#     def clear_rotor(rotor):
#         q = Queue(maxsize=128)
#         for i in rotor:
#             q.put(i)
#         a = q.get()
#         q.put(a)
#         rotor.clear()
#         for i in range(128):
#             rotor.append(q.get())
#         return rotor
#
#     def clear_rotor2(rotor):
#         q = Queue(maxsize=128)
#         for i in rotor:
#             q.put(i)
#         for i in range(2):
#             a = q.get()
#             q.put(a)
#         rotor.clear()
#         for i in range(128):
#             rotor.append(q.get())
#         return rotor
#
#     def clear_rotor3(rotor):
#         q = Queue(maxsize=128)
#         for i in rotor:
#             q.put(i)
#         for i in range(3):
#             a = q.get()
#             q.put(a)
#         rotor.clear()
#         for i in range(128):
#             rotor.append(q.get())
#         return rotor
#
#
#     rotor = [chr(x) for x in range(128)]
#     rotor2 = [x for x in clear_rotor(rotor)]
#     rotor3 = [x for x in clear_rotor2(rotor2)]
#
#
#     cipherText = ''
#
#     with open(sys.argv[1], 'r', encoding="utf-8") as file:
#         for i in file.read():
#             cipherText += rotor3[rotor2.index(rotor2[rotor.index(rotor[ord(i)])])]
#             rotor = clear_rotor(rotor)
#             rotor2 = clear_rotor2(rotor2)
#             rotor3 = clear_rotor3(rotor3)
#
#     with open(sys.argv[1], 'w', encoding="utf-8") as file:
#         file.write(cipherText)
#
# enigma3()

def enigma_reverse3():
    def clear_rotor(rotor):
        q = Queue(maxsize=128)
        for i in rotor:
            q.put(i)
        a = q.get()
        q.put(a)
        rotor.clear()
        for i in range(128):
            rotor.append(q.get())
        return rotor

    def clear_rotor2(rotor):
        q = Queue(maxsize=128)
        for i in rotor:
            q.put(i)
        for i in range(2):
            a = q.get()
            q.put(a)
        rotor.clear()
        for i in range(128):
            rotor.append(q.get())
        return rotor

    def clear_rotor3(rotor):
        q = Queue(maxsize=128)
        for i in rotor:
            q.put(i)
        for i in range(3):
            a = q.get()
            q.put(a)
        rotor.clear()
        for i in range(128):
            rotor.append(q.get())
        return rotor


    # cipherText = input()
    rotor= [chr(x) for x in range(128)]
    alphabet = [x for x in rotor]
    rotor2 = [x for x in clear_rotor(rotor)]
    rotor3 = [x for x in clear_rotor2(rotor2)]

    text = ''
    with open(sys.argv[1], 'r', encoding="utf-8") as file:
        for i in file.read():
            text += alphabet[rotor.index(rotor[rotor2.index(rotor2[rotor3.index(i)])])]
            rotor = clear_rotor(rotor)
            rotor2 = clear_rotor2(rotor2)
            rotor3 = clear_rotor3(rotor3)

    with open(sys.argv[1], 'w', encoding="utf-8") as file:
        file.write(text)

enigma_reverse3()