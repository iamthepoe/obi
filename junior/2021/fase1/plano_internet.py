limite_inicial = int(input());
limite_atual = limite_inicial;
qtd_meses = int(input());
gasto = [];
i = 0;

while(i<qtd_meses):
    gasto.append(int(input()));
    limite_atual = (limite_atual - gasto[i]) + limite_inicial;
    i = i + 1;

print(limite_atual);