from math import sin, cos, sqrt, atan2, radians

print('Input coordinates cities A: ')
latitudeA = radians(float(input('Latitude cities A: ')))
longitudeA = radians(float(input('Longitude cities A: ')))
print('Input coordinates cities B: ')
latitudeB = radians(float(input('Latitude cities B: ')))
longitudeB = radians(float(input('Longitude cities B: ')))

distance_longitude = longitudeB - longitudeA
distance_latitude = latitudeB - latitudeA

a = sin(distance_latitude / 2) ** 2 + cos(latitudeA) * cos(latitudeB) * sin(distance_longitude / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 -a))

# Approximate radius of earch in km
R = 6373.0
distance = R * c

print('distance between A and B: ', round(distance, 2), 'km')
print('distance between A and B: ', round(distance * 0.62137119223733, 2), 'mile')

