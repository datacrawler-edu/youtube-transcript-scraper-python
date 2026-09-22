# cURL request

Replace `YOUR_APIFY_TOKEN` with an Apify API token and edit `data/sample-input.json` when you want to send a different public video list. The API endpoint returns the default Dataset items after the run finishes.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~youtube-transcript-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

The endpoint waits for the run to finish and returns the default Dataset items. For long-running jobs or large batches, use the asynchronous run endpoint and read the Dataset after completion. Keep the token out of shell history and never commit it.
