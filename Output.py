def main():   #creating the main function for encryption and decryption
    option=0
    while option!=9:
        print("VIGENERE CIPHER\n")
        option=menu()
        if option==1:
            print("ENCRYPTING TEXT...\n")
            encrypt_vigenere()
            print("\nDONE!")
        elif option==2:
            print("DECRYPTING TEXT...\n")
            decrypt_vigenere()
            print("\nDONE!")
        elif option==9:
            break


def menu(): #Creating the menu function to prompt the user whether not they would like to encrypt or decrypt a text

    option=0

    while option!=1 and option!=2 and option!=9:

        menu="""
        Selection Operation:
        1) to encrypt
        2) to decrypt
        9) Quit
        """
        option=int(input(menu))
        if option==1:
            continue
        elif option==2:
            continue
        elif option==9:
            continue
        else:
            print("Invalid option. Try again.")

    return option

def adjusted_key(text,key): #function creating the encryption key for the encrypting process
    count=0
    length_text=len(text)
    adjusted=""
    while len(key) <= length_text:
        key+=key
    for i in range(length_text):
        if text[i]==" ":
            count+=1
    if count>0:
        adjusted=key[:len(text)-count]
    else:
        adjusted=key[:len(text)]
    return adjusted


def encrypt_vigenere(): #Encrpytion function
    filename_einput=input("Please enter the name of a file containing the text to be encrypted: ")
    textFile=open(filename_einput,'r')
    text=textFile.read()
    textFile.close()
    space_index=[k for k, x in enumerate(text) if x==' ']
    new_text=text.lower().replace(' ','')
    forText=new_text
    encrpyt_text=""
    key=input("Please enter an encoding key: ")
    adjusted=adjusted_key(text,key)

    for i  in range(len(new_text)):

        if ord(forText[i])>=97 and ord(forText[i])<=122:
            shift=ord(adjusted[i])-97
            if shift+ord(new_text[i])>122:
                order=ord(new_text[i])-97
                new_order=shift+order
                remainder=new_order%26
                new_character=chr(remainder+97)
                encrpyt_text="".join([new_text[:i], new_character, new_text[i+1:]])
                new_text=encrpyt_text

            else:
                new_character=chr(shift+ord(new_text[i]))
                encrpyt_text="".join([new_text[:i], new_character, new_text[i+1:]])
                new_text=encrpyt_text

        elif ord(forText[i])<97 and ord(forText[i])>122:

            encrypt_text="".join([new_text[:i],new_text[i+1:]])
            new_text=encrpyt_text

    for respace in space_index:
        new_text=new_text[:respace]+ ' '+new_text[respace:]
    filename_eoutput=input("Please enter the name for the output file (must be .txt): ")
    encrypt_result=open(filename_eoutput,'w')
    encrypt_result.write(new_text)
    encrypt_result.close()


def decrypt_vigenere(): #Decryption function
    filename_dinput=input("Please enter a filename containing the decrypted text: ")
    eFile=open(filename_dinput,'r')
    new_text=eFile.read()
    eFile.close()
    space_index=[k for k, x in enumerate(new_text) if x==' ']
    new_text=new_text.replace(' ','')
    forText=new_text
    decrypt_text=""
    key=input("Please enter a decoding key: ")
    adjusted=adjusted_key(new_text,key)

    for i  in range(len(new_text)):

        if ord(forText[i])>=97 and ord(forText[i])<=122:
            shift=ord(adjusted[i])-97
            if ord(new_text[i])-shift<97:
                order=ord(new_text[i])-97
                new_order=order-shift
                new_order+=26
                remainder=new_order%26
                new_character=chr(remainder+97)
                decrpyt_text="".join([new_text[:i], new_character, new_text[i+1:]])
                new_text=decrpyt_text

            else:
                new_character=chr(ord(new_text[i])-shift)
                decrpyt_text="".join([new_text[:i], new_character, new_text[i+1:]])
                new_text=decrpyt_text

        elif ord(forText[i])<97 and ord(forText[i])>122:

            decrypt_text="".join([new_text[:i],new_text[i+1:]])
            new_text=decrpyt_text

    for respace in space_index:
        new_text=new_text[:respace]+ ' '+new_text[respace:]
    filename_doutput=input("Please enter the name for the output file (must be .txt): ")
    dFile=open(filename_doutput,'w')
    dFile.write(new_text)
    dFile.close()
main()
