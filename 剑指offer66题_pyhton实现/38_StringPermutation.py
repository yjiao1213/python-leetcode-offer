# -*- coding:utf-8 -*-
'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''
class Solution:
    def Permutation(self, ss):
        # write code here
        list = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):
                if j not in list:
                    list.append(j)
        return list