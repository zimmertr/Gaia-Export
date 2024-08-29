# Gaia Export

## Summary

A small wrapper around [kk7ds](https://github.com/kk7ds/)' [gaiagpsclient](https://github.com/kk7ds/gaiagpsclient) tool to help [NWHikers](https://www.nwhikers.net/forums/viewtopic.php?p=1272948) bulk export their GPX tracks. 

Batteries not included, this was a quick hack.

<hr>

## Instructions

1. Log into Gaia GPS in your browser
2. Retrieve the SessionID cookie from your browser.
   1. Chrome Instructions: [here](https://developer.chrome.com/docs/devtools/application/cookies)
   2. Firefox Instructions: [here](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html)
   3. Edge Instructions: [here](https://support.microsoft.com/en-us/microsoft-edge/view-cookies-in-microsoft-edge-a7d95376-f2cd-8e4a-25dc-1de753474879)

3. Run the script

   1. With Docker:

      1. Install [Docker](https://docs.docker.com/engine/install/)

      2. Run Docker and pass in a directory on your computer to which you wish to save the tracks as well as your SessionID
         ```bash
         docker run -v $(pwd)/tracks:/tmp/ zimmertr/gaiaexport:latest $SESSION_ID
         ```

   2. With Python:

      1. Install [gaiagpsclient](https://github.com/kk7ds/gaiagpsclient?tab=readme-ov-file#installation)

      2. Run the script and pass in the SessionID. Tracks will be saved to `/tmp/`.
         ```bash 
         python3 bulk_export.py $SESSION_ID
         ```


<hr>

## Example

![https://raw.githubusercontent.com/zimmertr/Gaia-Export/main/Screenshot.png](https://raw.githubusercontent.com/zimmertr/Gaia-Export/main/Screenshot.png)