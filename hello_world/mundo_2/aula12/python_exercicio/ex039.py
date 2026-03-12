from datetime import date
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m','azul':'\033[1;95m'}
# Titulo
print(f'-'*30)
print(f'{'ALISTAMENTO MILITAR 🪖':^29}')
print(f'-'*30)
ano = int(input(f'Digite o ano em que nasceu: '))
ano_atual = date.today().year
if ano_atual - ano == 18:
    print(f'Esta na hora de se ALISTAR')
elif ano_atual - ano > 18:
    print(f'Passou da hora de se ALISTAR')
else:
    print(f'Ainda vai se ALISTAR')