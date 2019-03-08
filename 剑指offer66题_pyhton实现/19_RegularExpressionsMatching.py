# -*- coding:utf-8 -*-
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的
字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


class Solution(object):
    def Match(self, s, pattern):
        if len(s) == 0 or len(pattern) == 0:
            return False
        else:
            return self.matchCore(s, pattern)

    def matchCore(self, s, p):
        if len(p) == 0 and s:
            return False
        if not s and not p:
            return True
        if len(p) >= 2 and p[1] == '*':
            if len(s)>=1 and (p[0] == s[0] or p[0] == '.'):
                return self.matchCore(s[1:], p[2:]) or self.matchCore(s, p[2:]) or self.matchCore(s[1:], p)
            else:
                return self.matchCore(s, p[2:])

        if len(s)>=1 and (p[0] == s[0] or p[0] == '.'):
            return self.matchCore(s[1:], p[1:])
        return False


if __name__ == '__main__':
    a = 'aaa'
    p = 'aaaa*'
    sol = Solution()
    print(sol.Match(a,p))