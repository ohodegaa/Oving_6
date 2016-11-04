__author__ = 'ohodegaa'


def set_tuple():
    liste = [0.6, 0.6, 0.3, 0.3, 0.3, 0.6]
    length = 0
    temp_length = -1
    left = -1
    temp_left = -1
    for i in range(len(liste)):
        if liste[i] < 0.5:
            if temp_length == -1:
                temp_left = i
            temp_length += 1
        else:
            if temp_length >= length:
                length = temp_length
                left = temp_left
            temp_length = -1
    if temp_length > length:
        length = temp_length
        left = temp_left

    print((left, left + length))

set_tuple()