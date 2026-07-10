class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        decoded = []

        last_delimiter_index = -1
        cur_size = -1
        cur_size_str = ""
        cur_word_str = ""
        for i in range(len(s)):
            c = s[i]

            if cur_size == -1 and c == "#":
                # determine size
                last_delimiter_index = i
                cur_size = int(cur_size_str)
                cur_word_str = ""
            elif cur_size == -1: 
                # build size str
                cur_size_str += c
            else: 
                # build word str
                cur_word_str += c

            # check word termination
            if cur_size != -1 and i == last_delimiter_index + cur_size:
                decoded.append(cur_word_str)
                cur_size = -1
                cur_size_str = ""

        return decoded
