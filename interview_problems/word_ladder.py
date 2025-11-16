"""
Word Ladder Problem Implementation in Python

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord.

Time Complexity: O(M * N) where M is word length, N is number of words
"""

from collections import deque

def ladder_length(begin_word, end_word, word_list):
    """
    Find the shortest transformation sequence length.
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = set([begin_word])

    while queue:
        current_word, level = queue.popleft()

        # Generate all possible words by changing one letter
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]

                if next_word == end_word:
                    return level + 1

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))

    return 0

# Example usage and test cases
if __name__ == "__main__":
    # Test case 1
    begin_word1 = "hit"
    end_word1 = "cog"
    word_list1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("Word ladder length:", ladder_length(begin_word1, end_word1, word_list1))  # 5

    # Test case 2
    begin_word2 = "hit"
    end_word2 = "cog"
    word_list2 = ["hot", "dot", "dog", "lot", "log"]
    print("Word ladder length (no path):", ladder_length(begin_word2, end_word2, word_list2))  # 0

    # Test case 3
    begin_word3 = "a"
    end_word3 = "c"
    word_list3 = ["a", "b", "c"]
    print("Word ladder length:", ladder_length(begin_word3, end_word3, word_list3))  # 2
