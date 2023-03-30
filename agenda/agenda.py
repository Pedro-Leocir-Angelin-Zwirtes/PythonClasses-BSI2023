#Crie uma classe "Agenda" que tenha uma lista de contatos e métodos para adicionar contatos, buscar um contato pelo nome e imprimir a lista de contatos.

class Agenda():
    """Classe construtora da agenda"""

    def __init__(self):
        """Método iniciador"""
        
        self.agenda = {

        }

    def adicionar_contatos(self, nome:str, numero:str):
        """Método responsavel por adicionar os contatos"""

        if not isinstance(nome, str):
            raise TypeError("O contato deve ser uma string")
        
        if not isinstance(numero, str):
            raise TypeError("O contato deve ser uma string ex: (54) 9 9999-9999")
        
        try:

            self.nome = nome
            self.numero = numero

        except Exception as e:
            return e
        
        self.agenda[self.nome] = self.numero

    def bucar_contato(self, nome_busca=None, numero_busca=None):
        """Método que vai buscar o contato pelo nome ou numero"""

        try:

            self.nome_busca = nome_busca
            self.numero_busca = numero_busca

        except Exception as e:
            return e
        
        #Verificando se o nome não é vazio e buscando no dicionario
        if nome_busca is not None:

            for contato in self.agenda.keys():
                if contato == nome_busca:
                    return f"A busca de {self.nome_busca} foi encontrado {self.agenda[contato]}"
                
        #Caso o nome esteja vazio ele vai verificar se o numero possui algum valor     
        else:
            if numero_busca is not None:

                for contato, busca in self.agenda.items():
                    if busca == numero_busca:
                        return f"A busca de {self.numero_busca} foi encontrado {contato}"