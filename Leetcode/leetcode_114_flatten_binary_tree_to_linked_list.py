from binary_tree import create_btree_with_list
from collections import deque


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        """
        2 Steps:
        1. Since the problem want a DFS way to print the tree
           we shall first use a recursive function to save each 
           nodes into a stack(a first come last out array)
        2. Next,use a BFS way to write each level of the tree, 
           each time, pop out the 1st element as the right node's value
           and come to the next level calling the writing function itself.
        """
        if root:
            result_stack = deque()
            self.dfs_tree_to_stack(root, result_stack)
            #return(result_stack)
            result_stack.popleft()
            self.stack_2_tree(root, result_stack)
            #return(root)
        


        
    """
    dfs_tree_to_array function takes a tree's root,
    and export an array recording the node's value 
    from top to leaf, left to right
    """
    def dfs_tree_to_array(self, root, result):
        # result as global variable
        if not root:
            return(result)
        result.append(root.value)
        if root.left:
            result = self.dfs_tree_to_array(root.left, result)         
        if root.right:
            result = self.dfs_tree_to_array(root.right, result)       
        return(result)
        """
        The biggest problem of this solution is that, it skip
        the empty nodes in the tree, meaning that with the output 
        list, cannot re-create the tree.
        """

    def dfs_tree_to_array_II(self, root, result):
        # How to not skip a empty child node but does not
        # influence when both child nodes are empty(leaf)
        if not root:
            return(result.append(None))

        result.append(root.value)

        if not root.left and not root.right:
            return(result)
        
        self.dfs_tree_to_array_II(root.left, result)
        self.dfs_tree_to_array_II(root.right,result)

        
        """
        do not use :

        ```
        try:
            result = self.dfs_tree_to_array_II(root.left, result)
            result = self.dfs_tree_to_array_II(root.right,result)
        except:
            print(root) # 5 -> 6
            print(result) # None
        ```

        it will stuck at [1,2,3,4,5,None]
        because after running
        result = self.dfs_tree_to_array_II(root.left, result)
        result will be None rather than [1,2,3,4,5],
        and by running the next statement:
        result = self.dfs_tree_to_array_II(root.right, result)
        It will not allow you to append root.right to result which is None
        """
        return(result)

    """
    Inplace Operation:
    hat is an operation that modifies the object and returns nothing
    """
    # Skip Empty Child Nodes
    def dfs_tree_to_stack(self, root, result_stack):

        if not root:
            return(result_stack)
            #pass
        result_stack.append(root)
        if root.left:
            self.dfs_tree_to_stack(root.left, result_stack)    
        if root.right:
            self.dfs_tree_to_stack(root.right, result_stack)
        return(result_stack)

    # Keep record of Empty Child Nodes
    def dfs_tree_to_stack_II(self, root, result_stack):
        if not root:
            return(result_stack.append(None))

        result_stack.append(root)

        if not root.left and not root.right:
            return(result_stack)

        self.dfs_tree_to_stack_II(root.left, result_stack)
        self.dfs_tree_to_stack_II(root.right, result_stack)
        return(result_stack)

    def stack_2_tree(self, root, result_stack):
        if result_stack:
            root.left = None
            root.right = result_stack.popleft()
            self.stack_2_tree(root.right, result_stack)
        else:
            return(root)


        


data = [1,2,5,3,4,None,6]
tree = create_btree_with_list(data)
print(tree)
s = Solution()
s.flatten(tree)
print(tree)

        