"""
Calculate distances

Example from Vancouver to Curitiba

Vancouver
49.3°N 123.1°W
49.260833, -123.113889
49°15'39"N  123°06'50"W

Curitiba
25.42°S 49.27°W
-25.429722, -49.271111
25°25'47"S  49°16'16"W
"""

from math import asin, cos, radians, sin, sqrt

# Approximate radius of Earth in kilometers
rad = 6371

# Locations of Vancouver and Curitiba
phi1, λ1 = radians(49.260833), radians(-123.113889)
phi2, λ2 = radians(-25.429722), radians(-49.271111)

print(phi1, λ1)
# 0.8597637281250758 -2.1487427179848293

print(phi2, λ2)
# -0.4438323767668375 -0.8599431130655958

# Distance between Vancouver and Curitiba
dist = 2 * rad * asin(
  sqrt(
    sin((phi2 - phi1) / 2) ** 2
    + cos(phi1) * cos(phi2) * sin((λ2 - λ1) / 2) ** 2
  )
)

print(f"{dist:.2f} Km")
# 11039.97 Km
