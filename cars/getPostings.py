import random


def fetch_postings(year: int, make: str, model: str):
    """Return a list of fake postings for the given car."""
    # Placeholder implementation; in the future this would query APIs or scrape data
    postings = []
    for i in range(1, 4):
        postings.append({
            "title": f"{year} {make} {model} - Listing {i}",
            "price": random.randint(15000, 30000),
            "location": "Local Dealer",
        })
    return postings
