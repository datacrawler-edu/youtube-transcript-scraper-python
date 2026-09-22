"""Run the Actor and export its Dataset items to JSON and CSV."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path

from apify_client import ApifyClient


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
ACTOR_ID = "datascraperes/youtube-transcript-scraper"
OUTPUT_JSON = Path("youtube-transcripts.json")
OUTPUT_CSV = Path("youtube-transcripts.csv")
CSV_FIELDS = ["videoId", "videoUrl", "status", "title", "languageRequested", "segmentCount", "errorCode", "errorMessage"]


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    OUTPUT_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for item in items:
            writer.writerow({field: item.get(field) for field in CSV_FIELDS})

    print(f"Wrote {len(items)} item(s) to {OUTPUT_JSON} and {OUTPUT_CSV}.")


if __name__ == "__main__":
    main()
