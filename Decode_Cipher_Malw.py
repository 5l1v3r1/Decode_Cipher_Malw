#!/usr/bin/python
# Code by Miguel Mendez - @s1kr10s
# WeB: www.exploiting.cl

def mid(s, offset, amount):
    return s[offset-1:offset+amount-1]

def decrypts(ciphertext):
    offset = 10
    minAsc = 33
    maxAsc = 126

    if len(ciphertext) < 5:
        print "Largo menor a 5"

    plaintext = []
    print "Cifrado Original -> {}".format(ciphertext)

    ciphertext = mid(ciphertext, 3, len(ciphertext)-4)
    print "Cifrado Mid()    -> {}".format(ciphertext)
    print "Cifrado Len()    -> {} bytes".format(len(ciphertext))

    for i in range(len(ciphertext)):
        midcal = mid(ciphertext, i+1, 1)
        oldAsc = int(midcal.encode("hex"), 16) + offset

        if oldAsc > maxAsc:
            oldAsc = oldAsc - maxAsc + minAsc - 1

        plaintext.append(chr(oldAsc))
    return plaintext

if __name__ == "__main__":
    strencode = raw_input("Input key: ")

    urlfinal = []
    plaintext = decrypts(strencode)
    for key, valor in enumerate(plaintext):
        if key % 2 != 0:
            urlfinal.append(valor)

    print "Decifrado Final  -> {}".format("".join(urlfinal))
