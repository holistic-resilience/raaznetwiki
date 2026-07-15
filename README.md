# Raaznet Wiki

Bilingual (English / فارسی) digital-security and privacy wiki for the Raaznet project.

## Layout

- `en/` — English articles (Markdown)
- `fa/` — Persian (Farsi) articles (Markdown)

Both languages share the same category tree (`I. Foundational Concepts`,
`II. Technical Foundations`, …). Each article's filename ends in `_en.md` / `_fa.md`
and carries YAML frontmatter (title, section, tags, …).

## Contributing

Edit or add Markdown files under `en/` and `fa/` and open a pull request against
`main`. Try to keep the English and Persian trees in structural parity.

## Automation

This repository holds **content only**. The search indexing and the upstream
content-sync automation for this wiki live in a **separate, private repository**
maintained by the Holistic Resilience team — intentionally, so that operational
infrastructure is not exposed publicly. Content merged here is picked up
automatically; there is nothing to run from this repo.

If you need something from the automation side (a re-index, an upstream sync, or
access), contact a maintainer.
