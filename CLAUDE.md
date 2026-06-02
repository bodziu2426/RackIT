# RackIT — Gym Tracker Project

## Project Overview

Gym training helper for tracking PPL (Push/Pull/Legs) workouts. Future goal: Android app or website.
The repo holds the Excel training template and will eventually hold the app/backend code.

## Repository Structure

```
Plan_PPL_Dziennik_NEW.xlsx   — Training plan template (PPL split, do not delete)
CLAUDE.md                    — This file (project memory, auto-loaded by Claude Code)
```

## Training Plan Structure (Excel)

**3 sheets (PPL split):**
- `PUSH – Klatka · Barki · Triceps` — 5 exercises: Bench Press, Incline DB, OHP, Cable Lateral Raise, Dips
- `PULL – Plecy · Biceps` — 3 exercises: Deadlift, Pull-ups, DB Curls
- `NOGI – Uda · Pośladki` — 3 exercises: Squat, RDL, Hip Thrust

**Exercise row columns (20 total):**

| Col | Field |
|-----|-------|
| 0 | # |
| 1 | Exercise name |
| 2 | Sets in plan |
| 3 | Rep range |
| 4 | Starting weight |
| 5 | Last set to failure? |
| 6–8 | Series 1: Weight (kg) / Reps / RIR target |
| 9–11 | Series 2: Weight (kg) / Reps / RIR target |
| 12–14 | Series 3: Weight (kg) / Reps / RIR target |
| 15–17 | Series 4: Weight (kg) / Reps / RIR target |
| 18 | Add weight next session? |
| 19 | Technical notes |

**Progression rule:** when the last set (to failure) exceeds the upper rep range → add 2.5 kg next session.

**RIR color coding:** green = RIR 3, blue = RIR 2, orange = RIR 1, red = RIR 0 / failure.

Each sheet also contains a **warmup section** below the exercise table with phases, durations, and cues.

## Key Decisions / Notes

- Excel file is a template — actual logged set data (weight/reps per series) is filled in per session
- Deadlift and Squat are NEVER taken to full failure (spine safety)
- Progression increment: 2.5 kg

## Tech Stack (TBD)

Not decided yet. Candidates: Python backend + web frontend, or React Native for Android.

---

*Update this file as the project evolves so it stays useful across machines.*
