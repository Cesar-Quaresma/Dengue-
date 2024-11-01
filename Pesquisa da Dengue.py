print("\033[1:39m Trata-se de uma pesquisa para realizar o combate contra a \033[1:37mDengue\033[1:39m, independente da região. \nVamos expor quantas pessoas, entre homens e mulheres que contraíram a doença mas, com o foco de manter naquela \nregião específica, os cuidados necessários para a eliminação do vírus\033[1:34m Aedes Aegypti\033[1:39m:")

resp = ''
semhomem = 0
semmulher = 0
denguehomem = 0
denguemulher = 0

while resp in 'Ss':
    nome = str(input("Qual o seu nome? ")).title()
    região = str(input("Região dessa pessoa: ")).title()
    sexo = str(input("Sexo M/F: ")).upper()
    dengue = str(input("O(a) senhor(a) já teve com Dengue? S/N ")).upper()
    if sexo in 'Mm':
        if dengue in 'Ss':
            denguehomem += 1
            print(f"\033[1:37m{nome}\033[1:39m já teve \033[1:37mDengue\033[1:39m! \033[1:31mAlerta de segurança \033[1:39mna região de \033[1:37m{região}\033[1:39m. ")
        elif dengue in 'Nn':
            semhomem += 1
            print(f"{nome} \033[1:36mnão teve Dengue.\033[1:34m Obrigado pela colaboração!\033[1:39m")
        else:
            print("Erro na operação. Tente novamente!")
    elif sexo in 'Ff':
        if dengue in 'Ss':
            denguemulher += 1
            print(f"\033[1:37m{nome}\033[1:39m já teve \033[1:37mDengue\033[1:39m! \033[1:31mAlerta de segurança \033[1:39mna região de \033[1:37m{região}\033[1:39m.")
        elif dengue in 'Nn':
            semmulher += 1
            print(f"{nome}\033[1:36m não teve Dengue.\033[1:34mObrigado pela colaboração!\n")
    else:
        print("Erro na operação. Tente novamente!")
    if dengue in 'Ss':
        tempodengue = int(input("Tempo (em anos) que essa pessoa pegou Dengue: "))
    else:
        print(f"{nome} \033[1:36mestá livre\033[1:39m! \033[1:33mSe dirija (você pesquisador) para outra região.\033[1:39m")
    resp = str(input("Deseja continuar? ")).upper()
print(f"\nA quantidade de homens que \033[1:31mcontraíram Dengue\033[1:39m foram de cerca de: \033[1:32m{denguehomem} homens\033[1:39m, em relação aos que \033[1:36mnão contraíram\033[1:39m \nforam de: \033[1:32m{semhomem} homens\033[1:39m.")
print(f"Os números, entre mulheres que \033[1:31mcontraíram Dengue\033[1:39m ficaram de: \033[1:32m{denguemulher}\033[1:39m, em relação à outras que \033[1:36mnão contraíram\033[1:39m, \nforam entre: \033[1:32m{semmulher} mulheres\033[1:39m.")
