# Gaia Export

## Summary

A small wrapper around [kk7ds](https://github.com/kk7ds/)' [gaiagpsclient](https://github.com/kk7ds/gaiagpsclient) tool to help [NWHikers](https://www.nwhikers.net/forums/viewtopic.php?p=1272948) bulk export their GPX tracks.

<hr>

## Instructions

1. Log into Gaia GPS in your browser
2. Retrieve the SessionID cookie from your browser.
   1. Chrome Instructions: [here](https://developer.chrome.com/docs/devtools/application/cookies)
   2. Firefox Instructions: [here](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html)
   3. Edge Instructions: [here](https://support.microsoft.com/en-us/microsoft-edge/view-cookies-in-microsoft-edge-a7d95376-f2cd-8e4a-25dc-1de753474879)

3. Install [Docker](https://docs.docker.com/engine/install/)

4. Run Docker and pass in a directory on your computer to which you wish to save the tracks as well as your SessionID
   ```bash
   docker run -v $(pwd)/tracks:/tmp/ zimmertr/gaiaexport:latest $SESSION_ID
   ```

<hr>

## Example

```bash
$> docker run -v $(pwd)/tracks:/tmp/ zimmertr/gaiaexport:latest $SESSION_ID
Wrote '/tmp/New Track 113022 84422 AM.gpx'
Wrote '/tmp/Rocky Run - Ramparts - East Alta - Chikamin - Iceberg - Return.gpx'
Wrote '/tmp/Rocky Run - Ramparts - East Alta - Chikamin - Iceberg - Return - copy.gpx'
Wrote '/tmp/untitled.gpx'
Wrote '/tmp/Kilauea Iki Loop.gpx'
Wrote '/tmp/half trail, half bushwhack to ridge.gpx'
Wrote '/tmp/Golden Lakes Loop.gpx'
Wrote '/tmp/Mauna Loa #1.gpx'
Wrote '/tmp/Lennox Mount #1.gpx'
Wrote '/tmp/Frigid Mount #1.gpx'
Wrote '/tmp/Frigid Mount #2.gpx'
Wrote '/tmp/Grindstone M #1.gpx'
Wrote '/tmp/Grindstone M #1.gpx'
Wrote '/tmp/Tuesday Trip to Tarn Town.gpx'
Wrote '/tmp/Chikamin Pea #1.gpx'
```

