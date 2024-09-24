import unicodedata

while True:
    text_original = input("Please enter your text: ")
    text = text_original.replace(" ", ""). lower()

    text_final = ""
    text = unicodedata.normalize("NFD", text)
    for char in text:
        if unicodedata.category(char) != "Mn":
            text_final += char

    text_back = text_final[::-1]
    if text_final == text_back:
        print("Your text, \"", text_original, " \" IS a PALINDROM!", sep="")
    else:
        print("Sorry, your text \"", text_original, "\" is NOT a palindrom...", sep="")

    again = input("Another try? (y/n) ")
    if again == "y":
        continue
    else:
        break
