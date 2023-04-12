i = 0;
vitorias = 0;

while(i<6):
    resultado = input();
    if(resultado == "V"):
        vitorias = vitorias + 1;

    i = i + 1;

if(vitorias == 1 or vitorias == 2):
    print(3);
elif (vitorias == 3 or vitorias == 4):
    print(2);
elif (vitorias == 5 or vitorias == 6):
    print(1);
else:
    print(-1);