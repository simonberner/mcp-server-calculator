# How to build an MCP server - Calculator Example

⚠️ work in progress ⚠️

## About

> "MCP can provide a single, standardized way for AI models to interact with external systems. You write code once and all AI systems can use it." [1]

### Server

> "Servers are the fundamental building block that enriches LLMs with external data and context." [2]

## Usage

TODO

## Dev Setup

As we are using Nix in this project for having a reproducible and isolated development environment, there is no need to install Python or any other dependencies. You will get everything you need within seconds out of the box. Also there is no need to create a virtual environment in Python using `venv` or `poetry`. You just need to be willing to install Nix on your system.

- Install [direnv](https://github.com/direnv/direnv)
- Install [Lix](https://lix.systems/install/)
- Clone this repository
- cd into the directory
- Run `direnv allow`
- Run `pytest`

That's it!
### Tech Stack

- Python3
- Pytest
- MCP SDK
- MCP CLI
- Nix

## Resources

- [1] [MCP server: A step-by-step guide to building from scratch](https://composio.dev/blog/mcp-server-step-by-step-guide-to-building-from-scrtch/)
- [2] [What is Model Context Protocol (MCP)?](https://composio.dev/blog/what-is-model-context-protocol-mcp-explained/)
- [Understanding MCP and how AI engineers can leverage it](https://dev.to/luxdevhq/understanding-mcp-and-how-ai-engineers-can-leverage-it-3e2i`)

## Credits

- Project setup taken from [ical2json](https://github.com/CodersOnlyCH/ical2json)

## About Nix

- [Why using Nix?](https://nixos.org/)
- [Why using Lix?](https://lix.systems/about/#why-lix)
- [Nix packages](https://search.nixos.org/packages)
- [nix-shell](https://nix.dev/manual/nix/2.26/command-ref/nix-shell.html)
