class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_cities = set()
        all_cities = set()

        # Iterate through paths to identify outgoing cities
        for path in paths:
            outgoing_cities.add(path[0])
            all_cities.add(path[0])
            all_cities.add(path[1])

        # Find the destination city by subtracting outgoing cities from all cities
        destination_city = (all_cities - outgoing_cities).pop()

        return destination_city
        