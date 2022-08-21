'''
создай в проекте функцию с обычным принтом вместо заглушки, я тоже в своей ветке
'''


def main():
    galya() if input('who are you? ') == 'galya' else zhenya()


def galya():
    pass

def zhenya():
    print('Меня зовут Женя')


if __name__ == 'main':
    main()