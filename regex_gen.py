import sys

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
        curr_node.children["$"] = Node("$")


def is_balanced(s):
    stack = []
    for c in s:
        if c=='(':
            stack.append(c)
        elif c==')':
            if stack == []:
                return False
            stack.pop()
    return stack==[]


def get_longest_common_suffix(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return len(l[0])
    i = 1
    while i<=len(l[0]):
        flag = False
        c = l[0][-1*i]
        for lx in l[1:]:
            if len(lx)<i or lx[-1*i] != c:
                flag = True
                break 
        if flag:
            break
        i+=1
    while l[0][-1*(i-1)] == ")":
        i-=1
    return 0 if i-1>0 and not is_balanced(l[0][-1*(i-1):len(l[0])]) else i-1


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
    suffix = regs[0][-1*common_suffix_len:len(regs[0])] if common_suffix_len>0 else ""
    regs = [s[0:len(s)-common_suffix_len] for s in regs]
    return "{0}(?:{1}){2}".format(root.char, "|".join(regs), suffix)


def generate_regex(l):
    trie = Trie()
    for host in l:
        trie.insert(host)
    return build(trie.root)


if __name__ == "__main__":
    if len(sys.argv)<2:
        print "pass file path as first var"
        sys.exit(1)
    l = []
    with open(sys.argv[1], "r") as f:
        l = [h.strip() for h in f]
    print generate_regex(l)
