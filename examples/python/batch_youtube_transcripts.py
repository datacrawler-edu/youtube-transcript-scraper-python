"""Run a bounded batch of public YouTube URLs through the hosted Actor."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
ACTOR_ID = "datascraperes/youtube-transcript-scraper"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    run_input["videoUrls"] = list(dict.fromkeys(run_input["videoUrls"]))
    print(f"Submitting {len(run_input['videoUrls'])} unique video URL(s).")

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    successes = sum(item.get("status") == "success" for item in items)
    print(f"Received {len(items)} Dataset item(s): {successes} successful transcript(s).")

    for item in items:
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
