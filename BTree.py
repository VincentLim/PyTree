""" Module BTree
A BTree implementation for educative purposes
"""

class _BTreeIterator:
    """ Infixe Iterator for a BTree"""

    def __init__(self, root):
        self.current=root
        self.left_it = _BTreeIterator(root.left) if root.left else None
        self.right_it = _BTreeIterator(root.right) if root.right else None

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

    def to_list(self):
        return [x.value for x in self] 

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        string = "N:"+self.__str__()
        if self.left:
            string += "\n"+"-"*(self.depth()+2)+"L:"+self.left.__repr__()
        if self.right:
            string += "\n"+"-"*(self.depth()+2)+"R:"+self.right.__repr__()
        return string
       
        
        
    

    

tree = BTree(2)
tree.set_left(BTree(1))
tree.set_right(BTree(3))


