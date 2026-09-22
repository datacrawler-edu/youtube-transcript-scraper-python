# Run YouTube Transcript Extractor without code

You can use the hosted Actor from the Apify web interface without installing a package or writing a script.

## Step-by-step

1. Open [YouTube Transcript Extractor - Timestamps on Apify](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata).
2. Select the **Input** tab.
3. Enter one or more public YouTube watch, `youtu.be`, Shorts, live or embed URLs in **YouTube video URLs**.
4. Select a supported language from the **Transcript language** dropdown. English (`en`) is preselected.
5. Review the input and click **Start**.
6. When the run finishes, open the **Dataset** tab.
7. Review the `status`, `segmentCount`, `segments` and error fields, then export as JSON, CSV or Excel.

## First test

Start with the example in [`data/sample-input.json`](../data/sample-input.json). It uses a small, sanitized input so you can verify the output before sending a larger batch.

## Use the monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors, and no credit card is required to start. Use a small input first so you can test the Actor while credit is available. The credit is not unlimited, and unused credit expires at the end of the billing cycle.

See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for the current terms.

## What to check in the output

For a complete transcript, look for `status: "success"`, a positive `segmentCount`, a non-empty `segments` array and `errorCode: null`. Each segment contains its start time, duration and text. A failed video is still represented by one Dataset item with `status: "error"`, an empty `segments` array and a stable `errorCode`, so no input silently disappears.

## Larger runs

The run accepts 1–5,000 URL values and processes unique video IDs sequentially. It charges only for a complete successful transcript delivered to the Dataset. Videos without a transcript, without the selected language, unavailable videos and other error rows are not charged. See the [hosted Actor page](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata) for the current tier price.

You can save a tested input in Apify for repeated runs; scheduling and task features are optional Apify platform features rather than required for a first test.
