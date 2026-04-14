class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                return self.left
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
                return self.right
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        right_min = self.right
        while right_min is not None:
            right_min = right_min.left
        self.val = right_min.val
        self.right = self.right.delete(right_min.val)
        return self.val
        

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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
