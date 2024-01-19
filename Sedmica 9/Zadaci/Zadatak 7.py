def ispisi_koordinate(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print(f"({i},{j})", end = " ")
        print()

def cik_cak(m):
    n = len(m)
    d = 2 * n - 1
    sve_dijagonale = []
    ispisi_koordinate(m)
    for i in range(n):
        dijagonala = []
        for red in range(i+1):
            kolona = i - red
            dijagonala.append(m[red][kolona])
        sve_dijagonale.append(dijagonala)
        print(dijagonala)

    for i in range(n, d):
        dijagonala = []
        for kolona in range(n-1, i-(n-1)-1, -1):
            red = i - kolona
            dijagonala.append(m[red][kolona])
        sve_dijagonale.append(dijagonala)
        print(dijagonala)

    for i in range(len(sve_dijagonale)):
        dijagonala = sve_dijagonale[i]
        if i % 2 == 0:
            dijagonala.reverse()
        for e in dijagonala:
            print(e, end= " ")


m = [[1, 5, 3, 2],[2, 3, 7, 9],[7, 10, 8, 1],[9, 5, 1, 3]]
cik_cak(m)
