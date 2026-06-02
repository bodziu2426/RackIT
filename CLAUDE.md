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

## Tech Stack (Decided)

- **Backend:** Python + FastAPI
- **Database:** SQLite + SQLAlchemy
- **Mobile app:** Flutter (Dart)
- **AI assistant (Phase 5):** Claude API integrated into Python backend

Architecture: Flutter app talks to Python API over HTTP. Python handles all logic, data, and AI.

## Learning Roadmap

Claude acts as programming mentor — teach step by step, explain the why, ask comprehension questions. Do not dump full solutions.

### Phase 1 — Python Foundations
**Learn:** Variables, data types, functions, lists, dictionaries, loops, conditionals, JSON
**Build:** Script that reads the Excel workout plan and converts it to clean JSON
**Scope:** ~2–3 weeks

### Phase 2 — Backend API with FastAPI
**Learn:** What an API is, HTTP methods (GET/POST), endpoints, request/response, Pydantic validation
**Build:** Running Python server — `GET /workout/push`, `POST /session`, testable in browser
**Scope:** ~2–3 weeks

### Phase 3 — Database with SQLite + SQLAlchemy
**Learn:** SQLAlchemy ORM, database models, CRUD operations
**Build:** Persistent storage — exercises, sessions, logged sets, weight progression history
**Note:** User knows SQL well — this phase should click fast
**Scope:** ~1–2 weeks

### Phase 4 — Flutter Mobile App
**Learn:** Dart basics, Flutter widgets, screen navigation, state management, HTTP calls
**Build:** Phone app — workout screen, exercise cards, logging sets, history view
**Scope:** ~4–6 weeks

### Phase 5 — AI Workout Assistant
**Learn:** Claude API integration, prompt engineering, structuring context
**Build:** Assistant that analyses training history and gives personalised advice
**Scope:** ~1–2 weeks

### Current status
Phase 1 — not started

---

*Update this file as the project evolves so it stays useful across machines.*
