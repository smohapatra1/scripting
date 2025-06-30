#   https://www.google.com/search?q=How+will+you+convert+the+ternary+expression+to+a+binary+tree%3F+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifMowomqsincSVZ6LqK1cOHV2XDVLg%3A1751257010094&ei=sg9iaNSXBZSZwbkPv9Kd0AE&ved=0ahUKEwjUuPzfpJiOAxWUTDABHT9pBxoQ4dUDCBE&uact=5&oq=How+will+you+convert+the+ternary+expression+to+a+binary+tree%3F+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiSkhvdyB3aWxsIHlvdSBjb252ZXJ0IHRoZSB0ZXJuYXJ5IGV4cHJlc3Npb24gdG8gYSBiaW5hcnkgdHJlZT8gdXNpbmcgcHl0aG9uSNUcUABYiRpwAHgAkAEAmAGgAaAB4AyqAQQwLjE0uAEDyAEA-AEC-AEBmAICoAK_AsICBBAAGB6YAwCSBwMwLjKgB7wNsgcDMC4yuAe_AsIHBTMtMS4xyAcn&sclient=gws-wiz-serp

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Solution:
    def convert_ternary_to_binary(self, expression:str) -> Node:
        self.index = 0 
        def build_tree_recursive ():
            if self.index >= len(expression):
                return None
            current_char = expression[self.index]
            node = Node(current_char)
            self.index += 1 
            if self.index < len(expression) and expression[self.index] == '?':
                self.index += 1  # Move past '?'
                node.left = build_tree_recursive()
            if self.index < len(expression) and expression[self.index] == ':':
                self.index += 1  # Move past ':'
                node.right = build_tree_recursive()
            return node
        return build_tree_recursive()

solver = Solution()
root = solver.convert_ternary_to_binary("a?b:c") 