import json
import os
import requests


def fetch_serpapi(query, location="United States"):
    """
    Call SerpApi's Google-Jobs engine with `query`
    and optionally insert each result into jobs_raw.
    """
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise ValueError("Set SERPAPI_KEY in your .env file first!")

    params = {
        "engine":   "google_jobs",
        "q":        query,
        "location": location,
        "api_key":  api_key,
    }
    url = "https://serpapi.com/search.json"
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()                              # 4xx/5xx → exception
    results = resp.json().get("jobs_results", [])
    print(f"SerpApi returned {len(results)} jobs for '{query}'")


    return results

json_res = fetch_serpapi("sofware engineer", "United States")  # Example usage
with open("jobs_fetched.json", "w", encoding="utf-8") as f:
    json.dump(json_res, f, indent=2)