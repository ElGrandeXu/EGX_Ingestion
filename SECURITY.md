# Security Policy

This workspace must never contain committed secrets.

## Do not commit

- GitHub, OpenAI or other API tokens.
- API keys, passwords, private keys or certificates.
- `.env` files containing local configuration or credentials.
- Entire cloned external repositories.
- Installed dependencies such as `node_modules/`, `venv/` or `.venv/`.
- Generated build outputs, caches or bulky experiment runs.

## Configuration guidance

If environment variables are needed later, document their names in `.env.example` without real values. Keep real values in a local `.env` file, which is ignored by Git.

Before publishing or pushing, inspect the staged files and run a sensitive-string search for token, secret, key and password patterns.
