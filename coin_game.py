class Game:
    def __init__(self, coins):
        self.coins = coins
    
    def run(self, start, end):
        max_win = 0
        margin = 0
        takeRight = True
        # Do the calculation

        # Base case = 0 coin
        if end < start == 0:
            return (0, 0, True)
        
        # Cache in a 2D array 
        n = end - start + 1
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if i == j:  # Base case: one coin
                    dp[i][j] = self.coins[start + i]
                else:
                    # Calculate left and right choices based on the recursive formula
                    # left = min{CG[1,..n-2], CG[2,...n-1]}+c0
                    left = min(
                        dp[i + 2][j] if i + 2 <= j else 0, 
                        dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                    ) + self.coins[start + i]
                    # right = min{CG[0,..n-3], CG[1,...n-2]}+cn-1
                    right = min(
                        dp[i][j - 2] if j - 2 >= i else 0, 
                        dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                    ) + self.coins[start + j]
                    dp[i][j] = max(left, right)
        
        max_win = dp[0][n - 1]

        total_coins = sum(self.coins[start:end + 1])
        margin = max_win - (total_coins - max_win)

        if n > 1:
            takeLeftFirst = self.coins[start] + min(dp[2][n-1], dp[1][n-2])
            takeRightFirst = self.coins[end] + min(dp[0][n-3], dp[1][n-2])
            takeRight = max_win == takeRightFirst and takeRightFirst >= takeLeftFirst
        else:
            takeRight = True
        
        return (max_win, margin, takeRight)

