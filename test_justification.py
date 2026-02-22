from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(word) for word in line_words)
            
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - total_chars
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                line = ""
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += " " * (space_between + (1 if k < extra_spaces else 0))
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res
