class Solution:
    delimiter = chr(300) # outside the 256 ascii chars

    def encode(self, strs: List[str]) -> str:
        list_size = len(strs)
        list_contents = self.delimiter.join(s for s in strs)
        encoded = str(list_size) + self.delimiter + list_contents
        return encoded

    def decode(self, s: str) -> List[str]:
        segments = s.split(self.delimiter)
        list_size = int(segments[0])
        if list_size == 0:
            return []
        decoded_list = [s for s in segments[1:]]
        return decoded_list
