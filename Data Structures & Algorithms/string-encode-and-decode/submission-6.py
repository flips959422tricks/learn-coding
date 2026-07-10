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

        i = 0
        last_word_end_index = -1
        last_delimiter_index = -1
        cur_size = -1

        while i < len(s):
            c = s[i]

            # size determination
            if cur_size == -1 and c == "#":
                cur_size = int(s[last_word_end_index + 1:i])
                last_delimiter_index = i

            # word determination
            if cur_size != -1 and i == last_delimiter_index + cur_size:
                if cur_size == 0:
                    decoded.append("")
                else:
                    decoded.append(s[last_delimiter_index+1 : i+1])
                last_word_end_index = i
                cur_size = -1
            
            i += 1

        return decoded
