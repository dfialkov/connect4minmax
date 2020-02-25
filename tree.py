class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []
    def addChild(self, child):
        self.children += child