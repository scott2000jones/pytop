from blessings import Terminal

term = Terminal()
print(term.red + term.on_green + 'Red on green? Ick!' + term.normal)
print(term.bright_red + term.on_bright_blue + 'This is even worse!' + term.normal)
with term.location():
    print(term.move(1, 1) + 'Hi')
    print(term.move(9, 9) + 'Mom')