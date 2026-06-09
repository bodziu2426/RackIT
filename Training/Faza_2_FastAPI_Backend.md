# Faza 2 — Backend API z FastAPI

**Cel:** Zbudować działający serwer Python, który udostępnia dane treningowe przez HTTP.

**Zakres:** ~2–3 tygodnie  
**Status:** 🔲 Nie rozpoczęta — zacznij po ukończeniu Fazy 1

---

## Czego się nauczysz
- Czym jest API i jak działa HTTP (GET, POST, kody statusu)
- Jak działa FastAPI i dlaczego go używamy
- Uvicorn — serwer uruchamiający aplikację
- Endpointy, request, response, path parameters
- Pydantic — walidacja danych wejściowych i wyjściowych
- Swagger UI — automatyczna dokumentacja API

## Co zbudujesz
Działający serwer lokalny z endpointami:
- `GET /workout/push` — zwraca plan PUSH z workout_plan.json
- `GET /workout/pull` — zwraca plan PULL
- `GET /workout/legs` — zwraca plan NOGI
- `POST /session` — przyjmuje wyniki sesji treningowej

## Deliverable
Serwer testowalny w przeglądarce i przez Swagger UI (wbudowany w FastAPI).

---

## Sesje

### Sesja 1 — Czym jest API + pierwszy endpoint
**Status:** 🔲 Nie rozpoczęta  
**Uczysz się:** HTTP, GET/POST, request/response, instalacja FastAPI i uvicorn  
**Ćwiczenie:** serwer z jednym endpointem `GET /` zwracającym "Hello RackIT"  
**Plik roboczy:** `main.py`

---

### Sesja 2 — Path parameters i serwowanie danych
**Status:** 🔲 Nie rozpoczęta  
**Uczysz się:** parametry w URL (`/workout/{day}`), wczytywanie JSON z pliku  
**Ćwiczenie:** endpoint `GET /workout/{day}` zwraca ćwiczenia dla push/pull/legs  
**Plik roboczy:** `main.py`

---

### Sesja 3 — Pydantic models
**Status:** 🔲 Nie rozpoczęta  
**Uczysz się:** klasy Pydantic, typowanie danych, automatyczna walidacja  
**Ćwiczenie:** zdefiniuj model `Exercise` i `WorkoutDay`, zwróć dane z typami  
**Plik roboczy:** `models.py` + `main.py`

---

### Sesja 4 — POST endpoint
**Status:** 🔲 Nie rozpoczęta  
**Uczysz się:** przyjmowanie danych w request body, POST vs GET  
**Ćwiczenie:** endpoint `POST /session` przyjmuje wyniki treningu i zwraca potwierdzenie  
**Plik roboczy:** `main.py` + `models.py`

---

### Sesja 5 — Logika progresji w API
**Status:** 🔲 Nie rozpoczęta  
**Uczysz się:** łączenie endpointów z logiką biznesową, reużywanie kodu z Fazy 1  
**Ćwiczenie:** POST /session analizuje wyniki i zwraca które ćwiczenia wymagają zwiększenia ciężaru  
**Plik roboczy:** `main.py` + `logic.py`

---

### Sesja 6 — Deliverable: pełne API
**Status:** 🔲 Nie rozpoczęta  
**Budujesz:** kompletny serwer z wszystkimi endpointami, Swagger UI, obsługa błędów  
**Plik roboczy:** `main.py`, `models.py`, `logic.py`

---

## Pliki tej fazy

```
Training/Faza_2/
├── main.py        ← serwer FastAPI
├── models.py      ← modele Pydantic
└── logic.py       ← logika progresji (z Fazy 1)
```
