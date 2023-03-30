from agenda import Agenda

lista = Agenda()

#Adicionando contatos 
lista.adicionar_contatos("Pedro Leocir", "(54) 9 9903-2834")
lista.adicionar_contatos("Otavio Leomar", "(54) 9 9685-1532")
lista.adicionar_contatos("Jadir Zwrites", "(54) 9 9620-5015")
lista.adicionar_contatos("Iene Angelin", "(54) 9 9659-6062")

#Exibindo lista de contatos
print("-"*15,"Todos os contatos","-"*15)

for x in lista.agenda.keys():
    print(f"{x} // {lista.agenda[x]}")

print()

#Buscando contato pelo nome
print("-"*15,"Busca de contatos","-"*15)

print(lista.bucar_contato(None,"(54) 9 9903-2834")) # Pedro Leocir
print(lista.bucar_contato("Iene Angelin")) # (54) 9 9659-6062
print(lista.bucar_contato("Otavio Leomar")) # (54) 9 9685-1532
print(lista.bucar_contato(None,"(54) 9 9659-6062")) # Jadir Zwirtes