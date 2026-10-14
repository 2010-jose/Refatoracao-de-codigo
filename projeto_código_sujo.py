import random
import time
import os

def random_number():
    interval = int(input("Escolha um número: ")) + 1

    print("O computador vai escolher um número de 0 a", (interval - 1))

    time.sleep(4)

    print("Número escolhido: ", random.randint(1, interval))

    print("1- Sair")
    print("2- Continuar")
    now_choice1 = input("O que quer fazer agora? ")
    if now_choice1 == "1":
        home()
    elif now_choice1 == "2":
        random_number()

def random_password():
    my_length = int(input("Insira o tamanho da senha randômica: "))
    characters = 'abcdefgijklmnopqrstuvwxyz0123456789+-:*/?;.,<>_#@!%$'
    charc_list = list(characters)

    randomic_password = ''

    for z in range(my_length):
        randomic_password += random.choice(charc_list)

    print("Sua senha gerada: ", randomic_password)

    print("1- Sair")
    print("2- Continuar")
    now_choice2 = input("O que quer fazer agora? ")
    if now_choice2 == "1":
        home()
    elif now_choice2 == "2":
        random_password()

def clock():
    try:
        print("Pressione CTRL+C para parar o relógio")

        time.sleep(3)

        while True:
            h = time.localtime()

            print(f"\rHorário: {h.tm_hour}:{h.tm_min}:{h.tm_sec}", end="")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Relógio parado!")

        print("1- Sair")
        print("2- Continuar")
        now_choice3 = input("O que quer fazer agora? ")
        if now_choice3 == "1":
            home()
        elif now_choice3 == "2":
            clock()

def simple_calc():
    print(eval(input("Digite uma expressão numérica a ser resolvida: ")))

    print("1- Sair")
    print("2- Continuar")
    now_choice4 = input("O que quer fazer agora? ")
    if now_choice4 == "1":
        home()
    elif now_choice4 == "2":
        simple_calc()

def percent_calc():
    quant = int(input("Quantos números você quer inserir? "))

    list = []

    for i in range(quant):
        i = int(input("Insira um número: "))
        list.append(i)

    total = sum(list)

    for a in range(len(list)):
        selected = list[a]
        percent = selected * 100 / total
        print(f"Porcentagem de {selected} em relação ao total ({total}): {percent:.1f}%")

    print("1- Sair")
    print("2- Continuar")
    now_choice5 = input("O que quer fazer agora? ")
    if now_choice5 == "1":
        home()
    elif now_choice5 == "2":
        percent_calc()

def home():
    print("1- Sorteador de número")
    print("2- Gerador de senha")
    print("3- Relógio")
    print("4- Calculadora simples")
    print("5- Calculadora de porcentagem")
    print("6- Desligar sistema")

    home_choice = input("Qual software deseja acessar? (1, 2, 3, 4, 5, ou 6) ")

    match home_choice:
        case "1":
            random_number()
        case "2":
            random_password()
        case "3":
            clock()
        case "4":
            simple_calc()
        case "5":
            percent_calc()
        case "6":
            print(">>> Desligando o sistema <<<")
            time.sleep(3)
            exit()

while True:
    home()