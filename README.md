# YouTube transcript scraper with timestamps and JSON output

Run **YouTube Transcript Extractor - Timestamps** from Apify's web interface without writing code, or integrate it with Python, JavaScript or cURL to get complete timestamped **YouTube transcript segments**.

This repository contains working request examples, sanitized sample input, a complete sample Dataset item and CSV data so you can understand the result format before running a live request.

[Open YouTube Transcript Extractor - Timestamps on Apify](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata)

## What this repository helps you do

- Extract complete, timestamped captions from public YouTube videos for search, RAG and research workflows.
- Process up to 5,000 unique video URLs in one sequential run with a validated language selector.
- Receive one structured Dataset item per video, including title, requested language, segment timings and an explicit result status.
- Export transcript records as JSON, CSV or Excel for downstream analysis.

## Example result

The repository includes a sanitized example in [`data/sample-output.json`](data/sample-output.json) and a tabular version in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "videoId": "jNQXAC9IVRw",
  "videoUrl": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
  "status": "success",
  "title": "Me at the zoo",
  "languageRequested": "en",
  "segmentCount": 3,
  "segments": [
    {
      "start": 1.0,
      "duration": 6.0,
      "text": "All right, so here we are, in front of the elephants the cool thing about these guys is that they have really..."
    },
    {
      "start": 7.0,
      "duration": 9.0,
      "text": "really really long trunks and that's cool (baaaaaaaaaaahhh!!)"
    },
    {
      "start": 16.0,
      "duration": 0.0,
      "text": "and that's pretty much all there is to say"
    }
  ],
  "errorCode": null,
  "errorMessage": null
}
```

## Run without code

You can run the hosted Actor directly from the Apify web interface. This is the simplest option if you do not need to write a program.

1. Open [YouTube Transcript Extractor - Timestamps on Apify](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata).
2. In the **Input** tab, enter one or more public YouTube URLs in **YouTube video URLs**.
3. Select the requested transcript language from the dropdown. English (`en`) is the default.
4. Review the input and click **Start**.
5. Open the **Dataset** tab to inspect the per-video results and export them as JSON, CSV or Excel.

Use [`docs/no-code-guide.md`](docs/no-code-guide.md) for the field-by-field walkthrough and [`data/sample-input.json`](data/sample-input.json) for a first test input.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage** that can be spent in the Apify Store or on your own Actors. No credit card is required to start. This can cover a small first test of **YouTube Transcript Extractor - Timestamps** while you have credit available; it is not unlimited free usage.

Unused credits expire at the end of the billing cycle and do not roll over. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) before running a larger batch.

## Quick start for developers

### Python

#### 1. Install the client

```bash
pip install apify-client
```

#### 2. Set your Apify token

```bash
export APIFY_API_TOKEN="your-token"
```

On Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

#### 3. Run the example

```bash
python examples/python/youtube_transcript.py
```

The example reads [`data/sample-input.json`](data/sample-input.json), starts the hosted Actor and prints the returned dataset items.

## Input example

```json
{
  "videoUrls": [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
  ],
  "language": "en"
}
```

See the complete field guide in [`docs/input-reference.md`](docs/input-reference.md).

## Request examples

### cURL

See [`examples/curl-request.md`](examples/curl-request.md) for the synchronous API request.

### Python

See [`examples/python/youtube_transcript.py`](examples/python/youtube_transcript.py), [`examples/python/batch_youtube_transcripts.py`](examples/python/batch_youtube_transcripts.py) and [`examples/python/export_youtube_transcripts.py`](examples/python/export_youtube_transcripts.py).

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

All examples use the hosted Apify Actor. They do not expose a proxy, bypass access controls or require the Actor source code locally.

## Output fields

The most useful fields are:

| Field | Meaning |
| --- | --- |
| `videoId` | The normalized 11-character YouTube video ID. |
| `videoUrl` | The canonical public watch URL for the video. |
| `status` | `success` when a complete non-empty transcript was delivered; otherwise `error`. |
| `title` | The public video title when available, otherwise `null`. |
| `languageRequested` | The validated language code requested for the video. |
| `segmentCount` | Number of transcript segments in `segments`. |
| `segments` | Timestamped objects with `start`, `duration` and `text`; empty for error rows. |
| `errorCode` | Stable error classification, or `null` for a successful transcript. |
| `errorMessage` | User-facing explanation for an error, or `null` on success. |

See [`docs/output-reference.md`](docs/output-reference.md) for the complete output contract.

## Common use cases

Read [`docs/use-cases.md`](docs/use-cases.md) for complete examples covering:

- Build searchable timestamp indexes for public video libraries.
- Create JSON caption corpora for RAG, summarization or classification.
- Audit transcript availability by video and requested language.

## How to extract complete timestamped transcripts from YouTube

Use [`data/sample-input.json`](data/sample-input.json) with the hosted Actor for a one-video test, or pass up to 5,000 public URLs in `videoUrls`. The Actor processes unique video IDs sequentially and writes each completed result to the Dataset.

## How to export YouTube captions as JSON with Python

Run [`examples/python/export_youtube_transcripts.py`](examples/python/export_youtube_transcripts.py) with `APIFY_API_TOKEN` set. It calls the hosted Actor and writes the returned Dataset items to JSON and CSV files without requiring the Actor source code locally.

## FAQ

See [`docs/faq.md`](docs/faq.md) for questions derived from the actual Actor behavior.

## Limits and pricing

The Actor accepts 1–5,000 URL values per run and removes duplicate video IDs while preserving first-seen order. It charges one `transcript-delivered` event only for a complete successful transcript with non-empty segments. Error rows, unavailable videos, missing-language results, empty transcripts and results blocked by the run charge limit are not charged.

The active tiered prices are:

| Apify tier | Price per complete transcript | Equivalent per 1,000 transcripts |
| --- | ---: | ---: |
| Free | $0.003000 | $3.00 |
| Bronze | $0.002700 | $2.70 |
| Silver | $0.002400 | $2.40 |
| Gold | $0.002250 | $2.25 |
| Platinum | $0.002250 | $2.25 |
| Diamond | $0.002250 | $2.25 |

Apify resolves the applicable account tier. Compute, storage and proxy costs are separate platform costs. Verify the current pricing on [Apify](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata) before sending a large batch.

## Hosted version

Use the hosted version when you need repeatable execution, batching, scheduling, API access or output storage without managing the scraping infrastructure yourself. It can be run from the web interface or called programmatically:

[Open YouTube Transcript Extractor - Timestamps on Apify](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata)

## Responsible use

Use the returned data lawfully and respect the terms, access rules and privacy obligations that apply to your use case. Never commit API tokens or other credentials to this repository.

## Support

For a problem with the examples, [open a GitHub issue](https://github.com/datacrawler-edu/youtube-transcript-scraper-python/issues) with the command, sanitized input and error message. For an execution problem, include the Apify run ID but never include your token.

## License

This repository is released under the MIT License.
