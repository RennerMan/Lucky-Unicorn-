def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n {formatted_text}\n {top_bottom}"


text1 = input("What statement do you want to format?")
symbol1 = input("What symbol do you want to format?")
print()
print(formatter(symbol1, text1))

