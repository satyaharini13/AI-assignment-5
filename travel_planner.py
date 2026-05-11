places = {
    "beach": ["Goa", "Vizag"],
    "hill": ["Manali", "Ooty"],
    "city": ["Delhi", "Mumbai"]
}

budget_map = {
    "low": 1000,
    "medium": 5000,
    "high": 10000
}

def recommend(place_type, budget):
    options = places.get(place_type, [])
    return {
        "places": options,
        "estimated_budget": budget_map.get(budget, 0)
    }

if __name__ == "__main__":
    print(recommend("beach", "low"))
