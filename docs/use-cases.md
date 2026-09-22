# Use cases

These workflows use the hosted Actor and its default Dataset contract. Each one can start with the small input in [`data/sample-input.json`](../data/sample-input.json).

## Build a searchable timestamp index

Send a list of public video URLs with `language: "en"`. Use `videoId`, `title`, `segments[].start` and `segments[].text` to create search records that link a match back to the exact moment in the source video. Check `status` and skip error rows when building the index.

## Create a JSON caption corpus for AI workflows

Run a small or medium batch, export the Dataset as JSON and preserve `languageRequested` with every segment. The complete `segments` array is suitable for chunking, summarization, translation and retrieval pipelines without downloading video or audio.

## Audit transcript and language availability

Submit the same video list with different valid language selections. Compare `status`, `languageRequested`, `segmentCount` and `errorCode` to distinguish an available transcript from `LANGUAGE_UNAVAILABLE`, `NO_TRANSCRIPT` or `VIDEO_UNAVAILABLE`. Every unique input remains represented by one Dataset item.
