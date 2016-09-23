
def rot13_transform(s):
    # do transform for aphabetic leters
    char_list = list(s)

    for index, char in enumerate(char_list):
        ord_num = ord(char)
        if ord_num >= 65 and ord_num <= 90:  # lowercase
            char_list[index] = chr(ord_num + 13) if ord_num <= 77 else chr(ord_num - 13)
        elif ord_num >= 97 and ord_num <= 122:  # uppercase
            char_list[index] = chr(ord_num + 13) if ord_num <= 109 else chr(ord_num - 13)

    res = ''.join(char_list)
    return res


print(rot13_transform('abc'))
