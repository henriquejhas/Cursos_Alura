import re

endereco = 'Rua das Flores, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)