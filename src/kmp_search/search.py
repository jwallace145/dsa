from dataclasses import dataclass
from typing import List


@dataclass
class KMPSearch:
    """
    Knuth-Morris-Pratt (KMP) Algorithm

    Wikipedia:
    https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

    Goal:
    Efficiently find all occurrences of a pattern P in a string S.

    Problem:
    Given a string S and a pattern P, how can we efficiently locate
    every occurrence of P within S?

    Naive Approach:
    The straightforward method scans S from left to right, checking
    character by character. When a character in S matches the first
    character of P, we attempt to match the entire pattern.

    If the full pattern P is matched, we record the occurrence.
    If not, we shift one character to the right in S and repeat
    the process from scratch.

    The issue with this approach is redundancy: whenever a mismatch
    occurs, we discard all progress and recheck characters we've
    already examined. This leads to unnecessary re-computation.

    Time Complexity: O(n * m), where n = len(S) and m = len(P)

    KMP Algorithm:
    The Knuth-Morris-Pratt algorithm avoids this redundant work
    by using information gathered during the matching process.

    Specifically, it constructs a longest prefix-suffix (LPS) table
    for the pattern P. This table tells us how far we can shift
    the pattern when a mismatch occurs, without rechecking already
    matched characters.

    This optimization allows the algorithm to process S in linear time.

    Time Complexity: O(n + m), where n = len(S) and m = len(P)

    Example of LPS Table Construction:
    Pattern: P = "ababaca"

    Index:     0  1  2  3  4  5  6
    Pattern:   a  b  a  b  a  c  a
    LPS:       0  0  1  2  3  0  1

    Explanation:
    - At index 2 ('a'): prefix 'a', suffix 'a' → length 1
    - At index 4 ('a'): prefix 'aba', suffix 'aba' → length 3
    - At index 5 ('c'): no match → 0
    - At index 6 ('a'): prefix 'a', suffix 'a' → length 1

    The LPS table tells us how much of the pattern we can reuse
    after a mismatch, enabling us to avoid unnecessary comparisons.
    """

    pattern: str

    lps_table: List[int] = None  # set during post init

    def __post_init__(self) -> None:
        self.lps_table = KMPSearch.create_lps_table(self.pattern)

    def search(self, text: str) -> List[int]:
        text_index = 0
        pattern_index = 0

        matches = []
        while text_index < len(text):
            if text[text_index] == self.pattern[pattern_index]:
                text_index += 1
                pattern_index += 1

            if pattern_index == len(self.pattern):
                matches.append(text_index - pattern_index)
                pattern_index = self.lps_table[pattern_index - 1]

            elif (
                text_index < len(text)
                and text[text_index] != self.pattern[pattern_index]
            ):
                # try a shorter prefix if prefix length is not zero
                if pattern_index != 0:
                    pattern_index = self.lps_table[pattern_index - 1]
                # if prefix length is zero and no match, continue iterating over text
                else:
                    text_index += 1

        return matches

    @staticmethod
    def create_lps_table(pattern: str) -> List[int]:
        lps_table = [0] * len(pattern)
        length = 0
        pattern_index = 1

        while pattern_index < len(pattern):
            if pattern[pattern_index] == pattern[length]:
                length += 1
                lps_table[pattern_index] = length
                pattern_index += 1

            else:
                # if prefix length is not zero, try a shorter prefix
                if length != 0:
                    length = lps_table[length - 1]
                # if prefix length is zero, update lps_table with prefix of length zero
                # at given pattern index and increment pattern_index
                else:
                    lps_table[pattern_index] = 0
                    pattern_index += 1

        return lps_table
