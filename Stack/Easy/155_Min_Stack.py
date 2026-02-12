class MinStack:
    """
    MinStack supports push, pop, top, and retrieving
    the minimum element in constant time.
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        """Push element onto stack."""
        self.stack.append(val)

        # Push into minStack if it's the new minimum
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> int:
        """Remove and return the top element."""
        if not self.stack:
            return None

        val = self.stack.pop()

        # Remove from minStack if needed
        if val == self.minStack[-1]:
            self.minStack.pop()

        return val

    def top(self) -> int:
        """Return the top element."""
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """Retrieve the minimum element."""
        return self.minStack[-1] if self.minStack else None


# -------------------
# Example Usage
# -------------------
if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.push(2)
    obj.push(-1)

    print("Current Stack:", obj.stack)
    print("Minimum Element:", obj.getMin())

    obj.pop()
    print("Minimum After Pop:", obj.getMin())
