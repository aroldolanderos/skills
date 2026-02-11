# Commit Label to Subtask Prefix Mapping

How commit message prefixes map to subtask prefixes.

## Standard Mapping

| Commit Label | Subtask Prefix | Description                            | Example Subtask                           |
| ------------ | -------------- | -------------------------------------- | ----------------------------------------- |
| `feat:`      | `Feature:`     | New functionality, feature addition    | Feature: Implementar validación de tipos  |
| `fix:`       | `Fix:`         | Bug fix                                | Fix: Corregir respuesta de error          |
| `refactor:`  | `Refactor:`    | Code restructuring, no new feature     | Refactor: Centralizar métodos redundantes |
| `test:`      | `Test:`        | New tests, test improvements           | Test: Agregar pruebas unitarias           |
| `docs:`      | `Docs:`        | Documentation, README, comments        | Docs: Actualizar docstring de métodos     |
| `chore:`     | `Chore:`       | Maintenance, dependencies, cleanup     | Chore: Actualizar dependencias            |
| `perf:`      | `Perf:`        | Performance optimization               | Perf: Optimizar query de procesos         |
| `style:`     | `Style:`       | Code style, formatting, linting        | Style: Ajustar indentación y formato      |
| `build:`     | `Build:`       | Build system changes, Dockerfile       | Build: Actualizar Dockerfile              |
| `ci:`        | `CI:`          | CI/CD pipeline changes, GitHub Actions | CI: Agregar workflow de tests             |
| `env:`       | `Env:`         | Environment config, .env, variables    | Env: Configurar variables de producción   |

## How to Use This

### When Extracting from Session Context

1. **Review recent commits** from the session
2. **Extract prefixes** (feat, fix, refactor, etc.)
3. **Map to subtask prefixes** using table above
4. **Group commits** by module/concern (see grouping-guide.md)
5. **Create one subtask per group** with appropriate prefix

### Example Extraction

**Session commits**:

```
feat: Agrega soporte para filtros en consulta de procesos
fix: Corrige validación de parámetro scope
refactor: Centraliza validaciones en esquemas
test: Implementa pruebas para filtros
```

**Mapped subtasks**:

```
Feature: Implementar soporte para filtros en procesos
Feature: Agregar validación de scope según tipo de cliente
Refactor: Centralizar validaciones en esquemas
Test: Agregar pruebas para nuevos filtros
```

## Handling Multiple Commits per Subtask

If a subtask encompasses multiple commits:

**Example**:

- Commit 1: `feat: Agrega campo name a cliente`
- Commit 2: `refactor: Actualiza schema para name`
- Commit 3: `test: Pruebas para validación de name`

**Single subtask** (since all relate to "name" feature):

```
Feature: Implementar validación del parámetro name en clientes

Descripción: Se agrega soporte para parámetro name con validación
en modelo, esquema y pruebas.

Acciones a Realizar:
- Agregar campo name a modelo de cliente
- Actualizar ClientSchema para validación de name
- Implementar 3 nuevas pruebas unitarias
```

## When Prefix Ambiguity Arises

Use judgment based on **primary purpose**:

- If commit is "refactor + test", use the primary label
  - `refactor: Add tests for new refactored code` → `Refactor:` (primary)
  - `test: Refactor test utilities` → `Test:` (primary)

- If truly mixed, split into separate subtasks:
  ```
  Refactor: Centralizar métodos de validación
  Test: Agregar pruebas para validación centralizada
  ```

## Custom Labels

If your project uses non-standard labels:

- `wip:` → treat as `Feature:` or `Refactor:` based on context
- `hotfix:` → treat as `Fix:`
- `security:` → treat as `Fix:` (security bug fix)
- `deps:` → treat as `Chore:` (dependency update)

Ask if you're uncertain about mapping.
