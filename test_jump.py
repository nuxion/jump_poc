import binascii
import jump



class Algo:

    def __init__(self, shards):
        self.nodes = dict()
        self.shards = shards

    @staticmethod
    def compute(item, shards):
                return jump.hash(item, shards)

    def load(self, items):
        for i in items:
            encoded = i.strip().encode("utf-8")
            key = binascii.crc32(encoded) & 0xffffffff
            node = self.compute(key, self.shards)
            n = self.nodes.get(node)
            if n:
                self.nodes[node].append(key)
            else:
                self.nodes[node] = [key]

    def rebalance(self, shards):
        
        moves = 0
        for k in self.nodes.keys():
            for v in self.nodes[k]:
                new_node = self.compute(v, shards)
                if new_node != k:
                    print("Should be moved to: ", new_node)
                    moves += 1
        print("Total moves: ", moves)

    def print_status(self):
        for x in self.nodes.keys():
            print(len(self.nodes[x]))


alg = Algo(2)
with open("data.txt", "r") as f:
    items = f.readlines()
    alg.load(items)

alg.print_status()

alg.rebalance(3)
alg.print_status()

   
