import requests
import json

def validar_cpf(cpf):
    try:
        int(cpf)  # Tenta converter o CPF em um número
        if len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")
        return True
    except ValueError as e:
        print(f"Cpf inválido: {cpf}")
        return False

def add_record():
    # Postar dados no Firebase
    url = "https://hapbox-f9157-default-rtdb.firebaseio.com/.json"

    # Buscar todos os dados existentes
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extrair IDs e encontrar o máximo
        ids = [item['ID'] for item in data.values() if 'ID' in item]
        max_id = max(ids) if ids else 0
    else:
        print("Falha ao obter dados do Firebase", response.status_code)
        return

    # Obter entrada do usuário
    id = max_id + 1  # Preencher automaticamente o ID
    print("ID:", id)
    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    if any(item['Email'] == email for item in data.values()):
        print("Essa conta já existe.")
        return

    cpf = input("Digite o CPF: ")
    while not validar_cpf(cpf) or any(item['CPF'] == cpf for item in data.values()):
        if any(item['CPF'] == cpf for item in data.values()):
            print("Este CPF já existe.")
            return
        cpf = input("Digite o CPF: ")

    phone = input("Digite o telefone: ")
    while not phone.isdigit():
        print("Telefone inválido. Por favor insira apenas números.")
        phone = input("Digite o telefone: ")
    senha = input("Digite a senha: ")
    hapBoxId = input("Digite o HapBoxId: ")
    while not hapBoxId.isdigit():
        print("Entrada inválida. HapBoxId deve ser um número.")
        hapBoxId = input("Digite o HapBoxId: ")
    medicamentos = input("Digite os medicamentos (separados por vírgula): ").split(',')
    horarios = input("Digite os horários no formato 00:00 (separados por vírgula) : ").split(',')
    doses = list(map(int, input("Digite as doses (separadas por vírgula): ").split(',')))
    quantidadeComprimidos = list(map(int, input("Digite a quantidade de comprimidos (separados por vírgula): ").split(',')))

    # Preparar dados
    data = {
        "ID": int(id),
        "Name": name,
        "Email": email,
        "CPF": int(cpf),
        "Phone": phone,
        "Senha": senha,
        "HapBoxId": int(hapBoxId),
        "Medicamentos": medicamentos,
        "Horarios": horarios,
        "Doses": doses,
        "QuantidadeComprimidos": quantidadeComprimidos
    }

    response = requests.post(url, json=data)

    # Se a solicitação foi bem-sucedida, response.status_code será 200
    if response.status_code == 200:
        print("Dados postados com sucesso")
    else:
        print("Falha ao postar dados no Firebase", response.status_code)

def main():
    while True:
        print("1 - Adicionar cronograma de medicamentos")
        print("2 - Sair")
        choice = input("Digite sua escolha: ")
        if choice == '1':
            add_record()
        elif choice == '2':
            break
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

if __name__ == '__main__':
    main()