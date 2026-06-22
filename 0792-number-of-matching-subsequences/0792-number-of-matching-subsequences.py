from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Store positions of each character in s
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        count = 0

        for word in words:
            prev = -1
            is_subseq = True

            for ch in word:
                # Find the first occurrence of ch after prev
                idx = bisect_right(pos[ch], prev)

                if idx == len(pos[ch]):
                    is_subseq = False
                    break

                prev = pos[ch][idx]

            if is_subseq:
                count += 1

        return count