# Write a function to calculate electricity bill.

"""
    first 100 units - 10rs/unit
    100 to 200 units - 15rs/unit
    200 to 300 units - 20rs/unit
    above 300 units - 25rs/unit
"""
COST_ABOVE_300 = 25
COST_BETWEEN_200_300 = 20
COST_BETWEEN_100_200 = 15
COST_BELOW_100 = 10


def cost_for_units_upto_300(units):
    return (units - 200) * COST_BETWEEN_200_300 + cost_for_units_upto_200(200)

def cost_for_units_upto_200(units):
    return (units - 100) * COST_BETWEEN_100_200 + cost_for_units_upto_100(100)    

def cost_for_units_upto_100(units):
    return units * COST_BELOW_100

def calculate_electricity_bill(units: int) -> int:
    
    if units <= 100:
        return cost_for_units_upto_100(units)
    
    if units <= 200:
        return cost_for_units_upto_200(units)
    
    if units <= 300:
        return cost_for_units_upto_300(units)
    
    if units > 300:
        return (units - 300)*COST_ABOVE_300 + cost_for_units_upto_300(300)
        

if __name__ == "__main__":
    print(calculate_electricity_bill(300))
    print(calculate_electricity_bill(150))
    print(calculate_electricity_bill(70))
    print(calculate_electricity_bill(277))
    print(calculate_electricity_bill(0))
    print(calculate_electricity_bill(1000))
    print(calculate_electricity_bill(750))

