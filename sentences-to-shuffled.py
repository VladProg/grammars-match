from random import shuffle
import sys

sentences = list(open('sentences.txt', encoding='utf-8'))
print('sentences:', len(sentences))
shuffle(sentences)
open('shuffled.txt', 'w', encoding='utf-8').write(''.join(sentences))
