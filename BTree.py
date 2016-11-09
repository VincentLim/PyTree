""" Module BTree
A BTree implementation for educative purposes
"""

class _BTreeIterator:
    """ Infixe Iterator for a BTree"""

    def __init__(self, root):
        self.current=root
        self.left_it = self.__class__(root.left) if root.left else None
        self.right_it = self.__class__(root.right) if root.right else None

    def __iter__(self):
        return self

    def next(self):
        if self.left_it:
            try:
                return self.left_it.next()
            except StopIteration:
                pass# Continue to node
        if self.current:
            node = self.current
            self.current = None
            return node
        if self.right_it:
            return self.right_it.next()
        else:
            raise StopIteration


class _ReverseBTreeIterator():
    def generator(self, root):
        if root.right:
            for x in root.right.iter(True):
                yield x
        yield root
        if root.left:
            for x in root.left.iter(True):
                yield x
        
        
class BTree(object):
    """ A Btree is compound of a left BTree, a right BTree, a value and a parent"""



    def __init__(self, value=None, parent=None):
        """ init a BTree with one node"""
        self.right=None
        self.left=None
        self.value=value
        self.parent=None

    def set_right(self, btree):
        if not isinstance(btree, BTree):
            raise TypeError('Argument must be a BTree')
        self.right=btree
        btree.parent=self

    def set_left(self, btree):
        if not isinstance(btree, BTree):
            raise TypeError('Argument must be a BTree')
        self.left=btree
        btree.parent=self

    def set_value(self, value):
        self.value=value

    def is_leaf(self):
        return self.right==None and left.right==None

    def depth(self):
        if self.parent==None:
            return 0
        return 1+self.parent.depth()

    def remove(self):
        """ delete nodes from this node and downward"""
        #clear left
        if self.left:
            self.left.remove()
        # clear right
        if self.right:
            self.right.remove()
        #clear link in parent
        if self.parent.left is self:
            self.parent.left=None
        if self.parent.right is self:
            self.parent.right=None
        self=None


    def __len__(self):
        lr = 0 if self.right==None else self.right.__len__()
        ll = 0 if self.left==None else self.left.__len__()
        return 1+lr+ll

    def __iter__(self):
        """ infixe iteration """
        return _BTreeIterator(self)

    def iter(self, reverse=False):
        if reverse:
            return _ReverseBTreeIterator().generator(self)
        else:
            return self.__iter__()

    def to_list(self):
        return [x.value for x in self] 

    def __str__(self):
        return self.pretty_print()

    def pretty_print(self):
        string = "N:"+self.__repr__()
        if self.left:
            string += "\n"+"-"*2*(self.depth()+1)+"L:"+self.left.pretty_print()
        if self.right:
            string += "\n"+"-"*2*(self.depth()+1)+"R:"+self.right.pretty_print()
        return string
       
    def __repr__(self):
        return str(self.value)
        
    

    

tree = BTree(20)
tree.set_left(BTree(10))
tree.left.set_left(BTree(5))
tree.left.set_right(BTree(15))
tree.set_right(BTree(30))
tree.right.set_right(BTree(35))


