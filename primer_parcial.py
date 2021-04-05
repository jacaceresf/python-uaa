import numpy as np

anho = np.array([2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011,
        2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2000, 1999, 1997])

urbana_lpe = np.array([272067, 266754, 262768, 256881, 235088, 219632, 216077, 212676, 194438, 201084,
              187637, 170327, 164144, 160418, 137765, 110665, 97599, 94146, 81825, 69698, 59946, 54283])

urbana_lpt = np.array([712618, 699634, 686075, 664297, 630525, 606429, 588552, 569073, 540917, 523735,
              493061, 463965, 453610, 430835, 397342, 361707, 328550, 317340, 299981, 251299, 216024, 188578])

rural_lpe = np.array([248461, 243608, 239969, 234592, 214690, 200575, 197328, 194223, 177567, 183637,
             171357, 155548, 149902, 146499, 125812, 101063, 89130, 85977, 74725, 63650, 54745, 49573])

rural_lpt = np.array([506201, 497049, 488172, 473601, 446798, 427893, 416310, 403759, 381742, 374096,
             352073, 329460, 321358, 306770, 279728, 250008, 225239, 217526, 203235, 170609, 146324, 127812])

print(type(anho))
print(urbana_lpe)
print(urbana_lpt)
print(rural_lpe)
print(rural_lpt)

total_array = []
for an, u_lpe, u_lpt, r_lpe, r_lpt in zip(anho, urbana_lpe, urbana_lpt, rural_lpe, rural_lpt):
    arr = [an, u_lpe, u_lpt, r_lpe, r_lpt]
    total_array.append(arr)


total_array_np = np.array([total_array])
total_array_np