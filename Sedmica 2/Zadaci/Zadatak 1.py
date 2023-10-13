zvj = "*"
jedn = "="
for i in range(1, 11):
    for j in range(1, 11):
        if j == 10:
            print(f"{str(i)+zvj+str(j)+jedn+str(i*j):^10} *|*")
            break
        print(f"{str(i)+zvj+str(j)+jedn+str(i*j):^10} *|*", end="")
    print(f"___________*|*"*10)
