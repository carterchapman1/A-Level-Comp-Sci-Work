def title_case(title, minor_words=''):
    title = title.lower()
    words = (title.split())
    minor_words = minor_words.lower()
    minors = (minor_words.split())
    stringwords = ""
    for i in range (0,len(words)):
        if words[i] == words[0]:
            word = str(words[i])
            word = word.capitalize()
            words[i] = word
        elif words[i] in minors:
            pass
        else:
            word = str(words[i])
            word = word.capitalize()
            words[i] = word
        if stringwords != "":
            stringwords = stringwords + " " + words[i]
        else:
            stringwords = words[i]

    return stringwords

        