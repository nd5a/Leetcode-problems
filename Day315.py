# Fraction to Recurring Decimal

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        negative = False
        if numerator < 0:
            negative = not negative
        if denominator < 0:
            negative = not negative
            
        N, D = abs(numerator), abs(denominator)

        whole, remainder = divmod(N, D)

        def neg(s):
            return f"-{s}" if negative and s != "0" else s

        if remainder == 0:
            return neg(str(whole))   # apply sign here
        
        seen = {}
        ans = []

        while remainder > 0:
            remainder *= 10
            digit, remainder = divmod(remainder, D)

            if (digit, remainder) in seen:
                return neg(f"{whole}." + "".join(ans[:seen[(digit, remainder)]]) + "(" + "".join(ans[seen[(digit, remainder)]:]) + ")")
            
            seen[(digit, remainder)] = len(ans)
            ans.append(str(digit))

        return neg(f"{whole}." + "".join(ans))
