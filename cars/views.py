from django.shortcuts import render
from .getPostings import fetch_postings


def car_info(request, year: int, make: str, model: str):
    postings = fetch_postings(year, make, model)
    context = {
        "year": year,
        "make": make,
        "model": model,
        "postings": postings,
    }
    return render(request, "cars/car_info.html", context)
