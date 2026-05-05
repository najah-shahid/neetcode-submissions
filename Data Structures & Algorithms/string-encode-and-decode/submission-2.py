class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_word = f'{len(word)}#{word}'
            encoded_string += encoded_word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            word_len = ''
            while s[i] != '#':
                word_len += s[i]
                i+=1
            i+=1
            word_len = int(word_len)
            word = s[i:i+word_len]
            result.append(word)
            i += word_len
        return result

