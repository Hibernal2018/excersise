import unicodedata

while True:
    text = input("Zadejte výraz: ")
    text_simple = text.replace(" ", "").lower()

    text_final = ""
    helper_text = unicodedata.normalize("NFD", text_simple)
    for char in helper_text:
        if unicodedata.category(char) != "Mn":
            text_final += char

    if text_final == text_final[::-1]:
        print(f"Váš text, \"{text}\", JE PALINDROM!")
    else:
        print(f"Váš text,\"{text}\", NENÍ PALINDROM!")
    
    again = input("Další výraz? (a/n): ")
    if again == "a":
        continue
    else:
        break



            
