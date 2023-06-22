

class Solution_binSearch:
  def guessNumber(self, n) :
    lo, hi = 1, n
    while lo <= hi :
      half = (lo + hi) // 2
      res = guess(half)
      if res == 0: return half
      if res < 0 : hi = half - 1
      if res > 0 : lo = half + 1
