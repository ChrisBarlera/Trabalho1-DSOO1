class TelaDoador:
    def tela_opcoes(self):
        print('\n-------- DAODOR ----------')
        print('1 - Incluir Doador')
        print('2 - Alterar Doador')
        print('3 - Listar Doadores')
        print('4 - Excluir Doador')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_gato(self):
        print('\n-------- DADOS DAODOR ----------')
        numero_chip = int(input('Número do chip: '))
        nome = input('Nome: ')
        raca = input('Raça: ')

        return {'numero_chip': numero_chip, 'nome': nome, 'raca': raca}
    
    def mostra_gato(self, dados_gato):
        print('\nNUMERO DO GATO: ', dados_gato['numero_chip'])
        print('NOME DO GATO: ', dados_gato['nome'])
        print('RACA DO GATO: ', dados_gato['raca'])

    def seleciona_gato(self):
        numero = int(input('\nNumero do gato que deseja selecionar: '))
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)