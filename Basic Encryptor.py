#Encryption Software By 1resU
import string
import random

abclist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numlist = ["1","2","3","4","5","6","7","8","9","0"]
run = True

def makekey():
    key1 = random.randint (1,9)
    key2 = random.sample(abclist, len(abclist))
    key3 = random.sample(numlist, len(numlist))
    print (key1,*key2,*key3, sep = ",")
    run = False


def readkey():
    thekey = input("Please paste the key")
    themessage = input("Please paste the message")
    words = thekey.split(",")
    print(words)
    thenumber = words[0][0]
    print (thenumber)
    number1 = (int(thenumber))
    print (number1)
    startletter = words [number1][:number1]
    print (startletter)
    a = words [number1][:number1]
    b = words [number1 + 1][:number1 + 1]
    c = words [number1 + 2][:number1 + 2]
    d = words [number1 + 3][:number1 + 3]
    e = words [number1 + 4][:number1 + 4]
    f = words [number1 + 5][:number1 + 5]
    g = words [number1 + 6][:number1 + 6]
    h = words [number1 + 7][:number1 + 7]
    i = words [number1 + 8][:number1 + 8]
    j = words [number1 + 9][:number1 + 9]
    k = words [number1 + 10][:number1 + 10]
    l = words [number1 + 11][:number1 + 11]
    m = words [number1 + 12][:number1 + 12]
    n = words [number1 + 13][:number1 + 13]
    o = words [number1 + 14][:number1 + 14]
    p = words [number1 + 15][:number1 + 15]
    q = words [number1 + 16][:number1 + 16]
    r = words [number1 + 17][:number1 + 17]
    s = words [number1 + 18][:number1 + 18]
    t = words [number1 + 19][:number1 + 19]
    u = words [number1 + 20][:number1 + 20]
    v = words [number1 + 21][:number1 + 21]
    w = words [number1 + 22][:number1 + 22]
    x = words [number1 + 23][:number1 + 23]
    y = words [number1 + 24][:number1 + 24]
    z = words [number1 + 25][:number1 + 25]
    message1 = themessage.split(",")
    print (message1)
    replace_element()



if __name__ == '__main__':
    readkey()
