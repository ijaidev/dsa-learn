class BSTNode:
    def get_min(self):
        min = self.left
        if min is None:
            return self.val
        while min.left is not None:
            min = min.left
        return min.val

    def get_max(self):
        max = self.right
        if max is None:
            return self.val
        while max.right is not None:
            max = max.right
        return max.val

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
