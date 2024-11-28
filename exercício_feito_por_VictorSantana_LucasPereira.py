import os
import time
from dataclasses import dataclass

# DUPLA = Victor Santana e Lucas Pereira

os.system("cls || clear")
def limpa_terminal():
    os.system("cls || clear")

# Estrutura de dados
@dataclass
class Habitante:
    genero: str
    idade: int
    salario: float

# Lista
lista_de_habitantes = []
# Variáveis
quantidade_mulheres_5000 = 0
soma_salarios = 0
maior_idade = 0
menor_idade = 99

print("\n=== Solicitando dados dos habitantes ===")
while True:
    print("\nOpções do menu:")
    print("1. Adicionar pessoa")
    print("2. Exibir resultados e sair")
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            while True:
                genero = input("\nDigite o gênero ('M' para masculino e 'F' para feminino): ").upper().strip()
                if genero not in ['M', 'F']:
                    print("Gênero inválido. Tente novamente.")
                    continue

                idade = int(input("Digite a idade: "))
                salario = float(input("Digite o salário: "))

                # Adiciona o habitante na lista
                habitante = Habitante(genero, idade, salario)
                lista_de_habitantes.append(habitante)

                # Atualiza as variáveis de cálculo
                soma_salarios += salario
                if idade > maior_idade:
                    maior_idade = idade
                if idade < menor_idade:
                    menor_idade = idade
                if genero == 'F' and salario >= 5000:
                    quantidade_mulheres_5000 += 1
                
                print("Dados da pessoa salvos com sucesso.")
                break

        case 2:
            if not lista_de_habitantes:
                print("Nenhum dado foi inserido.")
                break

            # Calcula a média de salário
            media_salario = soma_salarios / len(lista_de_habitantes)

            print("\n=== Exibindo resultados ===")  
            print(f"Média de salário da população: R$ {media_salario:.2f}")
            print(f"Maior idade da população: {maior_idade}")
            print(f"Menor idade da população: {menor_idade}")
            print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres_5000}")
            time.sleep(8)
            limpa_terminal()
            break

        case _:  
            print("Opção inválida! Tente novamente.")
            time.sleep(1)
            limpa_terminal()
