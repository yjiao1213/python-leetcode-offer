使用python实现剑指offer和leetcode</br>
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
```python
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
```
这种方法效率太低，因此可以用查表法或者自下而上的递归来减少重复计算，就是第二种方法  </br>
第三种方法是利用斐波那契的公式直接计算，时间复杂度是O(logn)，由于公式网上很容易就搜到了，就没有给出解法
#### [面试题11](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/11_MinNumberInRotatedArray.py)：旋转数组的最小数字  </br>
由于数组在旋转之前是有序的，因此可以使用二分查找使时间复杂度为O(logn) <\br>
首先去两个指针left和right分别指向数组头和数组尾，然后计算中间的指针mid，可以分为两种情况：
1. mid指向的数字大于left指向的数字，说明最小的数字在mid右边，那么left指向mid  
2. mid指向的数字小于right指向的数字，说明最小的数字在左边的部分  
**left指向左边的数列，right指向的是右边的数列，那么当left和right相邻时就可以找到最小的数，为right指向的数字**
然后需要思考两种特殊情况，第一种就是当这个数列没有被旋转时，最右的数字为最小，第二种是当重复的数字太多，导致left=mid=right，这时需要遍历整个数组来找到最小值。
#### [面试题12](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/12_StringPathInMatrix.py)：矩阵中的路径  </br>
这里假设按照字符串的顺序寻找路径，解法为定义一个同样大小的bool类型数组用来保存节点状态（路径是否已被经过），然后利用回溯法求解  </br>
遍历matrix寻找第一个字符所在位置。假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的第i个字符。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子外，其他各自都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
#### [面试题13](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/13_RobotMove.py)：Robot Move  </br>
与上一题类似，使用回溯法来判断机器人能够走过的位置，这里需要计算能够到达的格子数量，因次代码会有略微的区别。
#### [面试题14](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/14_CuttingRope.py)：剪绳子  </br>
动态规划和贪心算法两种解:  </br>
DP:使用自下而上的动态规划，并保存下来每次的结果，可以避免重复运算 </br>
Greedy:把每一段绳子分为n个长度为3的部分时，结果最大，因此使用动态规划，每次截取3. </br>
贪心的数学公式是：当n>=5时，2(n-2)>n，3(n-3)>n,因此意味着当分为3和2时，乘积的大小要大于不分割时候的值，又因为2(n-2)<3(n-3), 因此应该长度为3时剪一次  </br>
#### [面试题15](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/15_NumberOf1InBinary.py)：二进制中1的个数  </br>
主要是进行二进制的处理，注意输入的数字为负数时，要先进行转换再取值。书上给的思路是把当原数减一时，其实是把最右边的1置为0，那么再与原数做与操作就可以减掉一个1，循环直到原数为零。很tricky的方法  </br>
#### [面试题16](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/16_Power.py)：数值的整数次方  </br>
可以适用递归减少运算，当计算的当前的exponent时，只需要计算exponent/2时的值就可以，利用二进制的移位运算来减少运算时间。   </br>
#### [面试题17](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/17_Print1ToMaxOfNDigits.py)：打印从1到最大的n位数  </br>
注意大数问题，用字符串做加法，注意输出是不要输出数字前面的0   </br>
#### [面试题18](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/18_01_DeleteNodeInList.py)：O(1)时间删除链表结点  </br>
注意区分3种情况 1.删除的是头节点 2.删除的是尾节点（这时需要从头开始遍历）3.删除的是其他节点（直接把这个结点的next的参数赋给这个结点，再删除下一个结点）   </br>
#### [面试题19](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/19_RegularExpressionsMatching.py)：正则表达式匹配  </br>
注意匹配星号时，要分为三种情况   </br>
#### [面试题20](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/20_NumericStrings.py)：判断字符串是否表示数值  </br>
把字符分为几部分分别进行判断   </br>
#### [面试题21](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/21_ReorderArray.py)：奇数排在偶数前面  </br>
用双指针分别从数组头和数组尾部进行遍历互换   </br>
#### [面试题22](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/22_KthNodeFromEnd.py)：链表中倒数第k个结点  </br>
两个指针，第二个指针等第一个指针走了k-1步时开始走，注意边界条件   </br>
#### [面试题23](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/23_EntryNodeInListLoop.py)：链表中环的入口节点  </br>
先判断是否有环，快慢指针，如果相遇，那么有环   </br>
然后从相遇位置和链表头同时开始遍历，相遇时的点为入口节点   </br>
#### [面试题24](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/24_ReverseList.py)：反转链表  </br>
三指针法    </br>
#### [面试题25](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/25_MergeSortedLists.py)：合并两个排序链表  </br>
注意边界条件    </br>
#### [面试题26](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/26_SubstructureInTree.py)：树的子结构  </br>
树的遍历，注意特殊情况   </br>
#### [面试题27](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/27_MirrorOfBinaryTree.py)：二叉树的镜像  </br>
递归修改左子树和右子树的位置，由于是镜像，因此需要修改每一个左右子树的位置就可以    </br>
#### [面试题28](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/28_SymmetricalBinaryTree.py)：对称的二叉树  </br>
递归进行比较，注意在递归比较时传入的参数，应该是左节点的左子树和右节点的右子树进行比较   </br>
#### [面试题29](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/29_PrintMatrix.py)：顺时针打印矩阵  </br>
递归法，注意当数组剩下一行或者一列时应该特殊计算   </br>
#### [面试题30](https://github.com/yjiao1213/python-leetcode-offer/blob/master/%E5%89%91%E6%8C%87offer66%E9%A2%98_pyhton%E5%AE%9E%E7%8E%B0/30_MinInStack.py)：包含min函数的栈  </br>
需要建立两个栈，一个用来存数据，一个用来存当前最小的数    </br>


Leetcode Top 100 Liked
------
#### [1.TwoSum](https://github.com/yjiao1213/python-leetcode-offer/blob/master/leetcode_top100_liked/Two_Sum.py)  </br>
暴力法时间复杂度较高，用字典法时间复杂度为O(n)
