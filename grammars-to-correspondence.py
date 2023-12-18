import re
import sys

grammars = open('grammars.txt').read().split('\n\n')
print('grammars:', len(grammars) // 2, 'pairs')


class Node:
    def __init__(self, category):
        self.category = category
        self.children = []
        self.word = self.index = None

    def __repr__(self):
        return self.category + '(' + ', '.join(
            ([self.full()] if self.full() else []) + [str(child) for child in self.children]) + ')'

    def full(self):
        return f'{self.word}-{self.index}' if self.word else None

    def lca(self, first, second):
        if self.full() == first == second:
            return self, self, self
        if self.full() == first:
            return 1
        if self.full() == second:
            return 2
        first_child = second_child = None
        for child in self.children:
            res = child.lca(first, second)
            if isinstance(res, tuple):
                return res
            elif res == 1:
                first_child = child
            elif res == 2:
                second_child = child
        if first_child and second_child:
            return first_child, second_child, self
        elif first_child:
            return 1
        elif second_child:
            return 2


with open('correspondence.txt', 'w') as file:
    for constituents, dependencies in zip(grammars[::2], grammars[1::2]):
        constituents = re.split(r'[ \n]+', constituents.replace(')', ' ) '))
        root = Node(constituents[0][1:])
        stack = [root]
        index = 0
        for item in constituents[1:]:
            if item.startswith('('):
                node = Node(item[1:])
                stack[-1].children.append(node)
                stack.append(node)
            elif item == ')':
                stack.pop()
            elif item:
                if item == '-LRB-':
                    item = '('
                elif item == '-RRB-':
                    item = ')'
                stack[-1].word = item
                index += 1
                stack[-1].index = index
        for dependency in dependencies.split('\n'):
            relation, first_second = dependency.removesuffix(')').split('(', 1)
            if relation == 'root':
                continue
            first, second = first_second.split(', ', 1)
            first_node, second_node, relation_node = root.lca(first.rstrip("'"), second.rstrip("'"))
            print(relation, first_node.category, second_node.category, relation_node.category, file=file)
