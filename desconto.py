nome = input("Qual seria seu nome")
mes = int(input("que mês você fez a compra"))
valor_compra = float(input("qual foi o valor da sua compra R$"))
desconto = 10
cupom_de_desconto = "É10"

print(f"Olá, {nome} sua compra foi realizada no mês {mes} com sucesso valor {valor_compra} e ganhou um desconto de {desconto} em sua próxima compra. Use o cupom {nome}{cupom_de_desconto}")