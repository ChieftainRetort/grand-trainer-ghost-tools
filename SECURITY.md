# Security Policy

## Scope

`grand-trainer-ghost-tools` is an offline modding toolkit for
*There Are No Ghosts at the Grand Trainer*. It reads and writes local
process memory of a single-player save only.

## Reporting a vulnerability

If you find an issue where the tool:

- writes outside its documented memory region,
- persists beyond process exit,
- or exfiltrates save data,

please open a private security advisory on GitHub. Do not file a public
issue for memory-safety bugs.

## Supported versions

| Version | Supported |
| ------- | --------- |
| 2026.x  | yes       |
| < 2026  | no        |

## Disclaimer

Use at your own risk. The maintainers are not responsible for corrupted
saves or bans incurred by running this against online modes.