s = "Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели."
count = 0
words = s.split()
for word in words:
    if word[0].lower() == 'е':
        count += 1
print("Количество слов на букву 'е': ", count)