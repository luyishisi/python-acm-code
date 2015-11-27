'''
描述:
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。
'''
print('UP' if L == sorted(L) else 'DOWN' if L == sorted(L, reverse = True) else "WRONG")

