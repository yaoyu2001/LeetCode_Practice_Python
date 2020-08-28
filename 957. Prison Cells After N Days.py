class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        # A dict to save state in every step
        seen = dict()
        # If find a cycle, let it equal to True
        is_cycle = False

        while N > 0:
            # we only need to run the fast-forward once at most
            if not is_cycle:
                cur_state = tuple(cells)
                if cur_state in seen:  # Find cycle !
                    N = N % (seen[cur_state] - N)
                    # The length of cycle is seen[cur_state] - N, so we let N = N mod length of cycle
                    is_cycle = True
                else:
                    seen[cur_state] = N

            # If there is still some steps remained
            # No matter it has the fast-forwarding.
            if N > 0:
                N -= 1
                next_cells = self.get_next(cells)
                cells = next_cells

        return cells

    def get_next(self, cells):
        res = [0]  # Head
        # Get every cells
        for i in range(1, len(cells) - 1):
            res.append(int(cells[i - 1] == cells[i + 1]))
        # Add tail
        res.append(0)
        return res
