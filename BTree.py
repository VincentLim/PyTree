""" Module BTree
A BTree implementation for educative purposes
"""
from itertools import izip   
        
class BTree(object):
    """ A Btree is compound of a left BTree, a right BTree, a value and a parent"""

    def __init__(self, value=None, parent=None):
        """ init a BTree with one node"""
        self.right=None
        self.left=None
        self.value=value
        self.parent=None

    def set_right(self, btree):
        """ set the right son
        btree must be a kind of tree
        returns the inserted Node
        """
        self.right=btree
        if btree:
            #in case of setting right to None
            btree.parent=self
        return btree

    def set_left(self, btree):
        """ set the left son
        btree must be a kind of tree
        returns the inserted Node
        """
        self.left=btree
        if btree:
            #in case of setting left to None
            btree.parent=self
        return btree

    def set_value(self, value):
        self.value=value

    def is_root(self):
        return self.parent is None

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        else:
            return self

    def is_leaf(self):
        """ True if self is a leaf"""
        return self.right is None and self.left is None

    def is_left(self):
        return self.parent and self is self.parent.left

    def is_right(self):
        return self.parent and self is self.parent.right

    def depth(self):
        if self.parent is None:
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
        lr = 0 if self.right is None else self.right.__len__()
        ll = 0 if self.left is None else self.left.__len__()
        return 1+lr+ll

    def __iter__(self):
        """ inorder iteration """
        return self.inorder_iter()

    def inorder_iter(self, reverse=False):
        """ inorder iteration
        reverse=False. True to start from right
        """
        if not reverse:
            if self.left:
                for x in self.left.inorder_iter(reverse):
                    yield x
        else:
            if self.right:
                for x in self.right.inorder_iter(reverse):
                   yield x
        yield self
        if not reverse:
            if self.right:
                for x in self.right.inorder_iter(reverse):
                    yield x
        else:
            if self.left:
                for x in self.left.inorder_iter(reverse):
                    yield x

    def preorder_iter(self):
        yield self
        if self.left:
            for x in self.left.preorder_iter():
                yield x
        if self.right:
            for x in self.right.preorder_iter():
                yield x

    def postorder_iter(self):
        if self.left:
            for x in self.left.postorder_iter():
                yield x
        if self.right:
            for x in self.right.postorder_iter():
                yield x
        yield self

    def __str__(self):
        return self.pretty_print()

    def pretty_print(self):
        string = "("+self.__repr__()+")"
        if self.left:
            string += "\n"+"-"*2*(self.depth()+1)+"L:"+self.left.pretty_print()
        if self.right:
            string += "\n"+"-"*2*(self.depth()+1)+"R:"+self.right.pretty_print()
        return string
       
    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        """"""
        #simple and maybe false
        if other is None or self.value != other.value:
            return False
        if self.left != other.left or self.right!=other.right:
            return False
        return True

    def __ne__(self, other):
        return not (self==other)
    
if __name__=='__main__':
    help(BTree)

    tree = BTree(20)
    tree.set_left(BTree(10))
    tree.left.set_left(BTree(5))
    tree.left.set_right(BTree(15))
    tree.set_right(BTree(30))
    tree.right.set_right(BTree(35))

    otree = BTree(20)
    otree.set_left(BTree(10))
    otree.left.set_left(BTree(5))
    otree.left.set_right(BTree(15))
    otree.set_right(BTree(30))
    otree.right.set_right(BTree(35))
    
    print tree.pretty_print()

    if not tree.is_root():
        print "Test erreur : is_root"
    if not tree.left.left.is_leaf():
        print "Test erreur : is_leaf"
    if len(tree)!=6:
        print "Test erreur : len"

    print tree == otree
