def lang(a, b):

    for la in a:

        if la == b:

            return True
    return False


languages = ['python', 'kotlin', 'javascript']

lag = lang(languages, 'python')

print(lag)
