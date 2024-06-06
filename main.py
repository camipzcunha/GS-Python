#Lista para salvar os usuários 
users = []  

#Lista para salvar as Startups cadastradas
startups = []

#Lista para salvar as empresas cadastradas
companies = []

# Lista para armazenar conexões entre empresas e startups
connections = []

# Lista de campo de atuação
fields = ['Lixo', 'Poluentes', 'Diversidade', 'Limpeza']

#Exibir o menu de opções
def show_menu():
    print("\nBem-vindo ao AquaVision Center!")
    print("1. Cadastrar usuário")
    print("2. Cadastrar startup")
    print("3. Cadastrar empresa")
    print("4. Encontrar startup para sua empresa")
    print("5. Conecte sua empresa com uma startup")
    print("6. Listar usuários")
    print("7. Listar startups")
    print("8. Listar empresas")
    print("9. Listar conexões")
    print("10. Sair")

#Função para cadastrar um usuário
def register_user():
    print("\nCadastre-se em nosso site!")
    name = input("Nome: ")
    email = input("Email: ")
    password = input("Senha: ")
    repeat_password = input("Repita a senha: ")
    if password != repeat_password:
        print("As senhas não coincidem!")
        password = input("Senha: ")
        repeat_password = input("Repita a senha: ")
    user = {"name": name, "email": email, "password": password}
    users.append(user)
    print(f"Usuário {name} cadastrado com sucesso!")

#Função para cadastrar uma startup
def register_startup():
    print("\nCadastre sua startup!")
    name = input("Nome: ")
    owner = input("Proprietário: ")
    field = input("Área de atuação. Escolha uma das seguintes opções:\n'Lixo'\n'Poluentes'\n'Diversidade'\n'Limpeza':")
    while field not in fields:
        print("Área de atuação inválida! Tente novamente.")
        field = input("Escolha uma das seguintes opções:\n'Lixo'\n'Poluentes'\n'Diversidade'\n'Limpeza':")
    description = input("Descrição: ")
    startup = {"name": name, "owner":owner, "field": field, "description": description}
    startups.append(startup)
    print(f"Startup {name} cadastrada com sucesso!")


#Função para cadastrar uma empresa
def register_company():
    print("\nCadastre sua empresa!")
    name = input("Nome: ")
    owner = input("Proprietário: ")
    field = input("Área de atuação: ")
    description = input("Descrição: ")
    company = {"name": name, "owner": owner, "field": field, "description": description}
    companies.append(company)
    print(f"Empresa {name} cadastrada com sucesso!")

#Função para encontrar a startup adequada para a empresa
def find_startup(company_problem):
    for startup in startups:
        if startup['field'] == company_problem:
            print(f"Startup encontrada: {startup['name']}")
            print(f"Descrição: {startup['description']}")
            break
        else:
            print("Nenhuma startup foi encontrada para o problema. Aguarde novas inscrições!.")

#Função para conectar uma empresa com uma startup   
def connect():
    company_name = input("Nome da empresa: ")
    startup_name = input("Nome da startup: ")

     #Verificar se a empresa e a startup existem
    company_exists = False
    startup_exists = False

    for company in companies:
        if company["name"] == company_name:
            company_exists = True
            break
    for startup in startups:
        if startup["name"] == startup_name:
            startup_exists = True
            break
    if company_exists and startup_exists:
        connection = {"company_name": company_name, "startup_name": startup_name}
        connections.append(connection)
        print(f"{company_name} conectada com {startup_name} com sucesso!\nEntre em contato para mais informações.")
    else:
        print("Empresa ou startup não encontrada! Tente novamente.")

#Função para listar os usuários
def list_users():
    if not users:
        print("Nenhum usuário cadastrado!")
        return
    print("\nUsuários cadastrados:")
    for user in users:
        print(f"Nome: {user['name']}, Email: {user['email']}")

#Função para listar as startups
def list_startups():
    if not startups:
        print("Nenhuma startup cadastrada!")
        return
    print("\nStartups cadastradas:")
    for startup in startups:
        print(f"Nome: {startup['name']}, Área de atuação: {startup['field']}")
        print(f"Descrição: {startup['description']}")

#Função para listar as empresas
def list_companies():
    if not companies:
        print("Nenhuma empresa cadastrada!")
        return
    print("\nEmpresas cadastradas:")
    for company in companies:
        print(f"Nome: {company['name']}, Área de atuação: {company['field']}")
        print(f"Descrição: {company['description']}")

#Função para listar as conexões
def list_connections():
    if not connections:
        print("Nenhuma conexão cadastrada!")
        return
    print("\nConexões cadastradas:")
    for connection in connections:
        print(f"Empresa: {connection['company_name']}, Startup: {connection['startup_name']}")

#Função principal
def main():
    while True:
        show_menu()
        option = input("Escolha uma opção: ")
        if option == "1":
            register_user()
        elif option == "2":
            register_startup()
        elif option == "3":
            register_company()
        elif option == "4":
            company_problem = input("Descreva a área do problema que deseja solucionar:\n'Lixo'\n'Poluentes'\n'Diversidade'\n'Limpeza':")
            while company_problem not in fields:
                print("Área de atuação inválida! Tente novamente.")
                company_problem = input("Descreva a área do problema que sua empresa deseja solucionar:\n'Lixo'\n'Poluentes'\n'Diversidade'\n'Limpeza': ")
            find_startup(company_problem)
        elif option == "5":
            connect()
        elif option == "6":
            list_users()
        elif option == "7":
            list_startups()
        elif option == "8":
            list_companies()
        elif option == "9":
            list_connections()
        elif option == "10":
            print("Obrigado por usar o AquaVision Center! Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
#Executar a função principal

main()

