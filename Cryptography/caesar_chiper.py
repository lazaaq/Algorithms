# input the text (alphabet, uppercase or lowercase)
plain_text = input()
# input the caesar chiper shift (negative = to the left, positive = to the right)
shift = int(input())

res = ""  # result declaration

for i in plain_text:  # iterate through plain text
    ordo = ord(i)  # ascii number of alphabet
    if ordo >= 65 and ordo <= 90:  # if uppercase
        ordo += shift  # add the ordo with the shift
        # if ordo is lower than 65 (whiches the minimum ascii of uppercase letter)
        if ordo < 65:
            ordo += 26  # then add 26 (number of alphabet)
        # if ordo is higher than 97 (whiches the maximum ascii of lowercase letter)
        elif ordo > 97:
            ordo -= 26  # then substract 26
    elif ordo >= 97 and ordo <= 122:  # if lowercase
        ordo += shift
        if ordo < 97:
            ordo += 26
        elif ordo > 122:
            ordo -= 26
    res += chr(ordo)  # fill up the result

print(res)
