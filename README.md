使用python实现剑指offer和leetcode上的题 </br>
==========
剑指offer
------
#### [面试题3](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/03_01_DuplicationInArray.py)：找数组中重复的数字 </br>
主要注意空间复杂度问题，给出了哈希表（O(n)）和换位法（O(1)）两种方法
#### [面试题4](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/04_FindInPartiallySortedMatrix.py)：有序二维数组查找 </br>
如果从数组中间开始查找，那么判断条件会很复杂，这里使用了书中给的提示，从数组的右上角进行判断，这样只需要分为三种情况。写代码时注意边界条件
#### [面试题5](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/05_ReplaceSpaces.py)：替换空格 </br>
对于python来说这个题是不能对str直接进行修改的，由于书中的思路是inplace方法，这里就按照书中的方法做了一个双指针的版本，同时写了一个字符串拼接的版本
#### [面试题6](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/06_PrintListInReversedOrder.py)：反向输出链表 </br>
思路是建一个栈，遍历一遍链表并把值放入栈里，遍历完之后从栈中pop出来并print
#### [面试题7](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/07_ConstructBinaryTree.py)：根据前序和中序遍历重建二叉树 </br>
思路是利用前序遍历的第一个value是根节点，而在中序遍历中分隔开了左右两个子树，因此可以利用递归的方法来进行求解
#### [面试题8](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/08_NextNodeInBinaryTrees.py)：给一个树，找中序遍历的下一个节点 </br>
这里可以根据中序遍历的特点（左→根→右）分为三种情况： </br>
1. 当前节点存在右子节点，那么下一个节点就是当前节点的右子树的最左子节点 
2. 当前节点无右子结点，那么下一个节点就是当前节点的父子节点  
3. 当前节点无右子节点，并且是父节点的右子节点，那么需要一直查找查找父节点是否是父节点的父节点的左子节点，
       如果存在那么下一个节点就是父节点的父节点 
#### [面试题9](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/09_QueueWithTwoStacks.py)：用栈实现队列  </br>
利用两个栈实现队列，一个栈用来接收输入（push），另一个栈用来输出（pop），输出时，当输出的栈为空，从输入的栈中把所有元素push入输出栈，再输出栈顶的元素；否则，输出栈顶值直到空为止。</br>
两个队列实现栈也是类似原理，输入时把元素放入有元素的队列1，输出时把队列1中元素放入另一个队列2中，当队列1长度为1时，输出的值就是最后一个元素
#### [面试题10](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/10_Fibonacci.py)：斐波那契数列的第n项  </br>
有三种解法，一种是最简单的三行递归：
'''
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
'''
这种方法效率太低，因此可以用查表法或者自下而上的递归来减少重复计算，就是第二种方法 <\br>
第三种方法是利用斐波那契的公式直接计算，时间复杂度是O(logn)，由于公式网上很容易就搜到了，就没有给出解法 <\br>
