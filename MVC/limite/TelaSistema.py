class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("\n-------- Sistema para ONG de adoção de animais ---------")
        print("1 - Animais")
        print("2 - Pessoas")
        print("3 - Doações")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao