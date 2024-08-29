import sys
import subprocess
import os
import re

def list_tracks(session_id):
    tracks = subprocess.run(
        ["gaiagps", "--sessionid", session_id, "track", "list", "--by-id"],
        stdout=subprocess.PIPE,
        text=True
    )

    return tracks.stdout.strip().splitlines()


# Remove invalid filename characters
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>\'|]', "", name)


def export_track(session_id, track_id, track_name):
    sanitized_name = sanitize_filename(track_name)

    subprocess.run(
        ["gaiagps",
            "--sessionid", session_id,
            "track", "export", track_id,
            f"/tmp/{sanitized_name}.gpx"
        ]
    )


def main(session_id):
    tracks = list_tracks(session_id)

    for track in tracks:
        # Parse STDOUT of gaiagps client
        parts = track.split(' ', 5)
        track_id = parts[0]
        track_name = parts[5]

        export_track(session_id, track_id, track_name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: export_tracks.py $SESSION_ID")
        sys.exit(1)

    session_id = sys.argv[1]
    main(session_id)
