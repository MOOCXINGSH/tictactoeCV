import tictactoe as tic

def dispaygame(game):
    print(game[0])
    print(game[1])
    print(game[2])

win = False
while win is False:
    #acertar verificacao, sair do loop imediatamente se houve ganhador
    tic.getPlayerMark(1)
    dispaygame(tic.game)
    win = tic.verifyWinner(1)
    if win=='EMPATE':
        print('no body win')
        break
    if win:
        print('You win !')
        break
    tic.inteligence(2)
    win = tic.verifyWinner(2)
    print("computer already played")
    dispaygame(tic.game)
    if win:
        print('computer win')
        break
