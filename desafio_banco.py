menu =  """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
     opcao = input (menu)
     
     if opcao == "d":
         valor = float(input("Digite o valor a ser depositado: "))
         if valor > 0:
             saldo += valor
             extrato += f"Depósito: R$ {valor:.2}\n"
         else:
             print("Valor inválido")    

     elif opcao == "s":
         valor = float(input("Digite o valor a ser sacado: "))
         
         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saques >= LIMITE_SAQUES
         
         if excedeu_saldo:
             print("Saldo insuficiente")
         elif excedeu_limite:
             print("Limite insuficiente")
         elif excedeu_saques:
             print("Limite de saques excedido")
         elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2}\n"
             numero_saques += 1
         else:
             print("Valor inválido")    
                     
     elif opcao == "e":
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movioentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2}")
        print("===============================================")
        
     elif opcao == "q":
        print("Sair")
        break
     else:
        print("Opção inválida")