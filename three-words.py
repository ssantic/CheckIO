def checkio(words):

    result = False

    # convert string into a list of strings
    word_list = words.split()

    # convert numerals into integers
    for i in xrange(len(word_list)):
        try:
            word_list[i] = int(word_list[i])
        except ValueError:
            pass

    # check in there is a succesion of three strings in the list
    for i in xrange(1, len(word_list) - 1):
        if type(word_list[i]) == unicode and type(word_list[i-1]) == unicode and type(word_list[i+1]) == unicode:
            result = True

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
