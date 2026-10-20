# Pipeline Architecture

`grand-trainer-ghost-tools` runs a fixed-order worker pipeline:

```
[handlers] -> [processors] -> [drivers]
```

- **handlers** ingest data: pattern scans, save-file watches.
- **processors** transform payload dicts: spirit state, trainer flags, ghost filtering.
- **drivers** emit results: console HUD, overlay window.

Each stage implements `run(payload: dict) -> dict`. Failures in one stage
are logged and abort the tick, so a bad pattern scan never corrupts the
trainer flag write that follows.

## Adding a stage

1. Drop a module in `handlers/`, `processors/`, or `drivers/`.
2. Export a class with `__init__(cfg, memory)` and `run(payload)`.
3. Append the dotted path to `pipeline.stages` in `config/default.yaml`.