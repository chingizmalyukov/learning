import random

random.seed()  # NOTE превосходно!


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Тебе выпала {current}. Кол-во твоих очков: {score}.')
        else:
            print(f'Компьютеру выпала карта {current}. Кол-во его очков: {score}.')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Еще карту? да/нет\n').lower()
            if choice == 'да':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Ты проиграл!')
                    break
                elif score == 21 and bot_score == 21:
                    print('ничья')
                elif score == 21 or bot_score > 21:
                    print('Ты победил!')
                    break
            elif choice == 'нет':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Ты проиграл, кол-во твоих очков - {score}, кол-во очков у компьютера - {bot_score}!')
                else:
                    print(f'Ты победил, кол-во твоих очков - {score}, кол-во очков у компьютера - {bot_score}!')

                break

    def start(self):
        random.shuffle(self.deck)
        print('Короче, тема серьезная, это тебе не 21, и не очко. Это новый уровень - BlackJack.')
        print('"В чем разница?", спросишь ты меня, а я тебе объясню:')
        print('В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков')
        print('----------------------------------')
        self.choice()

        print('парам пам пам')


game = BlackJack()
game.start()
