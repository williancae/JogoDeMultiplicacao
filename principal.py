import random # importando biblioteca que gera numeros aleatorios
import datetime
# Dicionario de formatação de texto
colors = {'white':  '\033[30m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'purple': '\033[35m',
         'cyan': '\033[36m',
         'gray': '\033[37m',
         'clear': '\033[m'}
post = {'alert': '\033[1;31m',
        'win': '\033[1;32m',
        'danger': '\033[1;31m'}
print(colors['cyan']) #definindo a Cor do titulo como Ciano
print('███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗     ██╗ ██████╗ █████╗ ██████╗ ')
print('████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║     ██║██╔════╝██╔══██╗██╔══██╗')
print('██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║     ██║██║     ███████║██████╔╝')
print('██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║     ██║██║     ██╔══██║██╔══██╗')
print('██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗██║╚██████╗██║  ██║██║  ██║')
print('╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝\033[m')

score = 10 #pontuação inicial
fault = 0 #iniciando a varivel de erros
hits = 0 #iniciando a variavel de acertos
x = datetime.datetime.now()
print(x.strftime("\nInicio as %H:%M:%S")) #hora de inicio
while True:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 15)
    result = number1 * number2
    response = int(input('Qual o resultado da multiplicação:  {} x {} = '.format(number1, number2)))
    if result == response:
        score += 1
        hits += 1
        print('{} VOCÊ ACERTOU!{} {}Voce tem {} Pontos{}\n'.format(colors['green'], colors['clear'], colors['blue'], score, colors['clear']))
        if score >= 20:
            print('\n{}VOCÊ GANHOU O JOGO!!!{} {}Acertou {} vezes e {} Errou {} vez(es){}'.format(post['win'], colors['clear'], colors['blue'], hits, colors['red'], fault, colors['clear']))
            break
    elif result != response:
        score -= 2
        fault += 1
        print('{} VOCÊ ERROU!{} {}Voce tem {} Pontos{}'.format(colors['red'], colors['clear'], colors['blue'], score, colors['clear']))
        print('{}A Resposta era {}{}\n'.format(colors['cyan'], result,colors['clear']))
        if score <= 0:
            print('\n{}VOCÊ PERDEU!!!{} Errou {}{} vezes e {} acertou {} vezes{}'.format(post['alert'], colors['clear'], colors['yellow'], fault, colors['cyan'], hits, colors['clear']))
            break
y = datetime.datetime.now()
print(x.strftime("\nInicio as %H:%M:%S")) #hora de inicio
print(y.strftime("\nTerminou as %H:%M:%S")) #hora de fim

