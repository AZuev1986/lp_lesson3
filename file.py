#-*- coding: utf-8 -*-
with open('referat.txt', 'r', encoding='utf-8') as f1:
    content = f1.read()
print(len(content))
sum_word = 0
sum_word = 0
with open('referat.txt', 'r', encoding='utf-8') as f2:
    for line in f2:
        if line != '\n':
            sum_word += len(line.split(' '))
print(sum_word)
new_content = content.replace('.', '!')
with open('referat2.txt', 'w', encoding='utf-8') as f3:
    f3.write(new_content)