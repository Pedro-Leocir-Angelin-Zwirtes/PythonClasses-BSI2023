from empregado import Empregado
from gerente import Gerente
from vendedor import Vendedor

NOME_PADRAO = "Pedro" 

empregado1 = Empregado(NOME_PADRAO)
gerente1 = Gerente(NOME_PADRAO, "Gerencia")
vendedor1 = Vendedor(NOME_PADRAO, 10.0)

print(vendedor1)
print(gerente1)
