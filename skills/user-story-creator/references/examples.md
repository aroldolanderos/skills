# User Story Examples

Real examples of properly structured user stories from development sessions.

## Example 1: Single-Module, Multi-Feature Change

**Context**: Session where filter validation was added to process queries.

**Recent commits**:

```
feat: Agrega soporte para filtros en consulta de procesos con validación
feat: Agrega validación para el campo `processes` en esquemas de categoría
```

**Result**:

```
HU - Agregar soporte para filtros de procesos con validación centralizada

Como: Desarrollador
Quiero: Tener métodos centralizados para filtrar procesos con validación de parámetros
Para: Reutilizar lógica de filtrado y garantizar consistencia en validaciones entre módulos


Subtareas:

Feature: Implementar soporte para filtros en consulta de procesos

Descripción: Se agrega lógica de filtrado en ProcessStore con parámetros
validados (status, category_id, name) permitiendo consultas más flexibles
y evitando consultas N+1.

Acciones a Realizar:
- Crear método filter_by_status() en ProcessStore
- Crear método filter_by_category() en ProcessStore
- Implementar validación de parámetros en ProcessSchema
- Actualizar GET /processes para aceptar parámetros ?status=X&category_id=Y


Feature: Agregar validación de procesos en categoría

Descripción: Se extiende CategorySchema para validar el campo processes,
permitiendo actualizar categorías con lista de proceso IDs y validando
integridad referencial.

Acciones a Realizar:
- Agregar campo processes (lista de ObjectIds) en CategorySchema
- Implementar validación de IDs de procesos existentes
- Crear método sync_processes_on_category_update() en CategoryStore
- Actualizar PUT /categories para soportar actualización de procesos


Criterios de Aceptación:

- Los filtros funcionan correctamente: GET /processes?status=active retorna solo procesos activos
- Se valida que category_id exista antes de filtrar
- Se evitaron regresiones en endpoints de procesos que no usan filtros
- Las pruebas de integración cubren al menos 3 escenarios de filtrado
```

---

## Example 2: Multi-Module Refactoring

**Context**: Large refactoring session that touched multiple modules.

**Recent commits**:

```
feat: Renueva y centraliza validaciones para diagramas con nuevos esquemas
feat: Sincroniza procesos al actualizar categorías
refactor: Refactoriza `DiagramStore` optimizando métodos redundantes
```

**Result**:

```
HU - Refactorizar validaciones centralizadas y sincronización de procesos

Como: Desarrollador
Quiero: Centralizar validaciones en esquemas y sincronizar cambios de procesos entre módulos
Para: Mejorar mantenibilidad, reutilizar validaciones y garantizar consistencia de datos


Subtareas:

Feature: Renovar validaciones de diagramas con esquemas centralizados

Descripción: Se crean nuevos esquemas Marshmallow (DiagramSchema,
DiagramUpdateSchema) que centralizan toda la lógica de validación de
diagramas, reemplazando validaciones dispersas en resources.py.

Acciones a Realizar:
- Crear DiagramSchema con validaciones de nombre, descripción y procesos
- Crear DiagramUpdateSchema para actualizaciones parciales
- Refactorizar POST /diagrams para usar DiagramSchema
- Refactorizar PUT /diagrams para usar DiagramUpdateSchema
- Eliminar validaciones duplicadas en resources.py


Feature: Sincronizar procesos al actualizar categorías

Descripción: Se implementa sincronización automática de procesos cuando
una categoría es actualizada, manteniendo integridad de relaciones
entre categorías y procesos.

Acciones a Realizar:
- Crear método sync_processes_on_update() en CategoryStore
- Actualizar PUT /categories para llamar sincronización después de update
- Validar que todos los procesos asignados existan antes de sincronizar
- Crear pruebas de integración para sincronización


Refactor: Optimizar métodos redundantes en DiagramStore

Descripción: Se eliminan 3 métodos redundantes (_validate_name(),
_validate_processes(), _build_response()) que eran duplicados con
lógica en schemas.py y resources.py.

Acciones a Realizar:
- Eliminar _validate_name(), _validate_processes() (delegados a schema)
- Unificar _build_response() con formato estándar de API
- Actualizar todos los llamadores de métodos eliminados
- Confirmar que pruebas existentes siguen pasando


Criterios de Aceptación:

- Todos los diagramas se validan correctamente con nuevos esquemas
- La sincronización de procesos ocurre automáticamente en actualizaciones de categorías
- Se eliminaron ≥3 métodos redundantes sin regresiones
- Cobertura de pruebas se mantuvo ≥80%
- Los endpoints /diagrams responden en <200ms (performance no afectado)
```

---

## Example 3: Feature with Mixed Concerns

**Context**: Adding a new CLI command with validation and dependency management.

**Recent commits**:

```
feat: Implementa comando para crear cliente con validaciones
feat: Agrega parámetros parametrizables a cliente
fix: Corrige validación de scope en clientes API
```

**Result**:

```
HU - Implementar comando CLI parametrizable para crear clientes con validaciones

Como: Desarrollador
Quiero: Tener un comando CLI que permita crear clientes (application o api) con validaciones específicas según tipo
Para: Automatizar creación de clientes durante inicialización del sistema sin necesidad de API calls


Subtareas:

Feature: Implementar aceptación de parámetros name y client_type en comando

Descripción: Se crea nuevo comando CLI `create-client` que acepta
parámetros --name (requerido) y --type (application|api) para
flexibilidad en creación de clientes.

Acciones a Realizar:
- Crear comando create_client en src/cli/commands.py
- Agregar argumento --name (requerido, string)
- Agregar argumento --type (opcional, default='application', choices=['application', 'api'])
- Validar que name sea único en base de datos antes de crear


Feature: Implementar validación de scope cuando client_type es api

Descripción: Se agrega validación obligatoria del parámetro scope
cuando client_type='api', asegurando que clientes API tengan permisos
configurados.

Acciones a Realizar:
- Agregar parámetro --scope a comando cuando --type=api
- Validar que scope sea formato válido (ej: "read:process write:diagram")
- Rechazar creación de cliente API sin scope definido
- Crear 2 pruebas para validación de scope


Feature: Implementar aceptación del parámetro institution en formato JSON

Descripción: Se permite pasar metadata de institución en formato JSON
al crear cliente, permitiendo asociar cliente a institución específica.

Acciones a Realizar:
- Agregar parámetro --institution en formato JSON {"name": "...", "id": "..."}
- Validar estructura JSON antes de procesar
- Guardar institution metadata en cliente
- Crear validador de estructura JSON en schemas


Feature: Implementar generación automática de client_id desde name

Descripción: Se genera client_id automáticamente a partir del name
(slugified y único) en lugar de requerir parámetro manual.

Acciones a Realizar:
- Crear función slug_from_name() que convierte "My App" a "my_app"
- Validar uniqueness de generated client_id en base de datos
- Si slug existe, agregar sufijo numérico (my_app_2)
- Actualizar recurso POST /clients para usar misma lógica


Criterios de Aceptación:

- El comando `create-client --name "Test App"` crea cliente sin errores
- El comando rechaza cliente API sin parámetro --scope
- El comando acepta --institution como JSON válido
- El client_id se genera automáticamente y es único
- Cobertura de pruebas para CLI es ≥85%
- Se evitaron regresiones en recurso POST /clients
```

---

## Key Patterns from Examples

1. **Titles are descriptive but concise**: 60 characters max
2. **Descriptions explain WHAT and WHY**: Not just the code change, but the purpose
3. **Acciones are atomic and action-oriented**: Use imperative verbs (Crear, Agregar, Validar, Actualizar, Eliminar)
4. **Future tense throughout**: "Se implementa", "Se agrega", "Se valida" — not past tense
5. **Subtasks are logically grouped**: Related changes in one subtask when possible
6. **Acceptance criteria verify behavior**: Not just "tests pass", but "system behaves X way"
