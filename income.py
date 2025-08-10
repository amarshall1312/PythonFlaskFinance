# file for handling income data and returning required objects

## thinking about having the values of "minimum expected income" which may be ~1800/2000 and then user adds actual income (e.g 2300) which leaves bonus income = 500
# this can then be divvied up across savings pots and reserve for variable bill fluctuation
# maybe minimum base income should cover all expected bills + ~10% 

def calculate_total_income(incomes):
    return sum(incomes)

