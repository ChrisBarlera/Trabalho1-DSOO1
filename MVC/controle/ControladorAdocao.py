from limite.TelaAdocao import TelaAdocao
from entidade.Adocao import Adocao


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_adotante = controlador_sistema.controlador_adotante
        self.__controlador_animal = controlador_sistema.controlador_animal
        self.__adocoes = [] # type: ignore
        self.__tela_adocao = TelaAdocao()
        self.__contador_id = 1

    def incluir_adocao(self):
        adotante = None
        animal = None
        
        if self.ja_tem_adotante():
            adotante = self.__controlador_adotante.seleciona_adotante()
        else:
            self.__tela_adocao.mostra_mensagem('Cadastre um adotante')
            adotante = self.__controlador_adotante.incluir_adotante()
        
        if self.ja_tem_animal():
            animal = self.__controlador_animal.seleciona_animal()
        else:
            self.__tela_adocao.mostra_mensagem('Cadastre um animal')
            animal = self.__controlador_animal.incluir_animal()
        
        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        nova_adocao = Adocao(self.__contador_id, adotante, animal, dados_adocao['data'])
        self.__contador_id += 1
        self.__adocoes.append(nova_adocao)
        return nova_adocao
    
    def alterar_adocao(self):
        self.lista_adocoes()
        numero_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_numero(numero_adocao)

        if adocao is not None:
            if self.tbm_trocar_adotante():
                self.__tela_adocao.mostra_mensagem('Cadastre o adotante')
                novo_adotante = self.__controlador_adotante.incluir_adotante()
                adocao.adotante = novo_adotante

            if self.tbm_trocar_animal():
                self.__tela_adocao.mostra_mensagem('Cadastre o animal')
                novo_animal = self.__controlador_animal.incluir_animal()
                adocao.animal = novo_animal
            novos_dados = self.__tela_adocao.pega_dados_adocao()
            adocao.data = novos_dados['data']
        else:
            self.__tela_adocao.mostra_mensagem('ATENCAO: adoção não existente')
        self.lista_adocoes()
        return adocao

    def lista_adocoes(self):
        for adocao in self.__adocoes:
            dados = {'numero_id': adocao.numero_id,
                     'data': adocao.data,
                     'animal': adocao.animal,
                     'adotante': adocao.adotante}
            self.__tela_adocao.mostra_adocao(dados)
            self.__controlador_animal.mostra_animal_especifico(dados['animal'])
            self.__controlador_adotante.mostra_adotante_especifico(dados['adotante'])

    def excluir_adocao(self):
        self.lista_adocoes()
        numero_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_numero(numero_adocao)

        if adocao is not None:
            self.__adocoes.remove(adocao)
        else:
            self.__tela_adocao.mostra_mensagem('ATENCAO: adoção não existente')
        
        self.lista_adocoes()

    def pega_adocao_por_numero(self, numero_id):
        for adocao in self.__adocoes:
            if adocao.numero_id == numero_id:
                return adocao
        return None

    def ja_tem_adotante(self):
        return self.__tela_adocao.ja_tem_adotante()
    
    def ja_tem_animal(self):
        return self.__tela_adocao.ja_tem_animal()

    def tbm_trocar_adotante(self):
        return self.__tela_adocao.tbm_trocar_adotante()
    
    def tbm_trocar_animal(self):
        return self.__tela_adocao.tbm_trocar_animal()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao,
                        2: self.alterar_adocao,
                        3: self.lista_adocoes,
                        4: self.excluir_adocao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()