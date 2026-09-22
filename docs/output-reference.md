# Output reference

The default Dataset contains one item for each unique input video ID. All fields below are present in both successful and error rows unless noted as nullable.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `videoId` | String | Yes | Normalized YouTube video ID. |
| `videoUrl` | URI string | Yes | Canonical public watch URL. |
| `status` | `success` or `error` | Yes | Whether a complete transcript was delivered. |
| `title` | String or null | Yes | Public title when available. `null` means the title could not be recovered. |
| `languageRequested` | String | Yes | Validated language code sent for this result. |
| `segmentCount` | Integer | Yes | Number of items in `segments`; zero for error rows. |
| `segments` | Array | Yes | Timestamped transcript segments. Empty for error rows. |
| `segments[].start` | Number | For segment rows | Start time in seconds. |
| `segments[].duration` | Number | For segment rows | Segment duration in seconds. |
| `segments[].text` | String | For segment rows | Caption text. |
| `errorCode` | String or null | Yes | Stable classification such as `NO_TRANSCRIPT` or `LANGUAGE_UNAVAILABLE`. |
| `errorMessage` | String or null | Yes | User-facing explanation for an error. |

Nullable fields are explicit: `title` can be unavailable, while `errorCode` and `errorMessage` are `null` on success. A successful item is billable only when `segments` is non-empty and complete. Error items remain useful for auditing failed inputs but are not billable transcript events.
