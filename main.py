from io import open

def transposition_encryption():
    
    # Read file
    txtFile = open('message.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

    # Delete special characters
    final_plain_text = ""
    for pt in plain_text:
        if pt.upper() in alphabet:
            final_plain_text += pt.upper()
        else:
            if pt == " ":
                final_plain_text += " "
            else:
                final_plain_text += ""
            


    print("\n\n========== Plain text ==========\n\n", final_plain_text)

    msg = final_plain_text.replace(" ", ",")

    # print(msg)
    key = input("\n---------- Transposition keyword: ").upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    print("\n\n========== Transposition grid ==========\n\n")
    # printing key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print("\n-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "."
    # if

    # print(msg)

    num_of_rows = int(len(msg) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)
    
    # cipher
    cipher_text = ""
    k = 0
    for i in range(len(key)):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1
    # for

    print("\n\n========== Final Text Encrypted ==========\n\n")
    print(cipher_text)

    # Create output file
    outputFile = open('message_encrypt.txt','w')
    outputFile.write(cipher_text)
    outputFile.close() 
    print("\n\n========== Check message_encrypt.txt file ==========\n\n")

def transposition_decryption():

    # Read file
    txtFile = open('message_encrypt.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    tws = ""
    for fc in fileContent:
        tws += fc.replace("\n", " ").upper()

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890.,"

    # Replace returns by spaces
    encrypted_text = ""
    for fc in tws:
        if fc.upper() in alphabet:
            encrypted_text += fc.upper()
        else:
            encrypted_text += ""

    print("\n\n========== Encrypted text ==========\n\n", encrypted_text)

    msg = encrypted_text
    # print(msg)
    key = input("\n---------- Transposition keyword: ").upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(msg) / len(key))

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
        # for
    # for

    print("\n\n========== Decrypted text ==========\n\n")
    print(plain_text.replace(","," ").replace(".",""))
    print("\n\n")

def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key)):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFG"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init - 1
            # if
        # inner for
    # for
    return kywrd_num_list

def main():
    
    option = int (input("\n\n========== Choose an option ==========\n1) Encrypt \n2) Decrypt\n\n"))

    if option == 1:
        transposition_encryption()
    elif option == 2:
        transposition_decryption()
    else:
        print("Incorrect option")

if __name__ == "__main__":
    main()