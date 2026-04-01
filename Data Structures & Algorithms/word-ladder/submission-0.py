class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([beginWord])

        res = 1
        while q:
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return res
                for i in range(len(curr_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr_word[i]:
                            continue
                        new_wrd = curr_word[:i] + c + curr_word[i+1:]
                        if new_wrd in wordSet:
                            q.append(new_wrd)
                            wordSet.remove(new_wrd)
            res += 1
        return 0




        
        