# coding=utf-8
"""Huffman Coding Python implementation."""


class Node:
    def __init__(self, code, frequency):
        self.code = code
        self.frequency = frequency
        self.left_child = None
        self.right_child = None


class HuffmanTree:
    def __init__(self, frequency_table):
        self.frequency_table = frequency_table
        self.heap = []
        self.minimum = None
        self.codes = {}

    def construct(self):
        self.heap = []
        for code in self.frequency_table:
            n = Node(code[0], code[1])
            self.heap.append(n)
            if self.minimum:
                if self.minimum.frequency > n.frequency:
                    self.minimum = n
            else:
                self.minimum = n
        while len(self.heap) > 1:
            extracted1 = self.minimum
            self.heap.remove(extracted1)
            self.minimum = None
            for n in self.heap:
                if self.minimum:
                    if self.minimum.frequency > n.frequency:
                        self.minimum = n
                else:
                    self.minimum = n
            extracted2 = self.minimum
            self.heap.remove(extracted2)

            new_node = Node(None, extracted1.frequency + extracted2.frequency)
            new_node.left_child = extracted1
            new_node.right_child = extracted2
            self.heap.append(new_node)
            self.minimum = None
            for n in self.heap:
                if self.minimum:
                    if self.minimum.frequency > n.frequency:
                        self.minimum = n
                else:
                    self.minimum = n

    def gen_codes(self):
        to_visit = [(self.heap[0], "")]
        while to_visit:
            visiting = to_visit.pop(0)
            if visiting[0]:
                if visiting[0].code:
                    self.codes[visiting[0].code] = visiting[1]
                to_visit.append((visiting[0].left_child, visiting[1] + "0"))
                to_visit.append((visiting[0].right_child, visiting[1] + "1"))

    def encode(self, message):
        return "".join([self.codes[c] for c in message])


if __name__ == "__main__":
    freq_tb = [
       ['a',  5],
       ['b', 9  ],
       ['c', 12],
       ['d', 13],
       ['e', 16],
       ['f', 45]]
    ht = HuffmanTree(freq_tb)
    ht.construct()
    print(ht.heap)
    ht.gen_codes()
    print(ht.codes)
    print(ht.encode("aabddddefdffdaaabee"))
