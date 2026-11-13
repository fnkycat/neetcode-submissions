class Solution:
    def hammingWeight(self, n: int) -> int:
        num = list(map(int, str(bin(n)[2:])))
        count = 0

        for i in range(len(num)):
            if num[i] == 1:
                count += 1

        return count
        