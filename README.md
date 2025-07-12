# CarDive
Get all the info you want for a particular vehicle

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Set your `OPENAI_API_KEY` environment variable before running the server to
enable fetching pros/cons from ChatGPT. Results are cached for a week in the
SQLite database so repeated searches don't hit the API again.

Visit `http://localhost:8000/car/<year>/<make>/<model>/` to see the vehicle info page.
