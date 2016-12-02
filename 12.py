#include <iostream>
 
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
  
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)

def in_order_New(tree):
  node=tree
  pile=[]
  while True:
    if node!=None:
      pile.append(node)
      node=node.left
    else:
      if len(pile)>0:
        print(pile[len(pile)-1].value)
        node=pile[len(pile)-1].right
        del pile[len(pile)-1]
      else:
        break
      
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print ("1", tree.value)
    if(tree.right!=None):
        in_order(tree.right)
        
def preorder(tree):
    print (tree.value)
    if tree.left!=None:
        preorder(tree.left)
    if tree.right!=0:
        preorder(tree.right)
        
def tree_sort(tree,Input):
    for i in range(0,len(Input)):
      tree_insert(tree,Input[i])
    in_order_New(tree)
    
if __name__ == '__main__':
  Input=[10,5,2,3,4,11]
  t=tree_insert(None,6);
  tree_sort(t,Input)
#  tree_insert(t,10)
 # tree_insert(t,5)
 # tree_insert(t,2)
 # tree_insert(t,3)
  #tree_insert(t,4)
 # tree_insert(t,11)
 # tree_sort(t)