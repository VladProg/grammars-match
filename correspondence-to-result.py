from collections import Counter, defaultdict
import sys

sys.stdout = open('result.txt', 'w')

dataset = [line.split() for line in open('correspondence.txt')]
print('total relations:', len(dataset), file=sys.stderr)
assert all(len(item) == 4 for item in dataset)
print('different categories: ',
      *zip(['relations', 'first', 'second', 'parent'],
           [len(set(item[i] for item in dataset)) for i in range(4)]),
      file=sys.stderr)

cnt_relation = Counter()
cnt_relation_first_second_parent = defaultdict(Counter)

for relation, first, second, parent in dataset:
    cnt_relation[relation] += 1
    cnt_relation_first_second_parent[relation][first, second, parent] += 1

for relation in sorted(cnt_relation, key=lambda relation: cnt_relation[relation], reverse=True):
    denominator = cnt_relation[relation]
    (first, second, parent), numerator = cnt_relation_first_second_parent[relation].most_common(1)[0]
    print(f'{relation}({first}, {second}) -> {parent} | {numerator} / {denominator} = {numerator / denominator:.3f}')
