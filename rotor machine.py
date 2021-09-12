from queue import Queue



def enigma():
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

    text = input()
    rotor = [chr(x) for x in range(128)]


    cipherText = ''

    # print(rotor)
    for i in text:
        cipherText += rotor[ord(i)]
        rotor = clear_rotor(rotor)
    return cipherText


a = enigma()
print(a)

def enigma_reverse():
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

    # cipherText = input()
    rotor= [chr(x) for x in range(128)]
    alphabet = [chr(x) for x in range(128)]

    text = ''
    for i in a:
        text += alphabet[rotor.index(i)]
        rotor = clear_rotor(rotor)
    return text

print(enigma_reverse())

def enigma2():
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
    text = input()
    rotor = [chr(x) for x in range(128)]
    rotor2 = [x for x in clear_rotor(rotor)]


    cipherText = ''

    # print(rotor)
    for i in text:
        cipherText += rotor2[rotor.index(rotor[ord(i)])]
        rotor = clear_rotor(rotor)
        rotor2 = clear_rotor2(rotor2)
    return cipherText

b = enigma2()
print(b)

def enigma_reverse2():
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

    # cipherText = input()
    rotor= [chr(x) for x in range(128)]
    alphabet = [x for x in rotor]
    rotor2 = [x for x in clear_rotor(rotor)]

    text = ''
    for i in b:
        text += alphabet[rotor.index(rotor[rotor2.index(i)])]
        rotor = clear_rotor(rotor)
        rotor2 = clear_rotor2(rotor2)
    return text

print(enigma_reverse2())

def enigma3():
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


    text = input()
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
    for i in c:
        text += alphabet[rotor.index(rotor[rotor2.index(rotor2[rotor3.index(i)])])]
        rotor = clear_rotor(rotor)
        rotor2 = clear_rotor2(rotor2)
        rotor3 = clear_rotor3(rotor3)
    return text

print(enigma_reverse3())