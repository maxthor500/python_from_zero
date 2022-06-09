# Questo programma calcola il volume (in litri) di una confezione
# di bibite con sei lattine, seguito dal volume di una tale confenzione
# insieme ad una bottiglia da due litri

CAN_VOLUME = 0.355  # liters in an 12 ounce's can 
BOTTLE_VOLUME = 2   # 2 liters bottle

cansPerPack = 6     # how many cans in a pack

# Total volume in a pack
totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "liters")#

# Total volume in a pack plus volume in a bottle
totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and two-liters bottle contain", totalVolume, "liters")