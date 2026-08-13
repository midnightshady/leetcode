class Solution {

    class Node {
        int maxLen;
        int prefixLen;
        int suffixLen;
        char firstChar;
        char lastChar;
        int len;

        Node(char c) {
            maxLen = 1;
            prefixLen = 1;
            suffixLen = 1;
            firstChar = c;
            lastChar = c;
            len = 1;
        }

        Node() {}
    }

    Node[] tree;
    char[] chars;

    public int[] longestRepeating(
        String s,
        String queryCharacters,
        int[] queryIndices
    ) {

        int n = s.length();
        int k = queryIndices.length;

        chars = s.toCharArray();
        tree = new Node[4 * n];

        // Build Segment Tree
        build(1, 0, n - 1);

        int[] ans = new int[k];

        for (int i = 0; i < k; i++) {

            int index = queryIndices[i];
            char ch = queryCharacters.charAt(i);

            // Update character
            chars[index] = ch;

            update(1, 0, n - 1, index, ch);

            // Root represents the complete string
            ans[i] = tree[1].maxLen;
        }

        return ans;
    }

    private void build(int node, int start, int end) {

        // Leaf node
        if (start == end) {
            tree[node] = new Node(chars[start]);
            return;
        }

        int mid = start + (end - start) / 2;

        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);

        tree[node] = merge(
            tree[2 * node],
            tree[2 * node + 1]
        );
    }

    private void update(
        int node,
        int start,
        int end,
        int index,
        char ch
    ) {

        // Leaf node
        if (start == end) {
            tree[node] = new Node(ch);
            return;
        }

        int mid = start + (end - start) / 2;

        if (index <= mid) {
            update(2 * node, start, mid, index, ch);
        } else {
            update(2 * node + 1, mid + 1, end, index, ch);
        }

        // Recalculate current node
        tree[node] = merge(
            tree[2 * node],
            tree[2 * node + 1]
        );
    }

    private Node merge(Node left, Node right) {

        Node res = new Node();

        res.len = left.len + right.len;

        res.firstChar = left.firstChar;
        res.lastChar = right.lastChar;

        // Initially, answer is either in left or right
        res.maxLen = Math.max(
            left.maxLen,
            right.maxLen
        );

        res.prefixLen = left.prefixLen;
        res.suffixLen = right.suffixLen;

        // Boundary characters are same
        if (left.lastChar == right.firstChar) {

            // A repeating sequence can cross the boundary
            res.maxLen = Math.max(
                res.maxLen,
                left.suffixLen + right.prefixLen
            );

            // Entire left segment is same character
            if (left.prefixLen == left.len) {
                res.prefixLen =
                    left.len + right.prefixLen;
            }

            // Entire right segment is same character
            if (right.suffixLen == right.len) {
                res.suffixLen =
                    right.len + left.suffixLen;
            }
        }

        return res;
    }
}