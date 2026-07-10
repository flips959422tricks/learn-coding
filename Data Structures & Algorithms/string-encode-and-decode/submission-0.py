class Solution:
    empty_string_encode_value = "1000"

    def encode(self, strs: List[str]) -> str:
        return "-".join(Solution.encode_string(self, s) for s in strs)

    def decode(self, s: str) -> List[str]:
        return list(map(lambda word: Solution.decode_string(self, word), s.split("-")))

    def encode_string(self, s: str) -> str:
        if s == "":
            return self.empty_string_encode_value
        else:
            return ".".join(map(lambda c: str(ord(c)), s))
    
    def decode_string(self, encoded_str: str) -> str:
        if encoded_str == self.empty_string_encode_value:
            return ""
        else:
            return "".join(map(lambda c: chr(int(c)), encoded_str.split(".")))
