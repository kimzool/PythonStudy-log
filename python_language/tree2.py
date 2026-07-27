class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
print("루트",root.data)
print("왼쪽",root.left.data)
print("오른쪽",root.right.data)


# --------

class TreeNode2:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# 노드 생성
root = TreeNode2(10)

root.left = TreeNode2(20)
root.right = TreeNode2(30)

root.left.left = TreeNode2(40)
root.left.right = TreeNode2(50)

root.right.left = TreeNode2(60)
root.right.right = TreeNode2(70)

print("루트",root.data)
print("2단계 자식 : ",root.left.data,root.right.data)
print("3단계 자식 : ",root.left.left.data,root.left.right.data,root.right.left.data,root.right.right.data)

# 전위순회
# 루트 -> 왼쪽 -> 오른쪽

def preorder(node):
    if node is not None:
        print(node.data,end = "")
        preorder(node.left)
        preorder(node.right)
print("전위순회")
preorder(root)

def inorder(node):
    if node is not None:
        preorder(node.left)
        print(node.data,end = "")
        preorder(node.right)
print("중위순회")
preorder(root)

def postorder(node):
    if node is not None:
        preorder(node.right)
        preorder(node.left)
        print(node.data,end ="")
print("후위순회")
postorder(root)