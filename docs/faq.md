# FAQ

These answers describe the current public Actor contract.

## Can I run this Actor without Python or code?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/youtube-transcript-scraper?fpr=edudata), enter the URLs in the **Input** tab, choose a language and click **Start**. Inspect or export the results from the **Dataset** tab. See [`docs/no-code-guide.md`](no-code-guide.md).

## Can I test this Actor with Apify's free plan?

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors. It can cover a small test while credit is available, but it is not unlimited free usage. Unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for the current terms.

## How do I request a complete YouTube transcript with timestamps?

Pass one or more public URLs in `videoUrls` and a valid `language` code. The [Python request example](../examples/python/youtube_transcript.py) reads the same structure from `data/sample-input.json` and prints every Dataset item returned by the hosted Actor.

## Which language codes are supported?

The input selector supports 47 codes, including `en`, `es`, `de`, `fr`, `pt`, `ja`, `zh-CN` and `zh-TW`. The web interface presents language names in a dropdown. If the selected language is not available for a video, the Actor returns `LANGUAGE_UNAVAILABLE` and does not substitute another language. See [`docs/input-reference.md`](input-reference.md).

## How do I use the transcript output in a spreadsheet?

Export the Dataset as CSV or Excel from Apify. Use `videoId`, `title`, `languageRequested`, `segmentCount`, `status` and `errorCode` for the overview; keep the JSON export when you need the nested `segments` array with timestamps.

## What happens when a video has no transcript?

The Actor continues with the remaining unique URLs and writes one error item for that video. It uses a stable code such as `NO_TRANSCRIPT`, `LANGUAGE_UNAVAILABLE` or `VIDEO_UNAVAILABLE`, leaves `segments` empty and does not charge the transcript-delivered event for that row.

## What is the billing unit?

The billing unit is one complete successful transcript delivered to the Dataset. The active Apify tier determines the exact per-transcript price. Error rows, empty transcripts and results stopped by the run charge limit are not charged as transcript events.
