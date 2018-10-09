#-*- coding: utf-8 -*-
with open('referat.txt', 'r', encoding='utf-8') as f1:
    content = f1.read()
print(len(content))
with open('referat.txt', 'r', encoding='utf-8') as f3:
    content3 = f3.read()
    print(len(content3.split()))
new_content = content.replace('.', '!')
with open('referat2.txt', 'w', encoding='utf-8') as f3:
    f3.write(new_content)