def caesar_cipher(chiffre, msg) :
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    pivoter = alphabet.copy()
    
    while chiffre != 0 :
            retenu = pivoter[0]
            for i in range (25) :
                pivoter[i] = pivoter[i + 1]
            chiffre -= 1
            pivoter[25] = retenu
    print(pivoter)

    result = ""

    for char in msg:
        if char != " ":
            upper_char = char.upper()
            if upper_char in alphabet:
                position = alphabet.index(upper_char)
                new_char = pivoter[position]
                result += new_char.lower() if char.islower() else new_char.upper
    print("encripted message : ", result)

chiffre = int(input("choisissez un chiffre : "))
msg = input("Type in something to encode : ")

caesar_cipher(chiffre, msg)