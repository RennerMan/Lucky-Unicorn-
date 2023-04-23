def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n {formatted_text}\n {top_bottom}"

print(formatter("-", "Welcome to the Lucky Unicorn game!"))
print()
print(formatter("!", "Congrats, you got a Unicorn"))
print()
print(formatter("*", "Goodbye!"))

