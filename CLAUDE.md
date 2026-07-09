# RackIT — Gym Tracker Project

## Project Overview

Gym training tracker — replaces the Excel file (Plan_PPL_Dziennik_NEW.xlsx) with a proper app where workout results are entered during/after training. The app handles logging sets, tracking weight progression, and will eventually provide AI-powered training advice.

**Two frontends, one backend** — both serve as learning tools and usable products:
- Web app (HTML/CSS/JS or framework)
- Flutter mobile app (Android)

Both talk to the same Python FastAPI backend.

The repo holds the Excel training template (reference/migration source) and will hold all app/backend code.

## Repository Structure

```
Plan_PPL_Dziennik_NEW.xlsx   — Training plan template (PPL split, reference only — do not delete)
CLAUDE.md                    — This file (project memory, auto-loaded by Claude Code)
Training/                    — All learning session files and exercises go here
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

## Athlete Profile

- **Waga:** 87 kg
- **Wzrost:** 178 cm
- **Staż:** kilka lat z przerwami
- **Cel:** sprawność + zdrowie długoterminowe — mniej kontuzji, lepszy performance w squashu i tenisie stołowym, estetyka jako efekt uboczny
- **Częstotliwość:** 3x tydzień (PPL raz w tygodniu)
- **Uwaga:** przy ćwiczeniach z masą ciała (podciąganie, dipy) uwzględniaj wagę 87 kg — to znacząco wpływa na ocenę wyników

## Claude's Dual Role

Claude operates in two modes within this project:

### 1. Programming Mentor
Teaches programming step by step. Explains the why, asks comprehension questions, does not dump full solutions.

### 2. Personal Trainer & Strength Coach
Analyses workout results from Excel files shared by the user and suggests plan optimizations. Bases recommendations on:
- Logged sets, weights, reps, and RIR values
- Progression trends over time
- Recovery, volume, and intensity balance

**Workflow:** User shares Excel file with recent workout → Claude reads and analyses results → proposes specific changes to exercises, weights, rep ranges, or structure.

## Training Principles (evidence-based, agreed 17.06.2026)

**Progresja piramidy — cała piramida rośnie razem:**
Przy każdej progresji (+2.5 kg) wszystkie serie w piramidzie rosną o +2.5 kg, nie tylko ostatnia. Uzasadnienie: objętość całkowita (ciężar × serie × powt.) jest głównym czynnikiem hipertrofii — jeśli tylko S4 rośnie, S1–S3 nie generują bodźca adaptacyjnego.

**Przyrost dla izolacji — +1 kg zamiast +2.5 kg:**
Małe grupy mięśniowe (naramienne, biceps) — skok +2.5 kg to za dużo. Stosuj +1 kg dla odwodzenia, uginań i podobnych ćwiczeń izolacyjnych.

**Zakres powtórzeń OHP — zmieniony na 6–8 (był 6–10):**
Szerszy zakres utrudnia ocenę progresji. 6–8 daje czytelny sygnał kiedy zwiększyć ciężar.

**Uginanie hantlami — S2 = S3:**
Skok z S2 do S3 (+2.5 kg na hantel) był za duży — biceps tego nie wytrzymuje. S2 i S3 powinny być na tym samym ciężarze aż do stabilizacji zakresu.

**Dipy — kolejne cele:**
BW × 8 osiągnięte. Następny cel: BW × 12 na S1, potem obciążenie na pasie.

**Podciąganie — kolejne cele:**
Cel: BW × 8 stabilnie na S1 przez 2 sesje → wtedy pas z obciążeniem.

**Plan NOGI — przeprojektowany (18.06.2026), priorytet: funkcjonalność + squash/tenis stołowy:**
1. Przysiad ze sztangą — 3×5-8, piramida, NIE do upadku (bezpieczeństwo kręgosłupa)
2. Bulgarian Split Squat — 3×8-10/noga, stały ciężar
3. Hip Thrust ze sztangą — 3×10-12, piramida
4. Leg Curl jednonóż (maszyna) — 3×10-12, stały ciężar, +2,5 kg przy progresji (minimalny skok maszyny)
5. Odwodzenie na wyciągu jednonóż — 3×12-15, stały ciężar, +1 kg przy progresji
6. Copenhagen Plank — 2×10-15s, BW
Rozgrzewka: Hip CARs (5 min) — mobilność biodra dla squasha.

**NOGI — sesja 1 (18.06.2026):**
Przysiad: 60/70/80 kg × 8/8/8 → S1 za lekki
BSS: BW × 10/10/11
Hip Thrust: 40/50/60 × 12/12/13
Leg Curl jednonóż: 25 kg × 10/10/12
Odwodzenie jednonóż: 3.75/3.75/6.25 → nieregularne
Copenhagen Plank: 15s/20s

**NOGI — sesja 2 (09.07.2026) + plan na następny trening:**
Przysiad: 70/75/80 × 8/8/8, S3 RIR 2 → progresja → następna sesja 75/80/85 kg
BSS: 2×6 × 10/10/11 → progresja → następna sesja 2×10 kg (zakres 8-10, cel dolny próg)
Hip Thrust: 50/60/65 × 12/12/13 (2. sesja z tym wynikiem) → progresja → następna sesja 55/65/70 kg
Leg Curl jednonóż: 25 kg × 10/11/13 → progresja → następna sesja 27,5 kg (+2,5 kg min. skok maszyny)
Odwodzenie jednonóż: 5/7,5/7,5 × 15/12/13 → S3 < 15 → zostań 7,5 kg × 3 serie
Copenhagen Plank: 20s/25s → następna sesja cel 25s × 2

**PUSH — ustalenia i aktualny stan (aktualizacja 07.07.2026):**

Wyciskanie sztangi płaska — aktualny ciężar: 62,5/67,5/72,5/77,5 kg, zakres 6–8:
- 23.06: S3=7, S4=7 → zostań
- 07.07: S3=8, S4=8 (S4 z pomocą asekurującego na 8. powt.) → zostań
- Trigger progresji: S4 = 77,5 × 8 czysto bez pomocy → wtedy +2,5 kg na całą piramidę

Wyciskanie hantlami skośna +30° — aktualny ciężar: 2×22,5 / 2×25 / 2×25 kg:
- **PRIORYTET: tempo 3–4s eccentric > liczba powt.** Jeśli tempo się rozjeżdża, zejdź z ciężarem.
- Reset po 30.06 (klatka bardzo zmęczona po treningu przy 2×25). Piramida: S1=22,5 (feeder), S2 i S3=25 (praca).
- 07.07: 22,5×8 / 22,5×8 / 25×8 → zostań, obserwuj klatkę po treningu
- Progresja: gdy S3 kończy się na RIR 0–1 przy utrzymanym tempie przez 2 treningi → +2,5 kg na hantel (cała piramida)

OHP sztangą — aktualny ciężar: 35/40/42/45 kg, zakres 6–8:
- Zmiana piramidy (23.06): stara 30/35/40/45 — S1 był rozgrzewką (możliwe 12–14 powt.). Nowa spłaszczona: 35/40/42/45.
- 07.07: 35×8 / 40×8 / 42×8 / 45×7 — S4 bez wybicia z nóg ✓ — piramida działa
- Trigger progresji: S4 = 45 × 8 czysto → +2,5 kg na całą piramidę (→ 37,5/42,5/44,5/47,5)

Odwodzenie na wyciągu jednorącz — aktualny ciężar: 3 × 7,5 kg:
- 07.07: 13/13/13 → cel 15 powt., +1 kg przy triggerze (izolacja)

Dipy — aktualny ciężar: -6,25 / -6,25 / -6,25 / BW (aktualizacja 07.07.2026):
- S1 i S2 osiągnęły 12 powt. przy -9,4 → obie przesunięte na -6,25
- Protokół: S4=BW ✓ → S3 gdy ≥12 → BW → S2 gdy ≥12 → BW → S1 gdy ≥12 → BW → gdy wszystkie BW × 12 przez 2 sesje → pas z obciążeniem

## Key Decisions / Notes

- Excel file is a reference and migration source — NOT the target solution
- Deadlift and Squat are NEVER taken to full failure (spine safety)
- Progression increment: 2.5 kg (compounds) / 1 kg (isolation)
- **Dostępne talerze na siłowni:** 0,5 / 1 / 1,5 / 2,5 kg — BRAK 1,25 kg. Nie można zrobić +2,5 kg symetrycznie. Praktyczny odpowiednik: **+3 kg całkowite (+1,5 kg na stronę)** — to standardowy krok progresji dla tej siłowni zamiast +2,5 kg.
- **Wiosłowanie sztangą — reset piramidy (07.07.2026):** Piramida wyrównana do okrągłych liczb: **60/65/70/75 kg**. Progresja: **+5 kg całkowite** (+2,5 kg na stronę) gdy trigger → 65/70/75/80 itd.
- Target user flow: open app → log sets/weight/RIR → app saves, calculates progression, shows history

## Tech Stack (Decided)

- **Backend:** Python + FastAPI (shared by both frontends)
- **Database:** SQLite + SQLAlchemy
- **Frontend 1:** Web app (HTML/CSS/JS or framework — TBD)
- **Frontend 2:** Flutter mobile app (Dart, Android)
- **AI assistant (Phase 5):** Claude API integrated into Python backend

Architecture: both frontends talk to Python API over HTTP. Python handles all logic, data, and AI.

## Learning Roadmap

Claude acts as programming mentor — teach step by step, explain the why, ask comprehension questions. Do not dump full solutions.

### Phase 1 — Python Foundations
**Learn:** Variables, data types, functions, lists, dictionaries, loops, conditionals, JSON
**Build:** Script that reads the Excel workout plan and converts it to clean JSON
**Scope:** ~2–3 weeks

**Session breakdown:**
- Session 1: Setup + Python basics — variables, strings, numbers, print()
- Session 2: Lists and dictionaries — represent one exercise as a dict
- Session 3: Loops and conditions — for loops, if/elif/else, iterate exercises
- Session 4: Functions — def, parameters, return values
- Session 5: JSON + File I/O — json module, save/load exercise data to .json file
- Session 6: openpyxl — pip, open workbook, iterate sheets/rows, print exercise names
- Session 7: Full parser (deliverable) — parse_plan.py reads all 3 sheets → workout_plan.json

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

### Phase 4 — Web Frontend
**Learn:** HTML/CSS/JS basics (czysty JS bez frameworka), DOM manipulation, fetch API, formularze
**Build:** Web interface — plan treningowy, formularz logowania serii, historia, decyzja progresji
**Scope:** TBD
**Decyzja:** czysty HTML/CSS/JS najpierw, React/Vue po opanowaniu podstaw

### Phase 6 — AI Workout Assistant
**Learn:** Claude API integration, prompt engineering, structuring context
**Build:** Assistant that analyses training history and gives personalised advice
**Scope:** ~1–2 weeks

### Current status
Phase 1 — ✅ UKOŃCZONA
- ✅ Sesja 1: zmienne, typy danych, print()
- ✅ Sesja 2: listy i słowniki
- ✅ Sesja 3: pętle i warunki
- ✅ Sesja 4: funkcje
- ✅ Sesja 5: JSON + zapis/odczyt plików
- ✅ Sesja 6: openpyxl — otwieranie Excela, iter_rows(), dostęp do komórek
- ✅ Sesja 7: pełny parser (deliverable) — parse_plan.py + workout_plan.json

Phase 2 — ✅ UKOŃCZONA
- ✅ Sesja 1: FastAPI + uvicorn — pierwszy serwer, 3 endpointy GET (/workout/push, /workout/pull, /workout/legs), Swagger UI, wczytywanie JSON przy starcie, dekoratory
- ✅ Sesja 2: POST /session — modele Pydantic (Series + rep_range_max, Sesion), funkcja add_weight(), endpoint zwraca listę słowników z decyzją progresji dla każdej serii, przetestowane w Swagger

Phase 3 — ✅ UKOŃCZONA
- ✅ Sesja 1: SQLite + SQLAlchemy — database.py (engine, Base, SessionLocal), models.py (SesjaDB z kolumnami), zapis do bazy przy POST /session, dane widoczne w SQLite Viewer
- ✅ Sesja 2: GET /history — odczyt historii z bazy, db.query(SesjaDB).all(), backend end-to-end działa

Phase 4 — Web Frontend — 🔄 W TOKU
- ✅ Sesja 1: HTML/CSS/JS intro — index.html szkielet, StaticFiles w FastAPI (app.mount), strona serwowana przez http://127.0.0.1:8000/static/index.html
- 🔄 Następny krok: utworzyć app.js, podłączyć przez <script src="app.js"> przed </body>, napisać pierwszy fetch() do GET /workout/push

---

*This file is the single source of truth for project context. Update it after every meaningful decision or session so it stays useful across machines and conversations.*
