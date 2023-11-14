import requests
import json

def main():

    url = "https://hapbox-f9157-default-rtdb.firebaseio.com"
    response = requests.get(url + '/.json')

    # Se a solicitação foi bem-sucedida, response.status_code será 200
    if response.status_code == 200:
        data = response.json()
        while True:
            print("1 - Deletar por nome")
            print("2 - Deletar por email")
            print("3 - Deletar por ID")
            print("4 - Sair")
            escolha = input("Digite sua escolha: ")
            if escolha in ['1', '2', '3']:
                if len(data) <= 3:
                    print("Não é possível deletar. Menos de 3 registros existentes.")
                    return
                confirmacao = input("Tem certeza que deseja deletar? (s/n): ")
                if confirmacao.lower() != 's':
                    continue
            if escolha == '1':
                nome_para_deletar = input("Digite o nome: ")
                for key, item in data.items():
                    if 'Name' in item and item['Name'] == nome_para_deletar:
                        del_url = url + '/' + key + '.json'
                        del_response = requests.delete(del_url)
                        if del_response.status_code == 200:
                            print("Deletado com sucesso")
                        else:
                            print("Falha ao deletar", del_response.status_code)
            elif escolha == '2':
                email_para_deletar = input("Digite o email: ")
                for key, item in data.items():
                    if 'Email' in item and item['Email'] == email_para_deletar:
                        del_url = url + '/' + key + '.json'
                        del_response = requests.delete(del_url)
                        if del_response.status_code == 200:
                            print("Deletado com sucesso")
                        else:
                            print("Falha ao deletar", del_response.status_code)
            elif escolha == '3':
                id_para_deletar = input("Digite o ID: ")
                for key, item in data.items():
                    if 'ID' in item and str(item['ID']) == id_para_deletar:
                        del_url = url + '/' + key + '.json'
                        del_response = requests.delete(del_url)
                        if del_response.status_code == 200:
                            print("Deletado com sucesso")
                        else:
                            print("Falha ao deletar", del_response.status_code)
            elif escolha == '4':
                break
            else:
                print("Escolha inválida. Por favor, digite 1, 2, 3 ou 4.")
    else:
        print("Falha ao obter dados do Firebase", response.status_code)

if __name__ == '__main__':
    main()