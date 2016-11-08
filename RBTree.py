from BTree import BTree

class RBTree(BTree):
    """ A research Binary Tree. Not balanced"""

##    def __init__(self, **kwargs):
##        super(RBTree, self).__init__(**kwargs)

    def insert(self, element):
        if element<self.value:
            if self.left:
                self.left.insert(element)
            else:
                self.set_left(RBTree(element))
        else:
            if self.right:
                self.right.insert(element)
            else:
                self.set_right(RBTree(element))
        return self

rTree=RBTree(5)
rTree.insert(4).insert(8).insert(45).insert(0).insert(12)

print rTree.to_list()

rTree.insert('a')
