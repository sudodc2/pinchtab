# PinchTab

Agent-native browser control for **Brave** (and any Chromium browser) — filesystem-first commands that let AI agents inspect and drive web pages through the accessibility tree.

PinchTab is built on the [CLI-Anything](https://github.com/HKUDS/CLI-Anything) browser harness methodology by [HKUDS](https://github.com/HKUDS), adapted by **Hashbrown** ([sudodc2](https://github.com/sudodc2)) for Brave-first use. It wraps [DOMShell](https://github.com/apireno/DOMShell), which maps the browser accessibility tree to a virtual filesystem (`ls`, `cd`, `cat`, `grep`, `click`, `type`).

## Why Brave

Brave is Chromium — it runs the same DOMShell extension as Chrome and exposes the same accessibility tree, so agents get identical control with Brave's privacy protections (ad/tracker blocking, fingerprinting resistance) intact. Your AI agent can browse, fill forms, and extract page structure without your browsing leaving the machine beyond normal traffic.

## Install

```bash
pip install -e .
pinchtab --help
```

Requires Python 3.10+, Node.js/npx, and the DOMShell browser extension.

## Brave setup

1. Install [Brave](https://brave.com) if needed.
2. In Brave, enable `brave://extensions` → **Load unpacked** is not needed — install DOMShell from the Chrome Web Store: <https://chromewebstore.google.com/detail/domshell-%E2%80%94-browser-filesy/okcliheamhmijccjknkkplploacoidnp>
   - If the store blocks it: `brave://settings` → **Extensions** → enable **"Allow extensions from other stores"**, then install from the Chrome Web Store link above.
3. Keep Brave running while using PinchTab.

## Usage

```bash
pinchtab page open https://example.com
pinchtab fs ls /
pinchtab fs grep "Login"
pinchtab act click /main/button[0]
pinchtab act type /main/input[0] "text"
pinchtab --json fs ls /
pinchtab            # interactive REPL
```

Command groups: `page` (open/reload/back/forward/info), `fs` (ls/cd/cat/grep/pwd), `act` (click/type), `session` (status/daemon).

## For agents

The REPL and `--json` output are designed for agent consumption: stable paths into the accessibility tree, machine-readable results, daemon mode for persistent sessions. See `pinchtab/skills/SKILL.md` for the agent-facing command reference.

## Credits

- Harness methodology and browser automation core: [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) (Apache-2.0)
- Accessibility-tree bridge: [apireno/DOMShell](https://github.com/apireno/DOMShell)
- PinchTab branding, Brave adaptation, and packaging: **Hashbrown** — [discord.gg/JUEc8rBVvC](https://discord.gg/JUEc8rBVvC)

## License

Apache-2.0 — see [LICENSE](LICENSE). Upstream attribution in [ATTRIBUTION.md](ATTRIBUTION.md).
