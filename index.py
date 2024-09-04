
saldo = 0
quantidade_saque_realizada = 0
extrato = ""

VALOR_MINIMO_DEPOSITO = 0
LIMITE_SAQUE_DIA = 3
LIMITE_VALOR_SAQUE = 500

menu = """

    [1] Depósito
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

while True:

    operacao = int(input(menu))

    if operacao == 1:
        valor_depositado = int(input("Qual valor do Depósito? "))
        
        # Valores positivos
        if valor_depositado > 0:
            saldo += valor_depositado
            
            extrato += f"Depósito: {valor_depositado:.2f}\n"
            
        else:
            print(f"Valor de Depósito deve ser mair que R${VALOR_MINIMO_DEPOSITO:.2f}.")  
            
        print(f"Saldo atual: R$ {saldo:.2f}")  

    elif operacao == 2:
        valor_saque = float(input("Qual valor do Saque? "))
        
        saque_excetido = quantidade_saque_realizada > LIMITE_SAQUE_DIA
        
        valor_conta_menor_solicitado = valor_saque > saldo
        
        valor_solicitado_maior_permetido = valor_saque > LIMITE_VALOR_SAQUE
        
        autorizado_saque = not (saque_excetido or valor_conta_menor_solicitado or valor_solicitado_maior_permetido)
        
        if saque_excetido:
            print("Quantidade de saques realizadas excedida por dia.")
            
        elif valor_conta_menor_solicitado:
            print("Valor solicitado mair que saldo.")
            
        elif valor_solicitado_maior_permetido:
            print("Valor solicitado maior que permitido por operação.")
            
        elif autorizado_saque:
            saldo -= valor_saque
            quantidade_saque_realizada += 1
            
            extrato += f"Saque: {valor_saque:.2f}\n"
            
            print(f"Saldo atual: R$ {saldo:.2f}")
                
        else:
            print("Houve algum erro interno tente novamente mais tarde.")

    elif operacao == 3:
        print(f"+++++++++++ EXTRATO +++++++++++++")
        print(f"Não houve movimentação financeira até o momento" if not extrato else extrato)
        print(f"SALDO ATUAL: R$ {saldo:.2f}")
        print(f"+++++++++++++++++++++++++++++++++")

    elif operacao == 0:
        break

    else:
        print("Operação inválida, tente novamente!")