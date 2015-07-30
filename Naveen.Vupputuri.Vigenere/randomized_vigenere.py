#****************************Program-2:Vigenere Cipher **************************
#Name :Naveen Sai Vupputuri
#Program Description :This programs builds a random vigenere matrix by using
#		seed and generates an alphabetic key from the seed to encrypt a plainText
#       using that key.And similarly it decrypts the cipher text by building the
#       same matrix and by using the same seed.			  	
#********************************************************************************


import random
seed=0
symbols ="""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

#This function shuffles the the 'symbols' string using the seed and then inserts 
#      each char of the string into 95*95 matrix by placing without the repetition
#      of same char in a row or a column
def vigenereTabulo(symbols,seed):
    random.seed(seed)
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    table = [[0 for i in range(len(symbols))] for i in range(len(symbols))]
    l=len(symbols)
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(l):
            r = random.randrange(l)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(l)
            
                myList.append(r)
                               
            while(table[i][r] != 0):
                r = (r + 1) % l
            
            table[i][r] = sym
    return table

#This function takes the integer 'seed'	as an input and generates a alphabetic string
#     from that number by taking modulo of 100 each time and find out the char for the 
#     ascii value.
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)
    
#def seedGeneration(vigenereKey):
#    num=0
#    for i in range(len(vigenereKey,0)):
#        num=


#This function first generates the key using keyFromSeed() function, builds vigenere 
#    table then find encrypts each char of the plain text using single char of the 
#    and find out the value that is present in the row of key and the column of message.
def encrypt(plainText,seed):
    key=keywordFromSeed(seed)
    tab=vigenereTabulo(symbols,seed)
    cipherText=[]
    x=[tab[i][0] for i in range(len(symbols))]
    for i in range(len(plainText)):
        cipherText.append(tab[x.index(key[i%len(key)])][tab[0].index(plainText[i])])
    cipherText=''.join(cipherText)
    return cipherText
    
#This function operates same as encryption generates the key,builds the vigenere table
#    but decrypts each char of cipher text using single char key and finds out the char
#    that is present in the 0th row of cipher text column.
def decrypt(cipherText,seed):
    #seed=seedGeneration(vigenereKey)
    key=keywordFromSeed(seed)
    tab=vigenereTabulo(symbols,seed)
    message=[]
    x=[tab[i][0] for i in range(len(symbols))]
    for i in range(len(cipherText)):
        row=x.index(key[i%len(key)])
        message.append(tab[0][tab[row].index(cipherText[i])])
    message=''.join(message)
    return message
        