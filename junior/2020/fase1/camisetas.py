qtd_premiados = int(input())
lista = input().split();

P = int(input());
M = int(input());

if(P == lista.count("1") and M == lista.count("2")):
    print("S")
else:
    print("N")
