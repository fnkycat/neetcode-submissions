class Solution:
    def countBits(self, n: int) -> List[int]:
        s = []
        for i in range(n+1):
            num = list(map(int, str(bin(i)[2:])))
            s.append(num.count(1))

        return s