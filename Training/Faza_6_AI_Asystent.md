# Faza 6 — AI Asystent Treningowy

**Cel:** Zintegrować Claude API z backendem — asystent analizuje historię treningów i daje spersonalizowane porady.

**Zakres:** ~1–2 tygodnie  
**Status:** 🔲 Nie rozpoczęta — zacznij po ukończeniu Fazy 5

---

## Czego się nauczysz
- Integracja Claude API (Anthropic SDK)
- Prompt engineering — jak konstruować kontekst z danych treningowych
- Strumieniowanie odpowiedzi (streaming)

## Co zbudujesz
Endpoint w FastAPI: `POST /ai/advice`
- Przyjmuje historię sesji z bazy danych
- Wysyła do Claude jako kontekst
- Zwraca spersonalizowaną analizę i rekomendacje

Przykładowe pytania do asystenta:
- "Czy powinienem zwiększyć ciężar na OHP?"
- "Jak wygląda mój postęp na ławce w ostatnim miesiącu?"
- "Czy widać oznaki przetrenowania?"

## Deliverable
Działający chat w aplikacji web i/lub Flutter, który zna historię twoich treningów.
