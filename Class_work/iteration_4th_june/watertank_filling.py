#program of water tank filling
#litter per minute
rate = 10          
water = 0
capacity = 100

while water < capacity:
    water += rate
#-------------------------------------
#validation
    if water > capacity:      
        water = capacity

    print("Water in tank:", water, "liters")
#-------------------------------------------    

print("Tank is full.")