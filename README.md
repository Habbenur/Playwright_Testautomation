# Playwright Testautomation

Övningsprojekt för UI-testautomation med [Playwright](https://playwright.dev/python/) och pytest, mot en testapplikation för studenthantering (FSH-kurs).

## Installation

```bash
pip install pytest playwright
playwright install
```

## Konfiguration

Projektet körs med headed Chromium via `pytest.ini`:

```ini
[pytest]
addopts = --headed --browser chromium --slowmo 2000
```

Byt `--browser chromium` till `--browser webkit` för att köra i Safari/WebKit istället.

## Köra testerna

```bash
pytest
```

## Testöversikt

`tests/test_google_search.py` innehåller UI-tester mot testapplikationen:

- Verifierar sidtitel
- Skapa student via UI (två varianter: `test_id`- och placeholder-baserade selektorer)
- Redigera student
- Ta bort student

> **Notering:** API-nyckeln i testfilen är en fast testnyckel mot en kursspecifik testmiljö, inte en riktig hemlighet.
