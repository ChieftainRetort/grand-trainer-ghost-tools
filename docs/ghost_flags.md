# Trainer flag reference

| Flag             | Bit  | Effect                                         |
| ---------------- | ---- | ---------------------------------------------- |
| `no_ghost`       | 0x01 | Suppresses ghost spawns at the Grand Trainer.  |
| `see_ghost`      | 0x02 | Reveals dormant spirits as manifested.         |
| `freeze_spirit`  | 0x04 | Freezes spirit state transitions.              |

Flags are OR-composed and written to the trainer pointer address resolved
by `GhostScanHandler`. Combine freely; the game reads the byte once per
frame, so toggling is safe mid-session in offline mode.