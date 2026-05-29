class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "{":"}",
            "(":")",
            "[":"]"
        }
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
                continue
            else:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[top] != bracket:
                    return False
        if stack:
            return False
        return True

