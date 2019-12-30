# Задание 2. Закодировать любую строку по алгоритму Хаффмана.

from collections import Counter, deque


DELIM = '-'*30


class HuffmanTree:
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

    def attach_right(self, node):
        self._right = node
        self.weight += node.weight

    def attach_left(self, node):
        self._left = node
        self.weight += node.weight

    def get_coding_table(self, prefix=''):
        node_list = deque()
        if self.symbol:
            print(f'"{self.symbol}": {prefix}')
            node_list.append((self.symbol, prefix, ))
        else:
            node_list.extend(self._right.get_coding_table(f'{prefix}1'))
            if self._left:
                node_list.extend(self._left.get_coding_table(f'{prefix}0'))
        return node_list


class HuffmanCoder:
    def __init__(self, content):
        if content == '':
            raise Exception("Невозможно кодировать пустую строку!")
        self._content = content
        self._freq_list = Counter(self._content)
        self._root = self._build_tree()
        code_q = self._root.get_coding_table()
        self._coder = {x[0]: x[1] for x in code_q}
        self._decoder = {x[1]: x[0] for x in code_q}
        self._content_coded = ''.join([self._coder[ch] for ch in self._content])

    def _build_tree(self):
        dq = deque([HuffmanTree(entry[1], entry[0]) for entry in self._freq_list.most_common()])
        dq.reverse()

        while len(dq) > 2:
            node_upper = HuffmanTree()
            node_upper.attach_left(dq.popleft())
            node_upper.attach_right(dq.popleft())
            print(node_upper)
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

        root = HuffmanTree()
        root.attach_right(dq.pop())
        if len(dq) > 0:
            root.attach_left(dq.pop())
        return root

    def get_dictionary(self):
        return self._decoder

    def get_encoded(self):
        return self._content_coded



# s1 = 'beep boop beer!'
s1 = input('Введите строку для кодирования: ')

h_enc = HuffmanCoder(s1)

saved_decoder = h_enc.get_dictionary()
coded_s = h_enc.get_encoded()
print(DELIM, f'str => {s1}', f'enc => {coded_s}', DELIM, sep='\n')

buffer = ''
decoded_s = ''
for c in coded_s:
    buffer += c
    if buffer in saved_decoder:
        decoded_s += saved_decoder[buffer]
        buffer = ''
print(f'dec => {decoded_s}')
assert s1 == decoded_s, 'Функция кодирования работает некорректно'
