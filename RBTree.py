from BTree import BTree

class SBTree(BTree):
    """ A Binary Search Tree. Not balanced"""

##    def __init__(self, **kwargs):
##        super(RBTree, self).__init__(**kwargs)

    def insert(self, element):
        if element<self.value:
            if self.left:
                self.left.insert(element)
            else:
                self.set_left(SBTree(element))
        else:
            if self.right:
                self.right.insert(element)
            else:
                self.set_right(SBTree(element))
        return self

class RB_BSTree(BTree):
    """ A Red and Black Binary Search Tree """

    BLACK=1
    RED=2

    def __init__(self, element, color=BLACK):
        BTree.__init__(self,element)
        self.color=color

    def isBlack(self):
        return self.color==RB_BSTree.BLACK

    def isRed(self):
        return self.color==RB_BSTree.RED

    def _simple_insert(self, element):
        if element<self.value:
            if self.left:
                return self.left._simple_insert(element)
            else:
                return self.set_left(RB_BSTree(element, RB_BSTree.RED))
        else:
            if self.right:
                return self.right._simple_insert(element)
            else:
                return self.set_right(RB_BSTree(element, RB_BSTree.RED))

    def _grand_parent(self):
        if self.is_root():
            return None
        else:
            return self.parent.parent

    def _uncle(self):
        gp = self._grand_parent()
        if gp:
            if self.parent is gp.left:
                return gp.right
            else:
                return gp.left
        return None

    def insert(self, element):
        #https://en.wikipedia.org/wiki/Red%E2%80%93black_tree#Insertion
        inserted = self._simple_insert(element)
        return self._balance_inserted(inserted)

    def _rotate_left(self):
        """
             P                 P    
           /   \             /   \
          S                 R
         / \               / \ 
        1   R       ==>   S   5
           / \           / \
          RL  5         1  RL  
        """
        
        s,r,rl,p=self, self.right, self.right.left, self.parent
        
        if p and s.is_left():
            p.set_left(r)
        elif p and s.is_right():
            p.set_right(r)
        else:
            r.parent=None
        s.set_right(rl)
        r.set_left(s) 

    def _rotate_right(self):
        """
             P                 P    
           /   \             /   \
          S                 L
         / \               / \ 
        L   5       ==>   1   S
       / \                   / \   
      1   LR                RL  5
        """
        s,l,lr,p=self, self.left, self.left.right, self.parent
        if p and s.is_left():
            p.set_left(l)
        elif p and p.is_right():
            p.set_right(l)
        else:
            l.parent=None
        s.set_left(lr)
        l.set_right(s)
        

    def _balance_inserted(self, inserted):
        print "Insertion {}", inserted
        print self
        if inserted.is_root() :
            inserted.color=RB_BSTree.BLACK
            return self
        elif inserted.parent.isBlack():
            return self
        elif inserted._uncle() and inserted._uncle().isRed():
            inserted.parent.color=RB_BSTree.BLACK
            inserted._uncle().color=RB_BSTree.BLACK
            inserted._grand_parent().color=RB_BSTree.RED
            return self._balance_inserted(inserted._grand_parent())
        elif self.is_right() and self.parent.is_left():
            inserted.parent._rotate_left()
        elif self.is_left() and self.parent.is_right():
            inserted.parent._rotate_right()
        inserted.parent.color=RB_BSTree.BLACK
        inserted._grand_parent().color=RB_BSTree.RED
        if inserted.is_left():
            inserted._grand_parent()._rotate_right()
        else:
            inserted._grand_parent()._rotate_left()
        print self
        return self

    def __repr__(self):
        return ('R' if self.color==RB_BSTree.RED else 'B') + '_' + str(self.value)


if __name__=='__main__':
    help(SBTree)
    rTree=SBTree(5)
    rTree.insert(4).insert(8).insert(45).insert(0).insert(12)
    print rTree
    print list(rTree)

    import random

    rbTree=RB_BSTree(10)
    for i in xrange(20):
        rbTree.insert(random.randint(0,100))
    print rbTree
    print list(rbTree)

