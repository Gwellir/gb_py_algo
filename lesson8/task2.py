# Задание 2. Закодировать любую строку по алгоритму Хаффмана.

from collections import Counter, deque


DELIM = '-'*30


class WeightedTree:
    def __init__(self, weight=0, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.weight = weight
        self._left = left
        self._right = right

    def __repr__(self):
        left = self._left if self._left else '..'
        right = self._right if self._right else '..'
        symbol = f'"{self.symbol}"' if self.symbol else '..'
        return f'{symbol}:{self.weight} [{left}] [{right}]'

    def __str__(self):
        left = self._left if self._left else '..'
        right = self._right if self._right else '..'
        symbol = f'"{self.symbol}"' if self.symbol else '..'
        return f'{symbol}:{self.weight} [{left}] [{right}]'

    def attach_right(self, node):
        self._right = node
        self.weight += node.weight

    def attach_left(self, node):
        self._left = node
        self.weight += node.weight

    def get_table(self, prefix=''):
        table = deque()
        if self.symbol:
            print(f'"{self.symbol}": {prefix}')
            table.append((self.symbol, prefix, ))
        else:
            table.extend(self._right.get_table(prefix + '1'))
            if self._left:
                table.extend(self._left.get_table(prefix + '0'))
        return table


def build_tree(dq):
    while len(dq) > 2:
        node_upper = WeightedTree()
        node_upper.attach_left(dq.popleft())
        node_upper.attach_right(dq.popleft())
        # print(node_upper)
        dq_head = deque()
        while True:
            curr_node = dq.popleft()
            if curr_node.weight >= node_upper.weight:
                dq_head.append(node_upper)
                dq_head.append(curr_node)
                dq_head.extend(dq)
                dq = dq_head
                break
            elif len(dq) == 0:
                dq_head.append(curr_node)
                dq_head.append(node_upper)
                dq = dq_head
                break
            else:
                dq_head.append(curr_node)

    root = WeightedTree()
    root.attach_right(dq.pop())
    if len(dq) > 0:
        root.attach_left(dq.pop())
    return root


# s1 = 'beep boop beer!'
s1 = input('Введите строку для кодирования: ')
count1 = Counter(s1)
print(count1)
dq_weights = deque([WeightedTree(entry[1], entry[0]) for entry in count1.most_common()])
dq_weights.reverse()

root = build_tree(dq_weights)

coding_deque = root.get_table()
coder = {x[0]: x[1] for x in coding_deque}
decoder = {x[1]: x[0] for x in coding_deque}

coded_s = ''.join([coder[c] for c in s1])
print(DELIM, f'str => {s1}', f'enc => {coded_s}', DELIM, sep='\n')

buffer = ''
decoded_s = ''
for c in coded_s:
    buffer += c
    if buffer in decoder:
        decoded_s += decoder[buffer]
        buffer = ''
print(f'dec => {decoded_s}')
assert s1 == decoded_s, 'Функция кодирования работает некорректно'
