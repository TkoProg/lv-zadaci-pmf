def zagrade(s):
    otvorena = 0
    zatvorena = 0
    for i in range(len(s)):
        if s[i] == "(":
            otvorena += 1
        if s[i] == ")":
            zatvorena += 1
        if zatvorena > otvorena:
            return False
    return True


print(zagrade("))()()(())"))
