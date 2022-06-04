import uuid

if __name__ == '__main__':
    funcionarios = []

    class Funcionario:
        def __init__(self, codigo, nome, email, data_admissao, salario):
            self.codigo = codigo
            self.nome = nome
            self.email = email
            self.data_admissao = data_admissao
            self.salario = salario

    menu_opcaos = {
        1: 'Criar um funcionário',
        2: 'Listar funcionários',
        3: 'Atualizar funcionário',
        4: 'Deletar funcionário',
        5: 'Sair',
    }

    def print_menu():
        for key in menu_opcaos.keys():
            print(key, '--', menu_opcaos[key])

    def create_funcionario():
        codigo = str(uuid.uuid4())
        nome = str(input('Digite o nome do funcionário: '))
        email = str(input('Digite o e-mail do funcionário: '))
        data_admissao = str(input('Digite a data de admissão do funcionário: '))
        salario = str(input('Digite o salário do funcionário: '))
        funcionario = Funcionario(codigo, nome, email, data_admissao, salario)
        funcionarios.append(funcionario)
        print('Funcionário criado com sucesso!\n', vars(funcionario))

    def list_funcionarios():
        for funcionario in funcionarios:
            print(vars(funcionario))


    def find_funcionario(uuid):
        for funcionario in funcionarios:
            if funcionario.codigo == uuid:
                return funcionario

    def update_funcionario():
        uuid = str(input('Digite o código do funcionário: '))
        funcionario = find_funcionario(uuid)
        if funcionario is None:
            return print('Funcionário não encontrado')
        print('Caso não deseje alterar, apenas aperte ENTER!')
        nome = str(input(f'Digite o nome do funcionário [{funcionario.nome}]: ') or funcionario.nome)
        email = str(input(f'Digite o e-mail do funcionário [{funcionario.email}]: ') or funcionario.email)
        data_admissao = str(input(
            f'Digite a data de admissão do funcionário [{funcionario.data_admissao}]: ') or funcionario.data_admissao)
        salario = str(input(f'Digite o salário do funcionário [{funcionario.salario}]: ') or funcionario.salario)
        funcionario.nome = nome
        funcionario.email = email
        funcionario.data_admissao = data_admissao
        funcionario.salario = salario
        print('Funcionário atualizado com sucesso!\n', vars(funcionario))

    def delete_funcionario():
        uuid = str(input('Digite o código do funcionário: '))
        for indice, funcionario in enumerate(funcionarios):
            if funcionario.codigo == uuid:
                del funcionarios[indice]
                return print('Funcionário deletado!')
        return print('Funcionário não encontrado')

    while(True):
        print_menu()
        opcao = ''
        try:
            opcao = int(input('Digite uma opção: '))
        except:
            print('Input inválido. Por favor digite um número')

        if opcao == 1:
           print('+------- Início da criação de Funcionários -------+')
           create_funcionario()
           print('+------- Fim da criação de Funcionários -------+')
        elif opcao == 2:
            print('+------- Início da listagem de Funcionários -------+')
            list_funcionarios()
            print('+------- Fim da listagem de Funcionários -------+')
        elif opcao == 3:
            print('+------- Início da criação de Funcionários -------+')
            update_funcionario()
            print('+------- Fim da criação de Funcionários -------+')
        elif opcao == 4:
            print('+------- Início da exclusão de Funcionários -------+')
            delete_funcionario()
            print('+------- Fim da exclusão de Funcionários -------+')
        elif opcao == 5:
            print('Saindo')
            exit()
        else:
            print('Opção inválida. Por favor, digite um número entre 1 e 5')