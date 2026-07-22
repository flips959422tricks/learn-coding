class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sequences = list (start, end, size)
        seqs = []

        # first pass = seq formation
        for i, n in enumerate(nums):

            # vars
            inserted = False
            j = 0

            while not inserted and j < len(seqs) - 1:
                seq = seqs[j]
            
                # insert
                if i == 0 or n < seq[0] - 1:
                    seqs.insert(j,(n,n,1))
                    inserted = True
                elif n == seq[0] - 1:
                    seq[0] = n
                    seq[2] = seq[2] + 1
                    inserted = True
                elif seq[0] <= n and n <= seq[1]:
                    inserted = True
                elif n == seq[1] + 1:
                    seq[1] = n
                    seq[2] = seq[2] + 1
                    inserted = True
                elif n > seq[2] + 1 and j == len(seqs) -1:
                    seqs.append((n,n,1))
                    inserted = True

                # inc
                j = j + 1

        # second pass = merge sequences
        largest_seq_size = 0

        for j in range(len(seqs)):
            if j > 0 and seqs[j-1][1] == seqs[j][0] - 1:
                seqs[j][0] = seqs[j-1][0]
                seqs[j][2] = seqs[j][2] + seqs[j-1][2]
            
            if seqs[j][2] > largest_seq_size:
                largest_seq_size = seqs[j][2]

        return largest_seq_size
