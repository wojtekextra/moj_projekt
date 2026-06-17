# Kalkulator Projekt

Projekt kalkulatora z automatyzacją CI.

## Quick Start
1. Sklonuj repozytorium.
2. Zainicjuj środowisko i zainstaluj zależności:
   `bash scripts/create_venv.sh`
3. Aktywuj środowisko: `source venv/bin/activate` (Windows: `source venv/Scripts/activate`)

## Uruchamianie narzędzi
- **Testy:** `bash scripts/test.sh`
- **Linting:** `bash scripts/lint.sh`
- **Formatowanie:** `bash scripts/format_check.sh`

## Pipeline CI
Projekt używa GitHub Actions. Każdy `push` do gałęzi `main` lub `develop` automatycznie uruchamia:
1. Instalację środowiska.
2. Sprawdzenie formatowania (Black).
3. Analizę statyczną (Pylint).
4. Testy jednostkowe (pytest).