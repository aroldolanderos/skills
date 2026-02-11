# Skills

Custom [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
skills for structured commits, changelog generation, and user story
creation. Built following the
[Agent Skills Open Standard](https://agentskills.io).

## Installation

```bash
npx skills add aroldolanderos/skills
```

Or install individual skills:

```bash
npx skills add aroldolanderos/skills/get-commits
npx skills add aroldolanderos/skills/make-commits
npx skills add aroldolanderos/skills/user-story-creator
```

## Skills

| Skill | Description |
|-------|-------------|
| **get-commits** | Parse git commit history into structured JSON with [Why]/[What]/[Impact] tags. For changelogs, PR summaries, and change analysis. |
| **make-commits** | Analyze git changes and generate semantic commits iteratively. Groups related files, confirms with user, executes git add + commit. |
| **user-story-creator** | Synthesize completed work into structured User Stories (HU) with subtask grouping, acceptance criteria, and technical narrative. |

## Commit Message Format

Two of these skills revolve around a structured commit format:

```
feat(scope): Brief description

[Why]: Motivation for this change
[What]: Technical implementation details
[Impact]: Business impact or breaking changes
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`,
`test`, `chore`, `env`

## Contributing

Contributions are welcome. Please open an issue or pull request.

## License

MIT - see each skill's `LICENSE.txt` for details.
