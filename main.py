'''
создай в проекте функцию с обычным принтом вместо заглушки, я тоже в своей ветке
'''


def main():
    galya() if input('who are you? ') == 'galya' else zhenya()


def galya():
    print('моя функция, которая не затрагивает Женину, хотя если я сейчас добавлю новую строку, проверим что получится')
    print('здесь была Галя\n\n=^.^=')
    dop = 'еще одно добавление для создания новой контрольной точки'


def zhenya():
    print('Меня зовут Женя')


def test_github():
    print('Galya')
    print('Zhenya')
    we = 'love'

if __name__ == 'main':
    main()