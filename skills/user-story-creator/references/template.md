# User Story Template

This is the exact structure to use for every user story.

## Format (Copy This)

```
HU - [Nombre descriptivo de la funcionalidad]

Como: Desarrollador
Quiero: [Qué se implementará]
Para: [Valor aportado / beneficio]

Subtareas:

[Prefix]: [Título corto (máx 60 caracteres)]

Descripción: [1-2 líneas explicando qué componente se toca y por qué]

Acciones a Realizar:
- [Acción 1 - concreta y verificable]
- [Acción 2 - concreta y verificable]
- [Acción 3 - concreta y verificable (opcional)]


[Prefix]: [Título corto]

Descripción: [Breve explicación]

Acciones a Realizar:
- [Acción 1]
- [Acción 2]


Criterios de Aceptación:

- [Sistema se comporta de X manera]
- [Se evitaron regresiones en Y funcionalidad]
- [Se validó Z según estándar de calidad]
```

## Structure Explanation

### Historia de Usuario Title

- Always starts with `HU - `
- Descriptive, action-oriented (max 100 characters)
- Example: `HU - Implementar validación centralizada para diagramas con soporte de filtros`

### Cómo/Quiero/Para (User Story Format)

- **Cómo**: Always "Desarrollador"
- **Quiero**: What will be implemented (future tense, imperative)
- **Para**: The value/benefit (why this matters)

### Subtareas

Each subtask has:

1. **Prefix** (from commit label mapping):
   - `Feature:` - New functionality
   - `Fix:` - Bug fix
   - `Refactor:` - Code reorganization
   - `Test:` - New tests or test improvements
   - `Docs:` - Documentation updates
   - `Chore:` - Maintenance, dependencies
   - `Perf:` - Performance improvements
   - `Style:` - Code style (formatting, linting)
   - `Build:` - Build system changes
   - `CI:` - CI/CD pipeline changes
   - `Env:` - Environment/configuration

2. **Título** (short, max 60 chars):
   - Example: `Refactor de Event Handler`
   - Example: `Implementación de validación en categorías`
   - Example: `Sincronización de procesos al actualizar`

3. **Descripción** (1-2 lines):
   - Explains WHAT was modified and WHY
   - Specific component names
   - Example: "Se refactoriza el manejador de eventos para eliminar dependencia circular y mejorar testabilidad del componente TaskEdit."
   - Example: "Se centraliza la validación de procesos usando nuevos esquemas Marshmallow, permitiendo reutilización entre endpoints y garantizando consistencia."

4. **Acciones a Realizar** (2-5 bullets):
   - Atomic, concrete, verifiable actions
   - Future tense (Implementar, Refactorizar, Validar, Eliminar, Actualizar, Agregar)
   - Example: "Eliminar la dependencia circular entre onClick y getProcessData"
   - Example: "Tipar completamente los parámetros BPMN en la tarea"
   - Example: "Crear 3 nuevas pruebas unitarias para validar el nuevo flujo"

### Criterios de Aceptación

2-4 validation criteria:

- System behavior expectations
- Regression prevention
- Quality standards met
- Testing coverage

Examples:

- "El sistema valida tipos de cliente según client_type (application, api)"
- "Se evitaron regresiones en endpoints de categorías que no cambiaron"
- "La cobertura de pruebas es ≥80% para el nuevo código"

## Tense Rule

**ALL text uses future/imperative tense as if planning the work:**

- ✅ "Implementar validación centralizada"
- ✅ "Se refactorizarán los handlers"
- ❌ "Implementé validación" (past tense = wrong)
- ❌ "Se implementó validación" (passive past = wrong)

This makes the story a "work agreement" rather than a historical log.
