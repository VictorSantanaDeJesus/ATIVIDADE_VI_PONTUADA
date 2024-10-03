import os
import time
from dataclasses import dataclass

# DUPLA = 
os.system("cls || clear")
def limpa_terminal():
    os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Habitantes:
    genero: str
    idade_masculino: int
    idade_feminino: int
    salario_masculino: float
    salario_feminino: float

# Lista de de alunos.
lista_de_habitantes = []
lista_genero = []
lista_salario_masculino = []
lista_salario_feminino = []
lista_idade_masculino = []
lista_idade_feminino = []
print("\n=== Solicitando dados dos alunos ===")
while True:
    print("Opções do menu:")
    print("\n1. Adicionar pessoa")
    print("2. Exibir resultados")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
            case 1:
                    while True:
                        genero = input("\nDigite o genêro ('M' para masculino e 'F' para feminino): ").upper().strip()
                        if genero == "M":
                            idade_masculino = int(input("\nDigite a idade"))
                            salario_masculino= float(input("Digite o salário: "))
                            lista_salario_masculino.append(salario_masculino)  
                            break
                        elif genero == "F":
                            idade_feminino = int(input("\nDigite a idade: "))
                            salario_feminino= float(input("Digite o salário: "))
                            lista_salario_feminino.append(salario_feminino)
                            break  
                    habitantes = Habitantes(
                    genero,      
                    idade_masculino,
                    idade_feminino,
                    salario_masculino,
                    salario_feminino
                )
                    lista_de_habitantes.append(habitantes)
                    print ("Dados da família salva com sucesso")

                    for pessoa in lista_de_habitantes:
                        lista_salario_masculino.append(pessoa.salario_masculino)
                        lista_salario_feminino.append(pessoa.salario_feminino)
                        lista_idade_masculino.append(pessoa.idade_masculino)
                        lista_idade_feminino.append(pessoa.idade_feminino)
                        
                        soma_salario = sum (lista_salario_masculino) + sum (lista_salario_feminino)
                        soma_quantidade_salario = len (lista_salario_masculino) + len (lista_salario_feminino)
                        media_salario = soma_salario / soma_quantidade_salario
                        maior_idade = max(lista_idade_masculino, lista_idade_feminino )
                        menor_idade = min(lista_idade_masculino, lista_idade_feminino )







                         
                    limpa_terminal()
            case 2:
                print("\n=== Exibindo resultados ===")  
                print(f"Média de salário da população: {media_salario}")
                print(f"Maior idade da população: {maior_idade}")
                print(f"Menor salário da população: {menor_idade}")
                time.sleep (8)
                limpa_terminal()
            case 3: 
                break        
            case _:  
                print("Opção inválida! Tente novamente.")
                time.sleep(1)
                limpa_terminal()


