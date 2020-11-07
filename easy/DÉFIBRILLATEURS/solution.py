import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
list_dist = []
for i in range(n):
    defib = input().split(';')
    name = defib[1]
    lon_defib = float(defib[-2].replace(',', '.'))
    lat_defib = float(defib[-1].replace(',', '.'))

    x = (lon - lon_defib) * math.cos(0.5 * lat * lat_defib)
    y = lat - lat_defib

    dist = math.sqrt(x**2 + y**2) * 6371

    list_dist.append((name, dist))

result = min(list_dist, key=lambda x: x[1])[0]

print(result)
