from datetime import date 

dt_atual = date.today().year
dt_contratacao = int(input("Digite o ano de contratação: "))
salario_inicial = float(input("Digite o salário inicial: "))

if dt_contratacao <= 1995 or dt_contratacao > dt_atual or salario_inicial < 1000:
    print("Você não possui aumento...")
    print(f"\nSalário: R${salario_inicial:,.2f}")
else:
    anos_trabalhando = dt_atual - dt_contratacao
    cont = 0
    perc_aumento = 0.0
    salario_final = salario_inicial
    
    while cont < anos_trabalhando:
        if cont > 0:
            perc_aumento += perc_aumento * 0.1
        else:
            perc_aumento = 0.015
        salario_final += salario_final * perc_aumento
        cont += 1
        
        
    print(f"\nAno de contratação: {dt_contratacao}")
    print("Salário anterior: R$", round(salario_inicial, 2))
    print("Salário atual: R$", round(salario_final, 2))
    perc_salario_inicial = (salario_final * 100) / salario_inicial
    print(f"Percentual de aumento: {(perc_salario_inicial - 100):,.2f}%")

    

