""" Module BTree
A BTree implementation for educative purposes
"""
   
        
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
        """
        self.right=btree
        btree.parent=self

    def set_left(self, btree):
        """ set the left son
        btree must be a kind of tree
        """
        self.left=btree
        btree.parent=self

    def set_value(self, value):
        self.value=value

    def is_leaf(self):
        """ True if self is a leaf"""
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
        string = "N:"+self.__repr__()
        if self.left:
            string += "\n"+"-"*2*(self.depth()+1)+"L:"+self.left.pretty_print()
        if self.right:
            string += "\n"+"-"*2*(self.depth()+1)+"R:"+self.right.pretty_print()
        return string
       
    def __repr__(self):
        return str(self.value)
        
    

help(BTree)

tree = BTree(20)
tree.set_left(BTree(10))
tree.left.set_left(BTree(5))
tree.left.set_right(BTree(15))
tree.set_right(BTree(30))
tree.right.set_right(BTree(35))
print tree.pretty_print()


