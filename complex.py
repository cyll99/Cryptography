from queue import Queue

def enigma3():
    def vigenere3():
        key = input()
        tab = [ord(el) for el in key]
        plaintext = input()
        cipherText = ''
        j = 0
        for el in plaintext:
            l = ord(el) + tab[j % len(tab)]
            if l > 127:
                while l > 127:
                    l = l - 127
            elif l < 0:
                while l < 0:
                    l = l + 127

            cipherText = cipherText + chr(l)
            j += 1

        # print(cipherText)
        return cipherText

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


    text = vigenere3()
    rotor = [chr(x) for x in range(128)]
    rotor2 = [x for x in clear_rotor(rotor)]
    rotor3 = [x for x in clear_rotor2(rotor2)]


    cipherText = ''

    # print(rotor)
    for i in text:
        cipherText += rotor3[rotor2.index(rotor2[rotor.index(rotor[ord(i)])])]
        rotor = clear_rotor(rotor)
        rotor2 = clear_rotor2(rotor2)
        rotor3 = clear_rotor3(rotor3)
    return cipherText



c = enigma3()
print(c)




def vigenere3_reverse():
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
        rotor = [chr(x) for x in range(128)]
        alphabet = [x for x in rotor]
        rotor2 = [x for x in clear_rotor(rotor)]
        rotor3 = [x for x in clear_rotor2(rotor2)]

        text = ''
        for i in c:
            text += alphabet[rotor.index(rotor[rotor2.index(rotor2[rotor3.index(i)])])]
            rotor = clear_rotor(rotor)
            rotor2 = clear_rotor2(rotor2)
            rotor3 = clear_rotor3(rotor3)
        return text

    key = input('Key: ')
    tab = [ord(el) for el in key]
    plaintext = enigma_reverse3()
    cipherText = ''
    j = 0
    for el in plaintext:
        l = ord(el) - tab[j % len(tab)]
        if l > 127:
            while l > 127:
                l = l - 127
        elif l < 0:
            while l < 0:
                l = l + 127

        cipherText = cipherText + chr(l)
        j += 1

    print(cipherText)
vigenere3_reverse()