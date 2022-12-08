# Encryption
def vigenere_encrypt(plain_text, key):

    plain_text = plain_text.upper()
    key = key.upper()
    key = list(key)
    
    #to verify the plaintext and key are the same 
    if(len(plain_text) != len(key)):
        for x in range (0, len(plain_text) - len(key)):
            key.append(key[x])

    x = 0
    cipher_text = []
    for x in range (len(plain_text)): # iterate thorugh each character in the message   
        if(ord(plain_text[x]) == 32): #checks for spacing
            cipher_text.append(" ")
        else:
            index = ((ord(plain_text[x]) + ord(key[x])) % 26) + 65 #encryption algorithm plus the addition of ASCII value 'A'
            cipher_text.append(chr(index))

    return ("".join(cipher_text))

#Decryption 
def vigenere_decrypt(cipher_text, key):

    cipher_text = cipher_text.upper()
    key = key.upper()
    
    key = list(key)
    
    #to verify the plaintext and key are the same 
    if(len(cipher_text) != len(key)):
        for x in range (0, len(cipher_text) - len(key)):
            key.append(key[x])

    x = 0
    plain_text = []
    for x in range (len(cipher_text)):
        
        if(ord(cipher_text[x]) == 32): 
            plain_text.append(" ")
        else:
            index = ((ord(cipher_text[x]) - ord(key[x])) % 26) + 65 #decryption algorithm plus the addition of ASCII value 'A'
            plain_text.append(chr(index))

    return ("".join(plain_text))
	


if __name__ == "__main__":
	#main()
	
    plain_text = input("Enter: TO BE OR NOT TO BE THAT IS THE QUESTION \n")
    key = input("Enter: RELATIONS \n")
    cipher_text = vigenere_encrypt(plain_text, key)
    print("Encrypted message: ",cipher_text)
    plain_text = vigenere_decrypt(cipher_text, key)
    print("Decrypted message: ", plain_text)
    
