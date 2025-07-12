import json
import os
from datetime import timedelta

from django.utils import timezone
import openai

from .models import CarInsightCache


def fetch_insights(year: int, make: str, model: str):
    """Return pros and cons for a car, cached for one week."""
    make = make.lower()
    model = model.lower()
    one_week_ago = timezone.now() - timedelta(weeks=1)
    try:
        entry = CarInsightCache.objects.get(year=year, make=make, model=model)
        if entry.updated_at >= one_week_ago:
            return json.loads(entry.data)
    except CarInsightCache.DoesNotExist:
        entry = None

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        openai.api_key = api_key
        prompt = (
            f"Give 5 bullet points each for the pros and cons of {year} {make} {model}."
        )
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            content = resp["choices"][0]["message"]["content"].strip()
        except Exception:
            content = "Could not fetch data from ChatGPT"
    else:
        content = "OPENAI_API_KEY not configured"

    data = {"analysis": content}

    if entry is None:
        entry = CarInsightCache(year=year, make=make, model=model)
    entry.data = json.dumps(data)
    entry.save()
    return data

