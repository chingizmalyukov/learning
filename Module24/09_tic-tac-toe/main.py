class Board:
    board = list(range(1, 10))

    def take_input(self, symbol):
        valid = False
        while not valid:
            answer = input("Куда поставим " + symbol + "? ")
            try:
                answer = int(answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= answer <= 9:
                if str(self.board[answer - 1]) not in "XO":
                    self.board[answer - 1] = symbol
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")

    def draw_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-" * 13)

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False


board = Board()
token_1 = 'X'
token_2 = 'O'

step = 1
while step != 10:

    board.draw_board()
    if step % 2 != 0:
        player_token = token_1
    else:
        player_token = token_2
    board.take_input(player_token)
    if step > 4:
        if board.check_win():
            print(board.check_win(), 'победил!')
            break
    step += 1

else:
    print('НИЧЬЯ!')
