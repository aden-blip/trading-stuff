#!/usr/bin/env python3
"""Turn a screen recording into things Claude can actually read.

Claude cannot open a video file. It can read images and text. This splits a recording into
both: the audio track, for transcription, and still frames, for the chart.

    python3 tools/video_notes.py <video> [--every SECONDS] [--at 1:23,4:05,...] [--out DIR]

--every   a frame every N seconds (default 20). Use for a first pass over a whole recording.
--at      frames at exact timestamps instead, once the transcript says where to look.
          Accepts 83, 1:23 or 0:01:23.

Needs ffmpeg, which is not in the container by default:  pip install imageio-ffmpeg
"""
import argparse, os, subprocess, sys


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg is missing. Run: pip install imageio-ffmpeg")


def seconds(stamp):
    parts = [float(p) for p in str(stamp).strip().split(":")]
    total = 0.0
    for p in parts:
        total = total * 60 + p
    return total


def run(exe, args):
    r = subprocess.run([exe, "-y", "-loglevel", "error"] + args, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg failed: " + r.stderr.strip()[:400])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--every", type=float, default=20.0)
    ap.add_argument("--at", default="")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    exe = ffmpeg()
    out = a.out or os.path.splitext(a.video)[0] + "_notes"
    frames = os.path.join(out, "frames")
    os.makedirs(frames, exist_ok=True)

    # the whole audio track, mono and small, ready to transcribe
    audio = os.path.join(out, "audio.mp3")
    run(exe, ["-i", a.video, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", audio])

    made = []
    if a.at:
        for stamp in [s for s in a.at.replace(" ", "").split(",") if s]:
            t = seconds(stamp)
            path = os.path.join(frames, "t%07.1f.png" % t)
            run(exe, ["-ss", str(t), "-i", a.video, "-frames:v", "1", path])
            made.append((t, path))
    else:
        run(exe, ["-i", a.video, "-vf", "fps=1/%g" % a.every, os.path.join(frames, "f_%04d.png")])
        for i, name in enumerate(sorted(os.listdir(frames))):
            made.append((i * a.every, os.path.join(frames, name)))

    dur = subprocess.run([exe, "-i", a.video], capture_output=True, text=True).stderr
    dur = next((l.strip() for l in dur.splitlines() if "Duration" in l), "duration unknown")

    print("# %s" % os.path.basename(a.video))
    print(dur)
    print("\naudio for transcription: %s (%.1f MB)" % (audio, os.path.getsize(audio) / 1e6))
    print("\n%d frames in %s:" % (len(made), frames))
    for t, p in made:
        print("  %-9s %s" % ("%d:%02d" % (int(t) // 60, int(t) % 60), p))
    print("\nNext: transcribe the audio, find the moments that matter, then re-run with")
    print("  --at <those timestamps>  for frames at exactly those points.")


if __name__ == "__main__":
    main()
