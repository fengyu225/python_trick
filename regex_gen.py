class Node(object):
    # Trie node
    def __init__(self,c=""):
        self.char = c
        self.children = {}


class Trie(object):
    # Trie
    def __init__(self):
        self.root = Node();

    def insert(self, word):
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]


def build(root):
    # post order traversal building regex
    regs = [build(root.children[child]) for child in root.children]
    if root.char == '.':
        root.char = "\."
    if len(regs) == 0:
        return root.char
    if len(regs) == 1:
        return "{0}{1}".format(root.char, "|".join(regs))
    return "{0}(?:{1})".format(root.char, "|".join(regs))


def generate_regex(l):
    trie = Trie()
    for host in l:
        trie.insert(host)
    return build(trie.root)


if __name__ == "__main__":
    l = [
            "app1.tmol.ash1.websys.tmcs",
            "app2.tmol.ash1.websys.tmcs",
            "apt1.tmol.phx1.websys.tmcs",
            "app1.tmol.phx1.websys.tmcs"
        ]
    print generate_regex(l)
