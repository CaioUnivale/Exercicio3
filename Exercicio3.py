class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

    def mostrar_endereco(self):
        return f"{self.rua}, {self.cidade}"

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostrar_informacoes(self):
        return f"{self.nome} mora em {self.endereco.mostrar_endereco()}"
        
class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar_info_computador(self):
        return f"Computador com sistema operacional {self.sistema.nome} versão {self.sistema.versao}"


endereco_exemplo = Endereco("Rua Principal", "Cidade Exemplo")
pessoa_exemplo = Pessoa("João", endereco_exemplo)

sistema_exemplo = SistemaOperacional("Windows", "10")
computador_exemplo = Computador(sistema_exemplo)

print(pessoa_exemplo.mostrar_informacoes())
print(computador_exemplo.mostrar_info_computador())