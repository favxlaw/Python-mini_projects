'''def translate (phrase):
    translation = phrase + "g"
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                    translation + translation +"g"
        else:
            translation = translation + letter
        return translation
print(translate(input("Enter a word: ")))   
'''
try:
    num = int(input("Enter a number"))
    print(num)
except:
    print("invalid input")