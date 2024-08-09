#translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "O"
            else:
                translation = translation + "o"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase\n")))
