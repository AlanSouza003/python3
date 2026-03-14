from datetime import date
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m','azul':'\033[1;94m'}
# Titulo
print(f'{cor['branco']}-{cor['limpa']}'*30)
print(f'{cor['azul']}{'ALISTAMENTO MILITAR 🪖':^29}{cor['limpa']}')
print(f'{cor['branco']}-{cor['limpa']}'*30)
ano = int(input(f'{cor['branco']}Digite o ano em que nasceu: {cor['limpa']}'))
ano_atual = date.today().year
if ano_atual - ano == 18:
    print(f'{cor['amarelo']}ESTA NA HORA DE SE ALISTAR{cor['limpa']}')
elif ano_atual - ano > 18:
    print(f'{cor['vermelho']}PASSOU DA HORA DE SE ALISTAR{cor['limpa']}')
else:
    print(f'{cor['verde']}AINDA VAI SE ALISTAR{cor['limpa']}')