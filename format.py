def format_str(letters: str, f: str) -> str:
    for i in range(len(f)):
        if f[i].isupper() and f[i]:
            letters = letters.replace(letters[i], letters[i].upper())
        else:
            letters = letters.replace(letters[i], letters[i].lower())
    return letters


print(format_str("aBcDe", "Xxxxx!"))
