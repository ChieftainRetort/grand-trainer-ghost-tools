# Contributing to grand-trainer-ghost-tools

Thanks for your interest in the Grand Trainer ghost tooling project.

## Ground rules

- This project targets **single-player / offline** sessions of *There Are No Ghosts at the Grand Trainer* only.
- Do not submit patches that touch networked or anti-cheat protected code paths.
- Keep pull requests scoped to a single pipeline stage (handler, processor, or driver).

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m trainers.ghost_runner --dry-run
```

## Style

- Python 3.11+, `ruff` for lint, `black` for format.
- New ingest handlers go in `handlers/`, new processors in `processors/`.
- Every output driver must declare a `NAME` constant and implement `emit()`.

## Reporting

Open an issue with the game build number, the trainer stage that failed,
and the contents of `logs/ghost_runner.log`.