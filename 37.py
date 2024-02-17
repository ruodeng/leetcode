from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 找到最小的可填数组，填一个，然后递归，如果递归失败，就回溯
        # 如果递归成功，就返回
        # bs=List[List[List[int]]]
        # create a 9x9 list of list of list
        # bs[i][j] is a list of int, which is the possible number for board[i][j]
        # if board[i][j] is filled, then bs[i][j] is an empty list
        bs=[[] for  _ in range(9)]

        minCount=9

        for i in range(9):
            bs[i] = [[] for _ in range(9)]
            for j in range(9):
                temp=[i for i in range(1,10)]
                if board[i][j] == '.':
                    for k in range(9):
                        if board[i][k] != '.' and int(board[i][k]) in temp:
                            temp.remove(int(board[i][k]))
                        if board[k][j] != '.' and int(board[k][j]) in temp:
                            temp.remove(int(board[k][j]))
                    for k in range(3):
                        for l in range(3):
                            if board[i//3*3+k][j//3*3+l] != '.':
                                if int(board[i//3*3+k][j//3*3+l]) in temp:
                                    temp.remove(int(board[i//3*3+k][j//3*3+l]))
                    bs[i][j]=temp
                    if len(temp) < minCount:
                        minCount=len(temp)

        def dfs():
            for i in range(9):
                for j in range(9):
                    if len(bs[i][j]) == minCount:
                        # if minCount == 1:
                        for k in range(minCount):
                            num = bs[i][j][k]
                            board[i][j]=str(num)
                            # bs[i][j].remove(bs[i][j][k])
                            for l in range(9):
                                if board[i][l] == '.' and   num in bs[i][l]:
                                    bs[i][l].remove(num)
                                if board[l][j] == '.' and   num in bs[l][j]:
                                    bs[l][j].remove(num)

                                for l in range(3):
                                    if num in bs[i//3*3+k][j//3*3+l]:
                                        # print(i//3*3+k,j//3*3+l, num, bs[i//3*3+k][j//3*3+l])
                                        bs[i//3*3+k][j//3*3+l].remove(num)

                            # if check(i,j) and dfs():
                            #     return True
                            # board[i][j]='.'
                        return False






        dfs()
        print(board)



s=Solution()
ss=s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])