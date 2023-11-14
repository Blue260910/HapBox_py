import CadastroMedicamentos
import DeleteMedicamentos
import ListagemMedicamentos
import UpdateMedicamentos  

def main():
    while True:
        print("1 - Cadastrar Plano de Tratamento")
        print("2 - Deletar Plano de Tratamento")
        print("3 - Listar Plano de Tratamento")
        print("4 - Atualizar Plano de Tratamento")  
        print("5 - Sair")  
        escolha = input("Digite sua escolha: ")
        if escolha == '1':
            CadastroMedicamentos.main()
        elif escolha == '2':
            DeleteMedicamentos.main()
        elif escolha == '3':
            ListagemMedicamentos.main()
        elif escolha == '4':  
            UpdateMedicamentos.main()
        elif escolha == '5':  
            break
        else:
            print("Por favor, utilize 1, 2, 3, 4 ou 5.")  

if __name__ == "__main__":
    main()