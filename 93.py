class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(path, s, res):
            []
            if len(path) == 4:
                if not s:
                    res.append('.'.join(path))
                return
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        dfs(path+[s[:i]], s[i:], res)
                    elif i == 2 and s[0] != '0':
                        dfs(path+[s[:i]], s[i:], res)
                    elif i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                        dfs(path+[s[:i]], s[i:], res)
        dfs([], s, res)
        return res