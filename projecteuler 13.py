def problem_13(zahl):
    with open("C://Users//Crymlink//Desktop//number.txt") as txt:
        str_txt = []
        str_txt = txt.read().split('\n')

        a = 0
        bla = [f for f in str_txt]
        print(bla)
        list_word = [int(f) for f in str_txt]
        a = sum(list_word)
        ende = str(a)
        print(ende[:10])
problem_13(1)
