class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Btree:
    def __init__(self, root = None):
        self.root = Node(root)


    def insert(self, ptr, x):
        if ptr.val != None:
            if x > ptr.val:
                if ptr.right != None:
                    self.insert(ptr.right, x)
                else:
                    ptr.right = Node(x)
            elif x < ptr.val:
                if ptr.left != None:
                    self.insert(ptr.left, x)
                else:
                    ptr.left = Node(x)
        else:
            self.root = Node(x)

    def call_insert(self, x):
        self.insert(self.root, x)


    def inorder(self, ptr, output):
            if ptr != None:
                output = self.inorder(ptr.left, output)
                output.append(ptr.val)
                output = self.inorder(ptr.right, output)
            return output



    def postorder(self, ptr, output):

        if ptr != None:
                output = self.postorder(ptr.left, output)
                output = self.postorder(ptr.right, output)
                output.append(ptr.val)
        return output

    def preorder(self, ptr, output):

        if ptr != None:
                output.append(ptr.val)
                output = self.preorder(ptr.left, output)
                output = self.preorder(ptr.right, output)
        return output

    def search(self, ptr, x):
        if ptr != None:
            if ptr.val == x:
                return True
            elif ptr.val > x:
                return self.search(ptr.left, x)
            else:
                return self.search(ptr.right, x)

        else:
            return False
def main():
    tree = Btree()
    #Inserting items
    tree.call_insert(5)
    tree.call_insert(7)
    tree.call_insert(3)
    tree.call_insert(9)
    tree.call_insert(10)
    tree.call_insert(20)
    tree.call_insert(2)

    #searching for items
    print(tree.search(tree.root, 5))
    print(tree.search(tree.root, 10))
    print(tree.search(tree.root, 2))
    print(tree.search(tree.root, 89))
    print(tree.search(tree.root, 16))
    print(tree.search(tree.root, 20000))

    #In order traversal
    print(tree.inorder(tree.root, []))

    #Pre order traversal
    print(tree.preorder(tree.root, []))

    #Post order traversal
    print(tree.postorder(tree.root, []))

if __name__ == '__main__':
    main()
