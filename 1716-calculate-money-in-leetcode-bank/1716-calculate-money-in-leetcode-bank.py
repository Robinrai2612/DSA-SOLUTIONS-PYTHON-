class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        current_day = 1
        current_amount = 1

        while current_day <= n:
            total += current_amount
            current_day += 1
            current_amount += 1

            if current_day % 7 == 1:
                current_amount = (current_day // 7) + 1

        return total
