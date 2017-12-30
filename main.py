import tictactoe as tic

win = False
while win is False:
    #acertar verificacao, sair do loop imediatamente se houve ganhador
    tic.getPlayerMark(1)
    print(tic.game[0])
    print(tic.game[1])
    print(tic.game[2])
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
    print(tic.game[0])
    print(tic.game[1])
    print(tic.game[2])
    if win:
        print('computer win')
        break
