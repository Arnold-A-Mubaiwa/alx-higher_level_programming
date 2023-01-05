#!/usr/bin/python3
"""Define the function text_indentation"""


def text_indentation(text):
    """
    Returns nothing

    Prints out each char to the terminal using a loop until
    it reaches the ., ? or :

    Raises:
        TypeError if the argument passed is not an integer
    """
    list_x = ['.', '?', ':']
    str_l = list(text)
    for i in range(len(str_l)):
        if str_l[i] in list_x:
            print(str_l[i])
            print()
            str_l[i + 1] = ''
        else:
            print(str_l[i], end='')


text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")