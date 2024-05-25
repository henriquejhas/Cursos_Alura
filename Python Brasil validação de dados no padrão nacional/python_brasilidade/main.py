from Cpf_Cnpj import Documento
import re
from telefoneBr import TelefonesBr
from datetime import datetime, timedelta
from  datasBr import DatasBr
from acesso_cep import BuscaEndereco
import requests
#cpf_um = Cpf('12354367996')
#print(cpf_um)
exemplo_cnpj = "35379838000112"
exemplo_cpf = '32007832062'
documento = Documento.cria_documento(exemplo_cpf)
#print(documento)

#padrao = '[0-9][a-z]{2}[0-9]'
#texto = '123 1ac2 1cc aa1'

#padrao = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
#padrao = '\w{5,50}@\w{3,10}.com.br'
#texto = 'asdflskdjfç rodrigo123@gmail.com.br jkdjaflsd jdklfçd'

#padrao_molde = '(xx)aaaa-wwww'
#padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
#texto = 'eu gosto do número 2125451234 e gosto também do 2136431234'

#resposta = re.findall(padrao, texto)
#print(resposta)

#telefone = '55119 26481234'

#telefone_objeto = TelefonesBr(telefone)
#padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
#resposta = re.search(padrao, telefone)
#print(telefone_objeto)

#cadastro = DatasBr()
#print(cadastro.dia_semana())

#hoje = datetime.today()
#hoje_formatada = hoje.strftime('%d/%m/%Y %H:%M')
#print(hoje)
#print(cadastro)

#hoje = datetime.today()
#amanha = datetime.today() + timedelta(days=1, hours=20)
#print(amanha - hoje)

#hoje = DatasBr()
#print(hoje.tempo_cadastro())

cep = '01524010'
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep)

#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(r.text)

#a = objeto_cep.acesso_via_cep()
#print(a.text)
#print(a.json())
#print(a.json()['bairro'])

bairro, cidade, uf = objeto_cep.acesso_via_cep()
print(bairro)
print(cidade)
print(uf)