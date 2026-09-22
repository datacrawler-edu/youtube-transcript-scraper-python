# Input reference

The Actor accepts a JSON object with a required list of public YouTube video URLs and an optional validated language code.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `videoUrls` | Array of strings | Yes | `https://www.youtube.com/watch?v=jNQXAC9IVRw` | One or more public YouTube watch, `youtu.be`, Shorts, live or embed URLs. Duplicate video IDs are processed once in first-seen order. |
| `language` | String | No | `en` | Requested transcript language. Defaults to English and must be selected from the supported enum. |

## Validation and limits

- Maximum input items: 5,000 URL values.
- Maximum URL value length: 500 characters.
- Defaults: `language` is `en` when omitted.
- Mutually exclusive fields: none.

## Supported language codes

`en`, `es`, `es-ES`, `de`, `fr`, `it`, `pt`, `pt-BR`, `nl`, `pl`, `ru`, `uk`, `tr`, `ar`, `he`, `fa`, `hi`, `bn`, `id`, `ms`, `vi`, `th`, `ko`, `ja`, `zh-CN`, `zh-TW`, `cs`, `da`, `fi`, `no`, `sv`, `el`, `hu`, `ro`, `sk`, `bg`, `hr`, `sr`, `sl`, `ca`, `eu`, `gl`, `ta`, `te`, `mr`, `ur`, `sw`.

The Apify web input shows human-readable names in a dropdown, so users do not need to type a code. An invalid code is rejected before the run starts. A valid code can still be unavailable for a particular video; that result is returned as `LANGUAGE_UNAVAILABLE` rather than silently substituting another language.
