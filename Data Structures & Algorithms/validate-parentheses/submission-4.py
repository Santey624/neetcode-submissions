class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bucket_tokens = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in bucket_tokens:
                if not stack or stack.pop() != bucket_tokens[char]:
                    return False
            else:
                stack.append(char)
        return not stack