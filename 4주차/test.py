def reverse(str):
    if (len(str)== 0 or len(str) ==1):
        return str
    else:
        r= reverse(str[1:])+str[0]
        return r
s1='Hello world!'

print(reverse(s1))
