

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        w = word
        result = 0
        while len(w) > 0:
            w[0] = character
            if character.upper() in w and character.lower() in w:
                result += 1
                w.replace(character.upper(), '')
                w.replace(character.lower(), '')
            else:
                w.replace(character, '')
        return result