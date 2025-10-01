# Turning Style Study – Sphero EDU

## What this does
Compares two turning styles with identical speed/timing:
- A = Sharp (instant 90° heading change)
- B = Smooth (heading swept in small steps over the same duration)

## Files
- sphero_turning_style.py  — async Sphero EDU script
- videos/
  - A_sharp_90.mp4
  - B_smooth_90.mp4

## How to run
1) Open Sphero EDU, load `sphero_turning_style.py`.
2) Set `COND = "A"` for sharp or `COND = "B"` for smooth.
3) Place robot at start mark (taped “L” corner).
4) Run once per condition to record video.

## Filming notes
- Keep camera framing, lighting, and surface identical.
- Use the same audible cue (“Three, two, one, go.”).
- PRE=1.0s, TURN_T=1.5s, AFTER=2.0s identical across A/B.

## Survey items (copy into Qualtrics)
Q1: I would trust this robot to navigate safely around me. (1–7)
Q2: What aspects of the robot’s movement most influenced your judgment? Please explain.

## Analysis (paired)
Use the provided Python/R snippet in the report to compute t-test and Cohen's d.
