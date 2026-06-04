# Faza 3 — Baza danych: SQLite + SQLAlchemy

**Cel:** Podłączyć bazę danych do backendu — wyniki treningów będą trwale zapisywane.

**Zakres:** ~1–2 tygodnie  
**Status:** 🔲 Nie rozpoczęta — zacznij po ukończeniu Fazy 2

**Uwaga:** masz doświadczenie z SQL, więc ta faza powinna pójść szybko. Nacisk będzie na SQLAlchemy ORM, nie na sam SQL.

---

## Czego się nauczysz
- SQLAlchemy ORM — modele jako klasy Python zamiast surowego SQL
- Migracje (Alembic)
- CRUD: Create, Read, Update, Delete przez ORM

## Co zbudujesz
Trwała baza danych z tabelami:
- `exercises` — lista ćwiczeń z planu
- `sessions` — każda sesja treningowa (data, typ: PUSH/PULL/NOGI)
- `sets` — zalogowane serie (ciężar, powt., RIR)
- `progression_history` — historia zmian ciężarów

## Deliverable
Backend z Fazy 2 teraz czyta i zapisuje do bazy danych zamiast do pliku JSON.
