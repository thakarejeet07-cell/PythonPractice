from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float

    def distance_km(self, other):
        return ((self.latitude - other.latitude)**2 + 
                (self.longitude - other.longitude)**2) ** 0.5


visited_places = {
    Location(40.7128, -74.0060): "New York",
    Location(51.5074, -0.1278): "London",
    Location(35.6762, 139.6503): "Tokyo",
}


nyc = Location(40.7128, -74.0060)
print(visited_places[nyc])

favorite_places = {Location(51.5074, -0.1278),Location(40.7128, -74.0060), }
print(len(favorite_places))

places = sorted(favorite_places, key=lambda x: x.latitude)
print(places[0])