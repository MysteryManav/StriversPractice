# Minimize Maximum distance between gas stations
def number_of_gas_station(distances, max_distance):
    n = len(distances)
    count = 0
    for i in range(1, n):
        gas_stations = (distances[i] - distances[i - 1])/max_distance
        if (distances[i] - distances[i - 1]) == max_distance * gas_stations:
            gas_stations -= 1
        count += gas_stations
    return count

def minimise_max_distance_gas_stations(distances, stations):
    n = len(distances)
    lo = 0
    hi = 0
    for i in range(n-1):
        hi = max(hi, distances[i+1] - distances[i])
    
    diff = 1e-6
    while hi - lo > diff:
        mid = (lo + hi)/2.0
        gas_stations = number_of_gas_station(distances, mid)
        if gas_stations > stations:
            lo = mid
        else:
            hi = mid
    return hi

stations = 4
distances = [1, 2, 3, 4, 5]
print(minimise_max_distance_gas_stations(distances, stations))
