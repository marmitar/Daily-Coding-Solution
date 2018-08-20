import regex as re

def serialize(root, order="inorder", envelope='()'):
    def env(s):
        return envelope[0] + s + envelope[1]

    if root == None:
        return ''

    s1 = ""
    s2 = ""
    s3 = ""

    if order == "preorder":
        s1 = str(root.val)
        s2 = serialize(root.left, "preorder", envelope)
        s3 = serialize(root.right, "preorder", envelope)

    elif order == "inorder":
        s1 = serialize(root.left, "inorder", envelope)
        s2 = str(root.val)
        s3 = serialize(root.right, "inorder", envelope)

    elif order == "postorder":
        s1 = serialize(root.left, "postorder", envelope)
        s2 = serialize(root.right, "postorder", envelope)
        s3 = str(root.val)

    else:
        raise Exception("Order Unknown")

    return env(s1) + env(s2) + env(s3)


def deserialize(s, order="inorder", envelope='()', matcher=None):
    if s == '':
        return None

    if matcher == None:
            pattern = "{0}([^{0}{1}]*+(?:(?R)[^{0}{1}]*)*+){1}".format(re.escape(envelope[0]), re.escape(envelope[1]))
            matcher = re.compile(pattern)

    s1, s2, s3 = matcher.findall(s)

    val = ""
    left = None
    right = None
    
    if order == "preorder":
        val = s1
        left = deserialize(s2, "preorder", envelope, matcher)
        right = deserialize(s3, "preorder", envelope, matcher)

    elif order == "inorder":
        left = deserialize(s1, "inorder", envelope, matcher)
        val = s2
        right = deserialize(s3, "inorder", envelope, matcher)

    elif order == "postorder":
        left = deserialize(s1, "postorder", envelope, matcher)
        right = deserialize(s2, "postorder", envelope, matcher)
        val = s3

    else:
        raise Exception("Order Unknown")

    return Node(val, left, right)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, order="inorder", envelope='()'):
        return serialize(self, order, envelope)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node, "preorder"))
print(serialize(node, "inorder"))
print(serialize(node, "postorder"))

assert deserialize(serialize(node, "preorder"), "preorder").left.left.val == 'left.left'
assert deserialize(serialize(node, "inorder"), "inorder").left.left.val == 'left.left'
assert deserialize(serialize(node, "postorder"), "postorder").left.left.val == 'left.left'