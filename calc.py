import numpy as np


pxv_in = int(input("vertical hight in px:"))

pxH_in = int(input("horizontal length as px:"))

#####33

kmH_os = 5
pxHo = 294
dTowerO = 390                   #px


scale = pxHo /kmH_os            #px/km

print ("scale old= ",scale)
######
dTowerkm = dTowerO/scale        #km
print ("distance between towers=" ,dTowerkm)
###########

dTowerN_px = 298

h_scale = dTowerN_px/dTowerkm   #px/km
v_scale = 110/1.3               #px/km
print("vscale =", v_scale)

##########

scaled_V = pxv_in / v_scale
scaled_H = pxH_in / h_scale

#############
print ("vertical hight:", scaled_V, "km")
print ("horizontal length:",scaled_H, "km")


angle = np.rad2deg(np.arctan(scaled_V/scaled_H))

print(angle)