def reverse(text):
    x = text
    y = len(x) - 1
    backwards = ""
    while y > -1:
        backwards = backwards + x[y]
        y -= 1
    return backwards
