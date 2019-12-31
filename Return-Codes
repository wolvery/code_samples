def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def enumerate_possibilities(side):
    number_side = int("".join(side)) if len(side) > 0 else None
    list_chars_side = list()
    if number_side is not None:
        list_chars_side = calculate(number_side)
    return list_chars_side


def translate(splitted_number, index_to_be_alone):
    left_side = splitted_number[0:index_to_be_alone]
    chars_groups_left = enumerate_possibilities(left_side)
    if chars_groups_left is None:
        return []

    right_side = splitted_number[index_to_be_alone + 1:len(splitted_number)] \
        if index_to_be_alone + 1 <= len(splitted_number) \
        else list()

    chars_groups_right = enumerate_possibilities(right_side)
    if chars_groups_right is None:
        return []


    char_index = get_alphabet(int(splitted_number[index_to_be_alone]))

    saida_first = list()

    for chars_group_left in chars_groups_left:
        saida_first.append(chars_group_left + char_index)

    if len(chars_groups_left) == 0:
        saida_first.append(char_index)

    if len(chars_groups_right) == 0:
        return saida_first

    saida_final = list()
    for elemento in saida_first:
        for chars_group_right in chars_groups_right:
            saida_final.append(elemento + chars_group_right)



    return saida_final


def objetos(splitted_number, index_to_be_alone):
    if len(splitted_number) == index_to_be_alone:
        return list()
    return translate(splitted_number, index_to_be_alone) + objetos(splitted_number, index_to_be_alone + 1)


def calculate(number):
    if number <= 0:
        return None
    if number > 26:
        splitted_number = [i for i in str(number)]
        return {elemento for elemento in objetos(splitted_number, 0)}
    if number > 0 and number <= 26:
        return [get_alphabet(number)]



def obtercharacteres(number):
    if number > 0 and number <= 26:
        return [get_alphabet(number)]

    splitted_number = [i for i in str(number)]
    return {elemento for elemento in objetos(splitted_number, 0)}


if __name__ == '__main__':
    print(obtercharacteres(123))
