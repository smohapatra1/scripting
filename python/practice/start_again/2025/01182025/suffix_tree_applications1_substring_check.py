#   https://www.geeksforgeeks.org/suffix-tree-application-1-substring-check/

class SuffixTreeNode:
    def __init__(self, start, end, root):
        # Dictionary to hold children (edges out of this node)
        self.children = {}
        # Suffix link which points to another internal node (initially None)
        self.suffix_link = root
        # Start and end indices of the edge label from parent node to this node
        self.start = start
        self.end = end
        # Suffix index for leaf nodes (initially set to -1)
        self.suffix_index = -1

    def edge_length(self, current_pos):
        # Calculate edge length; use current_pos if it's a leaf (end is a reference to leafEnd)
        return self.end if isinstance(self.end, int) else current_pos - self.start + 1


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode(None, None, None)
        self.root.suffix_link = self.root
        self.last_new_node = None
        self.active_node = self.root
        self.active_edge = 0
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.leaf_end = -1
        self.size = len(text)
        self.build_suffix_tree()

    def build_suffix_tree(self):
        # Main function to build the suffix tree for the given text
        for i in range(self.size):
            self.extend_suffix_tree(i)

    def extend_suffix_tree(self, pos):
        # Rule 1 extension: Every suffix extension extends the leaf edges
        self.leaf_end = pos
        # Increment the count of suffixes we need to add
        self.remaining_suffix_count += 1
        # Active node handling
        self.last_new_node = None

        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = pos  # APCFALZ

            next_char = self.text[self.active_edge] if self.active_edge < len(
                self.text) else None

            # Check if there is an outgoing edge starting with the active edge character
            if next_char not in self.active_node.children:
                # Rule 2 extension: Create a new leaf node
                self.active_node.children[next_char] = SuffixTreeNode(
                    pos, self.leaf_end, self.root)

                if self.last_new_node is not None:
                    self.last_new_node.suffix_link = self.active_node
                    self.last_new_node = None
            else:
                next_node = self.active_node.children[next_char]
                # Walk down the tree if active length is longer than current edge length
                if self.active_length >= next_node.edge_length(pos):
                    self.active_edge += next_node.edge_length(pos)
                    self.active_length -= next_node.edge_length(pos)
                    self.active_node = next_node
                    continue

                # Rule 3 extension: Current character is already on the edge
                if self.text[next_node.start + self.active_length] == self.text[pos]:
                    if self.last_new_node is not None and self.active_node != self.root:
                        self.last_new_node.suffix_link = self.active_node
                    self.active_length += 1
                    break

                # Rule 2 extension again: Creating a new internal node
                split_end = next_node.start + self.active_length - 1
                split = SuffixTreeNode(next_node.start, split_end, self.root)

                self.active_node.children[next_char] = split
                split.children[self.text[pos]] = SuffixTreeNode(
                    pos, self.leaf_end, self.root)
                next_node.start += self.active_length
                split.children[self.text[next_node.start]] = next_node

                if self.last_new_node is not None:
                    self.last_new_node.suffix_link = split

                self.last_new_node = split

            # One suffix less to add
            self.remaining_suffix_count -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = pos - self.remaining_suffix_count + 1
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link

    def _do_traversal(self, node, string, idx):
        if node.start is not None:
            # Traverse edge character by character
            edge_len = node.edge_length(len(self.text) - 1)
            if self.text[node.start:node.start + edge_len] != string[idx:idx + edge_len]:
                return False
            idx += edge_len

        if idx == len(string):
            return True

        next_char = string[idx]
        if next_char in node.children:
            return self._do_traversal(node.children[next_char], string, idx)
        return False

    def check_substring(self, string):
        # Function to check if the string is a substring
        if self._do_traversal(self.root, string, 0):
            print(f"Pattern <{string}> is a Substring")
        else:
            print(f"Pattern <{string}> is NOT a Substring")

# Driver code


def main():
    st = SuffixTree("THIS IS A TEST TEXT$")
    queries = ["TEST", "A", " ", "IS A", " IS A ",
               "TEST1", "THIS IS GOOD", "TES", "TESA", "ISB"]
    for query in queries:
        st.check_substring(query)


if __name__ == "__main__":
    main()
