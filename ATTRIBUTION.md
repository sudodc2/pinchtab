# Attribution

PinchTab's browser automation core (`pinchtab/`) is derived from the
`browser/agent-harness` package of
[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything), used under the
Apache License 2.0 (see LICENSE).

It drives [DOMShell](https://github.com/apireno/DOMShell) (MCP server +
browser extension by apireno) to map Chromium's accessibility tree to a
virtual filesystem.

Modifications in this repository: package renamed to `pinchtab`, imports
rewritten, Brave-first documentation, and standalone packaging.
