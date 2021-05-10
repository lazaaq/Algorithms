def isOperand(x):
    if x.isnumeric():
        return True
    elif (ord(x) >= 65 and ord(x) <= 91) or (ord(x) >= 97 and ord(x) <= 122):
        return True
    return False


def getInfix(exp):
    s = []
    list_exp = exp.split()
    for i in range(len(list_exp)):
        if isOperand(list_exp[i]):
            s.append(list_exp[i])
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.append("("+op2+list_exp[i]+op1+")")
    return s[0]


user_input = input()
result = getInfix(masukan)
print(result)
