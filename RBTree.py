# -*- coding: utf-8 -*-
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
        balance = self._balance_inserted(inserted)
        # print "{} inséré".format(balance.get_root())
        return balance.get_root()

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
        #print "rotate_left : "+ str(self.value)
        #print self.get_root()
        if not self.right:
            raise ValueError(
                "Self must have a non null right child to rotate left")
        s,r,rl,p=self, self.right, self.right.left, self.parent

        if p and s.is_left():
            p.set_left(r)
        elif p and s.is_right():
            p.set_right(r)
        else:
            r.parent=None
        s.set_right(rl)
        r.set_left(s)
        #print "rotated"
        #print self.get_root()


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
        if not self.left:
            raise ValueError(
                "Self must have a non null left child to rotate right")

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
            inserted = inserted.left
        elif self.is_left() and self.parent.is_right():
            inserted.parent._rotate_right()
            inserted = inserted.right
        inserted.parent.color=RB_BSTree.BLACK
        inserted._grand_parent().color=RB_BSTree.RED
        if inserted.is_left():
            inserted._grand_parent()._rotate_right()
        else:
            inserted._grand_parent()._rotate_left()
        # print self.get_root()
        return self

    def __repr__(self):
        return ('R' if self.color==RB_BSTree.RED else 'B') \
            + '_' + str(self.value)

    def checkRB(self):
        if not self.is_root():
            return self.get_root().checkRB()
        # Root is BLACK
        if not self.isBlack():
            print "root not black"
            return False
        # every RED node's father is BLACK
        for x in self:
            if x.isRed() and not x.parent.isBlack():
                print "two reds in line"
                return False
        # every path from leaf to root contains the same count of black nodes
        count_black=0
        for x in self:
            if not x.left or not x.right:
                count=1+len([n for n in x._iter_to_root() if n.isBlack()])
                if not count_black:
                    count_black=count
                else:
                    if count != count_black:
                        print "black count fail : {} - {} // {}".format(count, count_black, [n for n in x._iter_to_root()])
                        return False
        return True

    def _iter_to_root(self):
        yield self
        if self.parent:
            for x in self.parent._iter_to_root():
                yield x

if __name__=='__main__':
    help(SBTree)
    rTree=SBTree(5)
    rTree.insert(4).insert(8).insert(45).insert(0).insert(12)
    print rTree
    print list(rTree)

    #test rotation
    tree1=RB_BSTree('S')
    # tree1.set_left(RB_BSTree('1'))
    tree1.set_right(RB_BSTree('R'))
    # tree1.right.set_left(RB_BSTree('2'))
    # tree1.right.set_right(RB_BSTree('3'))
    print tree1.get_root()
    tree1._rotate_left()
    print tree1.get_root()
    tree1.get_root()._rotate_right()
    print tree1.get_root()

    print "-"*20

    import random

    rbTree=RB_BSTree(10)
    for i in xrange(20):
        ins = random.randint(0,100)
        rbTree.get_root().insert(ins)
        if not rbTree.checkRB():
            print "dernière insertion : " + str(ins)
            print rbTree.get_root()
            break
    print rbTree.get_root()
    print len(rbTree.get_root())
    print list(rbTree.get_root())
