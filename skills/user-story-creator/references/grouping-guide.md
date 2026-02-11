# Subtask Grouping Heuristics

How to group changes into logical subtasks.

## Quick Decision Tree

```
How many files/components changed?
│
├─ < 12 items
│  └─ Create one subtask per logical grouping
│     (each major change or feature aspect)
│
└─ ≥ 12 items
   └─ Identify natural groupings:
      1. By module (src/modules/diagram/, src/modules/task/, etc.)
      2. By architectural layer (models, schemas, resources)
      3. By feature/concern (validation, API responses, UI)
      4. By type of change (refactoring in one area, new feature in another)
      └─ Aim for 3-8 subtasks (not overly generic, not overly specific)
```

## Grouping Criteria (Priority Order)

### 1. **Module-Based Grouping** (strongest signal)

If changes span multiple modules:

- `src/modules/diagram/` changes → 1 subtask
- `src/modules/task/` changes → 1 subtask
- `src/modules/process/` changes → 1 subtask

**Example**: If you modified `models.py`, `schemas.py`, and `resources.py` in `diagram/`, that's ONE subtask:

```
Feature: Implementar validación centralizada en esquemas de diagramas

Descripción: Se centraliza la validación de diagramas en nuevos esquemas
Marshmallow (DiagramSchema, DiagramUpdateSchema) para reutilización entre
endpoints y consistencia de validaciones.

Acciones a Realizar:
- Crear nuevos esquemas de validación en DiagramSchema
- Actualizar resources.py para usar validación desde esquemas
- Refactorizar models.py para delegar validación a esquemas
```

### 2. **Architectural Layer Grouping** (if single module changes are heavy)

If one module had HEAVY changes across layers:

- Models logic + Schema validation + API responses → Still 1-2 subtasks grouped by concern

**Example**:

- Subtask 1: "Feature: Actualizar estructura de datos para procesos filtrados"
  - Model changes, schema updates
- Subtask 2: "Feature: Implementar endpoint de consulta con parámetros de filtro"
  - Resources/API endpoint changes

### 3. **Feature-Concern Grouping** (for mixed change types)

If changes address different concerns:

- **Validation logic** (models, schemas) → 1 subtask
- **API endpoint updates** (resources) → separate subtask
- **Error handling/response formatting** → separate subtask

**Example**:

```
Feature: Refactorizar validaciones de categoría
- models.py: validation logic
- schemas.py: Marshmallow schemas

Fix: Corregir respuesta de error en endpoint de actualización
- resources.py: error handling

Feature: Agregar filtros a consulta de procesos
- models.py: query logic
- schemas.py: filter parameter validation
- resources.py: new endpoint
```

### 4. **Type of Change Grouping** (when mixing refactors + features)

If session mixed different types:

- All "Feature:" changes → group if related
- All "Refactor:" changes → group if same area
- All "Fix:" changes → one subtask if all in same module

## Examples

### Example 1: Small Change (< 12 items)

**Scenario**: Modified 3 files to add client_type validation

- `src/modules/client/models.py` - Added `validate_client_type()`
- `src/modules/client/schemas.py` - Created `ClientTypeSchema`
- `src/modules/client/resources.py` - Updated POST endpoint

**Grouping**: 1 subtask (changes are cohesive)

```
Feature: Implementar validación de tipo de cliente

Descripción: Se agrega soporte para validación de client_type
(application o api) en modelos, esquemas y recursos de cliente.

Acciones a Realizar:
- Crear validador de client_type en models.py
- Definir ClientTypeSchema en schemas.py
- Actualizar POST /clients para usar nueva validación
```

### Example 2: Large Change (≥ 12 items) — Multi-Module

**Scenario**: Heavy refactoring across 4 modules

- diagram/: 5 files modified
- task/: 4 files modified
- process/: 3 files modified
- schema/: 2 files modified

**Grouping**: 4 subtasks (by module)

```
Feature: Refactorizar validaciones de diagramas con nuevos esquemas
- diagram/models.py, schemas.py, resources.py, store.py, decorators.py

Feature: Sincronizar procesos al actualizar categorías
- task/models.py, schemas.py, resources.py, store.py

Refactor: Centralizar métodos redundantes en ProcessStore
- process/models.py, process/store.py, process/resources.py

Feature: Validar parámetros de procesos en consultas
- schema/validation.py, schema/filters.py
```

### Example 3: Large Change — Single Module, Multiple Concerns

**Scenario**: Heavy changes in `diagram/` module (8 files)

- Logic layer: models.py (3 changes: add method, update validator, add util)
- Validation: schemas.py (3 changes: 2 new schemas, 1 updated)
- API: resources.py (2 changes: 1 new endpoint, 1 updated)

**Grouping**: 2-3 subtasks (by concern or layer)

```
Option A (By Concern):
Feature: Refactorizar lógica de almacenamiento de diagramas
- models.py changes

Feature: Implementar validación centralizada de diagramas
- schemas.py changes

Feature: Exponer nuevos endpoints de consulta y actualización
- resources.py changes

Option B (By Layer - if changes are very tightly coupled):
Feature: Refactorizar modelo de diagramas con nueva validación
- models.py + schemas.py

Feature: Actualizar API de diagramas
- resources.py
```

## When to Merge vs. Split

### MERGE into single subtask when:

- Changes are tightly coupled (e.g., model change requires schema change)
- Same feature or concern across layers
- Files are in the same module
- Total changes are atomic (can't understand one without the other)

### SPLIT into separate subtasks when:

- Changes address different concerns (validation vs. API vs. UI)
- Different modules
- Independent features (could be deployed separately)
- > 8 files total in group (getting unwieldy)

## Golden Rule

**Aim for 3-8 subtasks**. If you have:

- **<3 subtasks**: You may be grouping too aggressively (losing granularity)
- **>8 subtasks**: You may be splitting too finely (too much detail)

Exception: Small fixes (1-2 files) = often 1-2 subtasks. That's fine.
