"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

import pydoc

MAX_FREQ_WORD_COUNT = 10

text = pydoc.render_doc(int, "Help on %s").split()
counter = {}

for word in text:
    if word.isalpha():
        counter[word] = counter.get(word, 0) + 1

counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)

for i in range(MAX_FREQ_WORD_COUNT) if len(counter) > MAX_FREQ_WORD_COUNT \
        else range(len(counter)):
    print(*counter[i])
