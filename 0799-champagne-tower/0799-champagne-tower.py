class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * 101 for _ in range(101)]
    
        # Pour the initial amount of champagne into the top glass
        glasses[0][0] = poured

        # Iterate through the rows
        for row in range(query_row + 1):
            for glass in range(row + 1):
                # Calculate the excess champagne that flows to the left and right glasses
                excess = max(0, glasses[row][glass] - 1) / 2.0
                # Update the left and right glasses
                glasses[row + 1][glass] += excess
                glasses[row + 1][glass + 1] += excess

        # Return the amount of champagne in the specified glass
        return min(1, glasses[query_row][query_glass])