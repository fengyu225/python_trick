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

import pdb
def get_longest_common_suffix(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return len(l[0])
    i = 1
    while True:
        c = l[0][-1*i]
        for lx in l[1:]:
            if len(lx)<i or lx[-1*i] != c:
                return i-1
        i+=1


def build(root):
    # post order traversal building regex
    regs = [build(root.children[child]) for child in root.children]
    if root.char == '.':
        root.char = "\."
    if len(regs) == 0:
        return root.char
    if len(regs) == 1:
        return "{0}{1}".format(root.char, "|".join(regs))
    common_suffix_len = get_longest_common_suffix(regs)
    suffix = regs[0][-1*common_suffix_len:len(regs[0])]
    regs = [s[0:len(s)-common_suffix_len] for s in regs]
    return "{0}(?:{1}){2}".format(root.char, "|".join(regs), suffix)


def generate_regex(l):
    trie = Trie()
    for host in l:
        trie.insert(host)
    return build(trie.root)


if __name__ == "__main__":
    l = [
            "app1.tmol.ash1.websys.tmcs",
            "app1.tmol.euash1.websys.tmcs",
            "app2.tmol.ash1.websys.tmcs",
            "apt1.tmol.phx1.websys.tmcs",
            "app1.tmol.phx1.websys.tmcs"
        ]
#    l = [
#            "apt18.tmol.ash1.websys.tmcs",
#            "apt19.tmol.ash1.websys.tmcs",
#            "apt20.tmol.ash1.websys.tmcs",
#            "apt21.tmol.ash1.websys.tmcs",
#            "apt22.tmol.ash1.websys.tmcs",
#            "apt23.tmol.ash1.websys.tmcs",
#            "apt24.tmol.ash1.websys.tmcs",
#            "apt25.tmol.ash1.websys.tmcs",
#            "apt26.tmol.ash1.websys.tmcs",
#            "apt27.tmol.ash1.websys.tmcs",
#            "apt28.tmol.ash1.websys.tmcs",
#            "apt29.tmol.ash1.websys.tmcs",
#            "apt30.tmol.ash1.websys.tmcs",
#            "apt31.tmol.ash1.websys.tmcs",
#            "apt32.tmol.ash1.websys.tmcs",
#            "apt33.tmol.ash1.websys.tmcs",
#            "apt34.tmol.ash1.websys.tmcs"
#        ]
    print generate_regex(l)
