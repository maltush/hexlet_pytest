def reverse(string):
    return string[::-1]


with open('input.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()


reversed_text = reverse(original_text)


with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(reversed_text)

print("Перевернутый текст записан в output.txt")