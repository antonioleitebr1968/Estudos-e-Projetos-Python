nome = input("Informe seu nome: ")
sexo = input("Informe o sexo 'M' para Masculino e "
 "'F' para Feminino: ")[0].upper()
if sexo != "M" and sexo != "F":
 print("Opção inválida.")
 exit()
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))
imc = (peso)/(altura*altura)
if sexo == "M":
     if imc < 20.7:
        condicao = "Abaixo do peso"
     elif imc <= 26.4:
        condicao = "No peso normal"
     elif imc <= 27.8:
        condicao = "Marginalmente acima do peso"
     elif imc <= 31.1:
        condicao = "Acima do peso ideal"
     else:
        condicao = "Obeso"
elif sexo == "F":
    if imc < 19.1:
        condicao = "Abaixo do peso"
    elif imc <= 25.8:
        condicao = "No peso normal"
    elif imc <= 27.3:
     condicao = "Marginalmente acima do peso"
    elif imc <= 32.3:
        condicao = "Acima do peso ideal"
    else:
        condicao = "Obeso"
print(f"{nome}, com base no peso e altura informados, "
 f"o IMC é {imc:.1f} e a condição é '{condicao}'.")
