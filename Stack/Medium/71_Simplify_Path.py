class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" if not stack else "/" + "/".join(stack)


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.simplifyPath("/home//foo/"))  # Output: "/home/foo"
