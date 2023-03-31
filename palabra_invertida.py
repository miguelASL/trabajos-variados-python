def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for i in range(0, text_len):
        reversed_text += text[text_len -i - 1]
    return reversed_text

print(reverse("mamahuevos"))