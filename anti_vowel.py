def anti_vowel(text):
    word = ""
    vowel = "aeiouAEIOU"
    for x in text:
        if x in vowel:
            print ""
        else:
            word += x
    return word
