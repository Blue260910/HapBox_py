import requests
import json
from tabulate import tabulate

def main():
    url = "https://hapbox-f9157-default-rtdb.firebaseio.com/.json"
    response = requests.get(url)

    # Se a solicitação foi bem-sucedida, response.status_code será 200
    if response.status_code == 200:
        data = response.json()

        info_list = []

        # Iterar sobre os dados e criar um dicionário para cada item
        for item in data.values():
            if 'Name' in item and 'Email' in item and 'ID' in item:
                info_dict = {'Name': item['Name'], 'Email': item['Email'], 'ID': item['ID']}
                info_list.append(info_dict)

        # Formatar a lista de dicionários como uma tabela
        print(tabulate(info_list, headers="keys", tablefmt='fancy_grid'))

        while True:
            print("1 - Pesquisar por Nome")
            print("2 - Pesquisar por Email")
            print("3 - Pesquisar por ID")
            print("4 - Sair")
            choice = input("Digite sua escolha: ")
            results = []
            if choice == '1':
                name_to_search = input("Digite o nome: ")
                for item in data.values():  # Iterar sobre os valores do dicionário externo
                    if 'Name' in item and item['Name'] == name_to_search:
                        results.append(item)
            elif choice == '2':
                email_to_search = input("Digite o email: ")
                for item in data.values():  # Iterar sobre os valores do dicionário externo
                    if 'Email' in item and item['Email'] == email_to_search:
                        results.append(item)
            elif choice == '3':
                id_to_search = input("Digite o ID: ")
                for item in data.values():  # Iterar sobre os valores do dicionário externo
                    if 'ID' in item and str(item['ID']) == id_to_search:
                        results.append(item)
            elif choice == '4':
                break
            else:
                print("Por favor, utilize 1, 2, 3 ou 4.")
            
            if results:
                print(tabulate(results, headers="keys", tablefmt='fancy_grid' ))
            else:
                print("Nenhum resultado encontrado.")
    else:
        print("Falha ao obter dados do Firebase", response.status_code)

if __name__ == "__main__":
    main()