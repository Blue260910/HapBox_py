import requests
import json
from tabulate import tabulate

def main():
    print("____________________________________________")
    print("  ＡＴＵＡＬＩＺＡＣＡＯ ＤＥ ＰＬＡＮＯＳ    ")
    print("____________________________________________")

    url = "https://hapbox-f9157-default-rtdb.firebaseio.com"
    response = requests.get(url + '/.json')

    # Se a solicitação foi bem-sucedida, response.status_code será 200
    if response.status_code == 200:
        data = response.json()
        while True:
            print("1. Atualizar por nome")
            print("2. Atualizar por email")
            print("3. Atualizar por ID")
            print("4. Sair")
            print("____________________________________________")
            escolha = input("Digite sua escolha: ")
            if escolha == '1':
                nome_para_atualizar = input("Digite o nome: ")
                for key, item in data.items():
                    if 'Name' in item and item['Name'] == nome_para_atualizar:
                        print("Dados atuais: ")
                        current_data_table = [["Medicamentos", item.get("Medicamentos", "")], ["Doses", item.get("Doses", "")], ["Horarios", item.get("Horarios", "")], ["QuantidadeComprimidos", item.get("QuantidadeComprimidos", "")]]
                        print(tabulate(current_data_table, headers='firstrow', tablefmt='fancy_grid'))

                        update_url = url + '/' + key + '.json'
                        medicacao = input("Digite os medicamentos (separados por vírgula): ").split(',')
                        doses = list(map(int, input("Digite as doses (separadas por vírgula): ").split(',')))
                        horarios = input("Digite os horários no formato 00:00 (separados por vírgula) : ").split(',')
                        quantidadeComprimidos = list(map(int, input("Digite a quantidade de comprimidos (separados por vírgula): ").split(',')))
                        update_data = {"Medicamentos": medicacao, "Doses": doses, "Horarios": horarios, "QuantidadeComprimidos": quantidadeComprimidos}

                        # Create a table with tabulate
                        table = [["Medicamentos", medicacao], ["Doses", doses], ["Horarios", horarios], ["QuantidadeComprimidos", quantidadeComprimidos]]
                        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

                        update_response = requests.patch(update_url, json=update_data)
                        if update_response.status_code == 200:
                            print("Atualizado com sucesso")
                        else:
                            print("Falha ao atualizar", update_response.status_code)
            elif escolha == '2':
                email_para_atualizar = input("Digite o email: ")
                for key, item in data.items():
                    if 'Email' in item and item['Email'] == email_para_atualizar:
                        print("Dados atuais: ")
                        current_data_table = [["Medicamentos", item.get("Medicamentos", "")], ["Doses", item.get("Doses", "")], ["Horarios", item.get("Horarios", "")], ["QuantidadeComprimidos", item.get("QuantidadeComprimidos", "")]]
                        print(tabulate(current_data_table, headers='firstrow', tablefmt='fancy_grid'))

                        update_url = url + '/' + key + '.json'
                        medicacao = input("Digite os medicamentos (separados por vírgula): ").split(',')
                        doses = list(map(int, input("Digite as doses (separadas por vírgula): ").split(',')))
                        horarios = input("Digite os horários no formato 00:00 (separados por vírgula) : ").split(',')
                        quantidadeComprimidos = list(map(int, input("Digite a quantidade de comprimidos (separados por vírgula): ").split(',')))
                        update_data = {"Medicamentos": medicacao, "Doses": doses, "Horarios": horarios, "QuantidadeComprimidos": quantidadeComprimidos}

                        # Create a table with tabulate
                        table = [["Medicamentos", medicacao], ["Doses", doses], ["Horarios", horarios], ["QuantidadeComprimidos", quantidadeComprimidos]]
                        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

                        update_response = requests.patch(update_url, json=update_data)
                        if update_response.status_code == 200:
                            print("Atualizado com sucesso")
                        else:
                            print("Falha ao atualizar", update_response.status_code)
            elif escolha == '3':
                id_para_atualizar = input("Digite o ID: ")
                for key, item in data.items():
                    if 'ID' in item and str(item['ID']) == id_para_atualizar:
                        print("Dados atuais: ")
                        current_data_table = [["Medicamentos", item.get("Medicamentos", "")], ["Doses", item.get("Doses", "")], ["Horarios", item.get("Horarios", "")], ["QuantidadeComprimidos", item.get("QuantidadeComprimidos", "")]]
                        print(tabulate(current_data_table, headers='firstrow', tablefmt='fancy_grid'))

                        update_url = url + '/' + key + '.json'
                        medicacao = input("Digite os medicamentos (separados por vírgula): ").split(',')
                        doses = list(map(int, input("Digite as doses (separadas por vírgula): ").split(',')))
                        horarios = input("Digite os horários no formato 00:00 (separados por vírgula) : ").split(',')
                        quantidadeComprimidos = list(map(int, input("Digite a quantidade de comprimidos (separados por vírgula): ").split(',')))
                        update_data = {"Medicamentos": medicacao, "Doses": doses, "Horarios": horarios, "QuantidadeComprimidos": quantidadeComprimidos}

                        # Create a table with tabulate
                        table = [["Medicamentos", medicacao], ["Doses", doses], ["Horarios", horarios], ["QuantidadeComprimidos", quantidadeComprimidos]]
                        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

                        update_response = requests.patch(update_url, json=update_data)
                        if update_response.status_code == 200:
                            print("Atualizado com sucesso")
                        else:
                            print("Falha ao atualizar", update_response.status_code)
            elif escolha == '4':
                break
            else:
                print("Escolha inválida. Por favor, digite 1, 2, 3 ou 4.")
    else:
        print("Falha ao obter dados do Firebase", response.status_code)

if __name__ == '__main__':
    main()