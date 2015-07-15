import re
import pprint
import itertools

#converts the message into capitals and removes special charaters and numbers
#split double letters and add X by taking the index
#removes space by taking the index to replace
def cleanMsg(message):
    index=[]
    spindex=[]
    message = message.upper()
    message = re.sub('[^A-Za-z]+', ' ', message)
    for i in range(0,len(message)-1):
        if(message[i]==" "):
            spindex.append(i)
    message=message.replace(" ","")
    for i in range(0,len(message)-1):
        if(message[i]==message[i+1]):
            index.append(i+1)
    message=re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', message)
    if(len(message)%2!=0):
        message=message+"X"
    return (message,index,spindex)
    
#generates playfair matrix by replacing 'j' with 'i' 
def playfairMatrix(key):
    key=key.replace(" ","")
    key=key+"abcdefghijklmnopqrstuvwxyz"
    key=key.upper()
    key=key.replace("J","I")
    key=re.sub('[^A-Za-z]+', ' ',key)
    genKey=[]
    seen=set()
    for char in key:
        if char not in seen: 
            seen.add(char)
            genKey.append(char)
    matrix = [[0 for x in range(5)] for x in range(5)]
    count=0
    for i in range(0,5):
        for j in range(0,5):
            matrix[i][j]=genKey[count]
            count+=1
    return matrix

#caluculates the cipher text for two characters at a time
#caluculates seperately for encryption and decryption  
def validation(a,b,matrix,choice):
    col1=0
    col2=0
    row1=0
    row2=0
    for w in range(0,5):
        for x in range(0,5):
            if(a==matrix[w][x]):
                col1=x
                row1=w
            elif(b==matrix[w][x]):
                col2=x
                row2=w
    #encryption            
    if((col1==col2) and (choice==1)):
        row1=(row1+1)%5
        row2=(row2+1)%5
    elif((row1==row2) and (choice==1)):
        col1=(col1+1)%5
        col2=(col2+1)%5
    #decryption    
    elif((col1==col2) and (choice==2)):
        row1=(row1-1)%5
        row2=(row2-1)%5
    elif((row1==row2) and (choice==2)):
        col1=(col1-1)%5
        col2=(col2-1)%5
    else:
        temp=col1
        col1=col2
        col2=temp
    return (row1,col1,row2,col2)    

#replace the spaces and removes 'X' near double letters by using the index arrays for both spaces and double letters
def replacing(ind,spind,cnvrttext):
    for z in range(0,len(cnvrttext)-1):
        for y in range(0,len(ind)):
            if(z==ind[y]):
                cnvrttext=cnvrttext[:z] + cnvrttext[z+1:]
    
    for z in range(0,len(cnvrttext)-1):
        for y in range(0,len(spind)):
            if(z==spind[y]):
                cnvrttext=cnvrttext[:z]+" " + cnvrttext[z:]
    print(cnvrttext)

#Gets the encrypted or decrypted message
def convertedText(message,matrix,choice):
    cnvrttext=""
    for w in range(0,len(message)-1):
        if((w%2)==0):
            a=message[w]
            b=message[w+1]
            row1,col1,row2,col2=validation(a,b,matrix,choice)
            cnvrttext=cnvrttext+matrix[row1][col1]
            cnvrttext=cnvrttext+matrix[row2][col2]
    return cnvrttext

# Encryption function
def encrypt():
    print("Enter your message:")
    message=input()
    print("Enter the key to encrypt with : ")
    key=input()
    message,ind,spind=cleanMsg(message)
    matrix=playfairMatrix(key)
    choice=1
    cnvrttext=convertedText(message,matrix,choice)
    print("The encrypted message is:")
    print(cnvrttext)
    print("do u wish to decrypt the message.press y")
    ch=input()
    if(ch=='y'):
        cnvrttext=decrypt()
        print(cnvrttext)
        print(ind)
        print(spind)
        replacing(ind,spind,cnvrttext)

# Decryption function    
def decrypt():
    print("Enter Cipher text to decrypt :")
    message=input()
    print("Enter the key to decrypt :")
    key=input()
    matrix=playfairMatrix(key)
    choice=2
    cnvrttext=convertedText(message,matrix,choice)
    return cnvrttext
    
#************start********************
print ("Enter your option")
print ("1.Encrypting.    2.Decrypting")
n = input()
flag=1
while(flag==1):
    if(n=='1'):
        encrypt()
        flag=0
    elif(n=='2'):
        cnvrttext=decrypt()
        print("The decrypted message is:")
        print(cnvrttext)
        print("press 'y' if you have index arrays for space and double letters")
        opt=input()
        if(opt=='y'):
            print("enter the index values spaces") 
        print("Bye")
        flag=0
    else:
        print("Improper Entry")
        print ("Enter your option")
        print ("1.Encrypting. , 2.Decrypting")
        n = input()