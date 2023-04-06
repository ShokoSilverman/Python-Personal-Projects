# two inputs (str, str)
# check if anagrams of eachother
# silent = listen


def check_anagram(input1: str, input2: str):
    input1_dict: dict = {}
    input2_dict: dict = {}
    for letter in list(input1):
        if input1_dict.get(letter) is None:
            input1_dict[letter] = 1
        else:
            input1_dict[letter] = input1_dict[letter] + 1
    for letter in list(input2):
        if input2_dict.get(letter) is None:
            input2_dict[letter] = 1
        else:
            input2_dict[letter] = input2_dict[letter] + 1
    return input1_dict == input2_dict


print(check_anagram("silent", "listeni"))
