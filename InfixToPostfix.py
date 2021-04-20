def prioritas(s):
    if (s=="^"):
        return 2
    elif (s=="*" or s=="/"):
        return 1
    elif (s=="+" or s=="-"):
        return 0
    else:
        return -1

def solve(s):
    stack = []
    s = s.split()
    length = len(s)
    result = ""
    for i in range(length):
        if (len(s[i])>1):
            result+=s[i]+" "
        elif (ord(s[i])>=48 and ord(s[i])<=57) or (ord(s[i])>=65 and ord(s[i])<=91) or ((ord(s[i])>=97) and ord(s[i])<=122):
            result+=s[i]+" "
        elif (s[i]=="("):
            stack.append("(")
        elif (s[i]==")"):
            while (len(stack)>0 and stack[-1]!="("):
                result += stack.pop()+" "
            if (stack[-1]=="("):
                stack.pop()
        else:
            while (len(stack)>0 and prioritas(s[i])<=prioritas(stack[-1])):
                result+=stack.pop()+" "
            stack.append(s[i])
    while (len(stack) > 0):
        result+=stack.pop() + " "
    return result

masukan = input()
hasil = solve(masukan)
print(hasil)