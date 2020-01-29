

text = "HelLoworld"


def maximumOccurringCharacter(text):
    # Write your code here
    list1 = list(text)
    new_dict = dict(dict.fromkeys(list1))

    for i in new_dict:
        new_dict[i] = list1.count(i)

    keymax = max(new_dict, key=new_dict.get)

    return keymax


print(maximumOccurringCharacter(text))
