# Faza 1 — Python Podstawy

**Cel:** Nauczyć się podstaw Pythona i zbudować skrypt, który czyta plan treningowy z Excela i zapisuje go jako JSON.

**Zakres:** ~2–3 tygodnie  
**Status:** 🔲 W toku

---

## Sesje

### Sesja 1 — Setup + Python basics
**Status:** ✅ Ukończona  
**Uczysz się:** zmienne, typy danych (string, int, float), print(), komentarze  
**Ćwiczenie:** napisz skrypt, który przechowuje dane jednego ćwiczenia (nazwa, serie, zakres powtórzeń) i wypisuje je na ekran  
**Plik roboczy:** `sesja_1.py`

---

### Sesja 2 — Listy i słowniki
**Status:** ✅ Ukończona  
**Uczysz się:** list [], dict {}, dostęp do elementów, dodawanie, zagnieżdżanie  
**Ćwiczenie:** przedstaw jedno ćwiczenie jako słownik, a cały dzień treningowy jako listę słowników  
**Plik roboczy:** `sesja_2.py`

---

### Sesja 3 — Pętle i warunki
**Status:** ✅ Ukończona  
**Uczysz się:** for, if/elif/else, iterowanie po listach i słownikach  
**Ćwiczenie:** iteruj po liście ćwiczeń i wypisuj tylko te z zakresem powtórzeń poniżej 8  
**Plik roboczy:** `sesja_3.py`

---

### Sesja 4 — Funkcje
**Status:** ✅ Ukończona  
**Uczysz się:** def, parametry, return, po co w ogóle funkcje  
**Ćwiczenie:** napisz funkcję, która przyjmuje ćwiczenie i zwraca czy należy dodać ciężar (logika progresji)  
**Plik roboczy:** `sesja_4.py`

---

### Sesja 5 — JSON + zapis/odczyt plików
**Status:** ✅ Ukończona  
**Uczysz się:** moduł json, open(), read/write, json.dumps() / json.loads()  
**Ćwiczenie:** zapisz listę ćwiczeń do pliku .json, a następnie wczytaj ją z powrotem  
**Plik roboczy:** `sesja_5.py`

---

### Sesja 6 — openpyxl
**Status:** ✅ Ukończona  
**Uczysz się:** pip, instalacja paczek, otwarcie workbooka, iterowanie po arkuszach i wierszach  
**Ćwiczenie:** otwórz Plan_PPL_Dziennik_NEW.xlsx i wypisz nazwy wszystkich ćwiczeń z każdego arkusza  
**Plik roboczy:** `sesja_6.py`

---

### Sesja 7 — Pełny parser (deliverable)
**Status:** ✅ Ukończona  
**Budujesz:** `parse_plan.py` — czyta wszystkie 3 arkusze Excela i zapisuje do `workout_plan.json`  
**Output:** plik JSON z pełną strukturą planu: ćwiczenia, serie, zakresy, ciężary startowe  
**Plik roboczy:** `parse_plan.py` + `workout_plan.json`

---

## Pliki tej fazy

```
Training/
├── Faza_1_Python_Podstawy.md   ← ten plik
├── sesja_1.py
├── sesja_2.py
├── sesja_3.py
├── sesja_4.py
├── sesja_5.py
├── sesja_6.py
├── parse_plan.py               ← finalny deliverable
└── workout_plan.json           ← output parsera
```
