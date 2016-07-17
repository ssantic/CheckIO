import string
from collections import Counter

def checkio(text):
    #replace this for solution
    as_list = list(text)

    # iterate over list and remove non-letter characters
    for l in list(text):
        if l not in string.ascii_letters:
            as_list.remove(l)

    # convert all remaining list characters to lowercase
    lowercased_list = map(lambda x: x.lower(), as_list)

    # define list of result letters, and populate it with non-unique
    # letters from lowercased_list
    result_list = []
    for l in lowercased_list:
        if lowercased_list.count(l) != 1:
            result_list.append(l)

    # find the (alphabetically) first element of result_list
    def MostCommon(lst):
        data = Counter(lst)
        return data.most_common(1)[0][0]

    # check if there are non-unique elements at all, and accordingly return
    # the result
    if len(result_list) == 0:
        return min(lowercased_list)
    else:
        return MostCommon(result_list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
