## TAREA: Análisis de Entrevista y Calificación de Riesgo de Attrition

Realiza un análisis detallado de la transcripción de la entrevista proporcionada en formato VTT. Debes evaluar al candidato según los criterios y pesos especificados, y generar una única línea en formato CSV como salida.

### Instrucciones Generales
1.  **Análisis Literal:** Basa tu análisis únicamente en lo que se dice explícitamente en la transcripción.
2.  **No Inferir:** No hagas suposiciones que no estén respaldadas por una cita directa del texto.
3.  **Manejo de Información Faltante:** Si la información para un criterio no se menciona, asígnalo con una puntuación de 0 y anótalo en el campo Justificacion.
4.  **Puntuación Binaria:** Si la evidencia es explícita y suficiente, asigna el peso completo. Si no, asigna 0.

---
### **REGLAS CRÍTICAS DE FORMATO (OBLIGATORIAS)**

1.  **ESTRUCTURA INFLEXIBLE:** La salida DEBE ser una **única línea de texto en formato CSV** con **EXACTAMENTE 18 campos** separados por comas. Ni más, ni menos.
2.  **SEPARADOR EXCLUSIVO:** La **coma (,)** se usa **EXCLUSIVAMENTE** como separador de campos.
3.  **PROHIBICIÓN DE COMAS INTERNAS:** Dentro del campo de texto (`Justificacion`), **NUNCA uses comas** para crear listas o separar ideas. En su lugar, utiliza **guiones (-), puntos (•) o saltos de línea literales (\n)**.
4.  **EJEMPLO COMO VERDAD ABSOLUTA:** El formato de la `SALIDA (CSV esperado)` en el ejemplo es la **única referencia válida**. No te desvíes de él bajo ninguna circunstancia. Asegúrate de que los campos de texto largos estén encapsulados en comillas dobles (" ").

---

### Tabla de Criterios y Pesos
| Categoría | ID | Subcriterio | Peso |
| :--- | :- | :--- | :--- |
| **A. Attrition (40%)** | A1 | Estudios e Intenciones Futuras | 12 |
| | A2 | Hobbies y otras actividades | 12 |
| | A3 | Foráneo o Local | 5.6 |
| | A4 | Entorno de Vida | 5.6 |
| | A5 | Ubicación y Metodología de Trabajo | 4.8 |
| **B. Salary/Comp (20%)** | B1 | Current salary expectation | 10 |
| | B2 | Solvo Payment model | 10 |
| **C. Position (20%)** | C1 | Profile according to the position | 6 |
| | C2 | Test the workload | 8 |
| | C3 | Leadership | 6 |
| **D. Minimum Req (20%)**| D1 | Language Requirement | 4 |
| | D2 | Schedule Requirement | 4 |
| | D3 | Location Requirement | 4 |
| | D4 | Profile Requirement | 4 |
| | D5 | Benefits and Compensation | 4 |

# Manual de Criterios de Evaluación de Candidatos

**Cada criterio tiene:**
**Objetivo -- Definiciones operativas -- Evidencia válida -- Regla de puntuación -- Reglas de no inferencia -- Preguntas de sondeo -- Ejemplos -- Campos CSV -- Errores comunes.**

---

## A. ATTRITION (40%)

### A1 --- Estudios e Intenciones Futuras (12)

#### Objetivo
Evaluar riesgos de continuidad asociados a estudios, interrupciones académicas, prácticas obligatorias u objetivos futuros del candidato (como migrar, emprender o estudios a corto plazo) que interfieran con la permanencia en el cargo.

#### Definiciones operativas
- **Estudios Activos:** Actualmente matriculado en universidad, técnica o curso formal.
- **Estudios Relacionados:** Carrera alineada al cargo o área.
- **Estudios No Relacionados:** Carreras desviadas del cargo y que proyectan cambio próximo.
- **Prácticas Próximas:** Obligatorias dentro de 6-12 meses que afectarán la vacante.
- **Intención de migrar:** Tiene planes claros de mudarse de ciudad o país en corto (menos de tres meses) y/o mediano (entre 6 a 12 meses) plazo.
- **Continuidad:** No se proyectan interrupciones académicas, viajes ni otros planes que interfieran.

#### Evidencia válida
- Declaraciones explícitas de estar estudiando o no.
- Detalle de modalidad (virtual/presencial), horarios, semestre y proximidad de prácticas.
- Comentarios textuales sobre planes a futuro: migrar, emprender, ascender en el corto plazo.

#### Regla de puntuación (binaria, 12 o 0)
- **12 puntos:** Estudios formales (universitarios) alineados al cargo o estudios de cursos cortos en plataformas online (Udemy, Coderhouse, cursos en YouTube, etc.), modalidad no interferente (virtual/nocturna/diurna/asincrónica), sin prácticas próximas, sin viajes/migraciones ancladas. Planes de continuidad estables y sin descoordinación de su horario de estudiante con el de la posición de la vacante a la que está aplicando.
- **0 puntos:** Evidencia clara de interferencia: prácticas próximas, viajes definidos de mediana (entre 6 a 12 meses) o larga duración (mayor a un año) o muy próximos a las fechas de ingreso para la posición. Si se menciona que se comunicará al cliente o supervisor de operaciones, dejar la cita textual con la marcación en tiempo. Si no se declara nada → 0.

#### Reglas de no inferencia
- No asumir interferencia solo porque estudia presencial si no se mencionan choques de horario.
- No asumir migración si solo expresa interés general en "viajar algún día".
- Si no hay evidencia suficiente → puntuar 0 y registrar ausencia.

#### Preguntas de sondeo
- ¿Dónde estudias actualmente y en qué modalidad?
- ¿Tus horarios de la universidad o de estudio son diurnos o nocturnos?
- ¿Tienes prácticas profesionales próximas? ¿Cuándo?
- ¿Tienes planes de migrar o de emprender en los próximos años (mayor a un año)?
- ¿Tienes planes de continuar estudiando (especialización, maestría, doctorado)?
- ¿Realizas cursos de corta duración en plataformas online?

#### Ejemplos aplicados
- Cursa en modalidad virtual, menciona "mis clases son en la noche y no interfieren". Decisión: **12** → Justificación: estabilidad, sin conflicto.
- Está en últimos semestres o esperando grado, prácticas inician en 6 meses y son presenciales. Decisión: **12** → Justificación: existe interrupción pero cumple el plazo mínimo de permanencia en la empresa de 3 meses.
- Está en últimos semestres, prácticas inician en 3 meses y son presenciales. Decisión: **0** → Justificación: interrupción inevitable y no cumplimiento del plazo mínimo de permanencia en la empresa de 3 meses.
- No estudia, no menciona planes ni continuidad clara de estudio. Decisión: **0** → Justificación: ausencia de evidencia.
- No estudia, y manifiesta que no tiene planes de estudio y su prioridad es trabajar/crecer en una empresa/ganar más experiencia. Decisión: **12** → Justificación: No presenta restricciones de horario como estudiante y tiene determinación de crecer como empleado.
- No estudia, y manifiesta que no tiene planes de estudio, pero sí de armar un emprendimiento (empresa de comida, proyecto musical, escritor, crear un videojuego) y quiere trabajar para poder ahorrar y crecer esa meta. Decisión: **12** → Justificación: si y solo si la proyección es mayor a seis meses o está en etapa temprana de estructuración del proyecto.
- No estudia, y manifiesta que no tiene planes de estudio, pero sí de armar un emprendimiento (empresa de comida, proyecto musical, escritor, crear un videojuego) y quiere trabajar para poder cumplir ese objetivo. Decisión: **0** → Justificación: si y solo si la proyección es menor a seis meses para el cumplimiento de ese objetivo.
- Egresado con carrera alineada, sin planes inmediatos de migrar, dice "quiero crecer aquí mínimo dos años". Decisión: **12**.
- No se menciona nada sobre sus estudios o planes futuros en cuanto a su educación. Decisión: **0**. Justificación: No se indagó nada sobre este subcriterio en la entrevista.

#### Campos CSV afectados
- `A1_Studies`: 12 o 0.
- `Justificacion`: Combinación de la evidencia textual (citas) y un breve análisis del riesgo. Ejemplo: "Evidencia: [cita textual sin comas sobre modalidad, prácticas, etc.] - Análisis: [Riesgo alto/bajo por motivo X]".

#### Errores comunes a evitar
- Asignar 12 sin confirmación explícita de no interferencia.
- Inferir riesgo de migración solo porque viaja en vacaciones.
- Marcar 0 automáticamente por ser presencial sin validar horarios o restricciones.

---

### A2 --- Hobbies y Otras Actividades (12)

#### Objetivo
Determinar si los pasatiempos, deportes, videojuegos o actividades productivas del candidato generan riesgo de interferencia con la jornada y continuidad en la vacante.

#### Definiciones operativas
- **Recreativo genérico:** Pasear, salir en familia, ver TV, escuchar música, leer por interés, cine, disfrutar el tiempo con sus hijos.
- **Deportivo/hobby activo:** Fútbol, gimnasio, running, artes marciales, videojuegos.
- **Actividad productiva:** Emprendimiento, tutorías, clases, freelancing, voluntariado con horario fijo, negocio propio.
- **Interferencia:** Requiere tiempo dentro de la jornada laboral, implica viajes frecuentes, competencias, o constituye una segunda fuente principal de ingresos y al mismo tiempo existe interferencia con la jornada laboral.

#### Evidencia válida
- Declaraciones textuales sobre qué hace en tiempo libre.
- Confirmaciones explícitas de que no interfiere con la jornada.
- Menciones de ingresos actuales por la actividad, frecuencia, horarios.

#### Regla de puntuación (binaria)
- **12 puntos:** Solo actividades recreativas genéricas o hobbies/actividades productivas fuera del horario, y evidencia de no interferencia. Ejemplo: "Doy clases ocasionalmente en mis tiempos libres" y "no interfiere con la jornada".
- **0 puntos:** Evidencia de que compiten con la jornada, o falta total de información para decidir. Ejemplos: competencias con viajes, horarios laborales compartidos, ingresos prioritarios, o el candidato no menciona nada sobre hobbies o actividades y no hay confirmación de no interferencia.

#### Reglas de no inferencia
- No asumir que un hobby competitivo interfiere sin mención de frecuencia, horarios o viajes.
- No asumir que un emprendimiento genera ingresos si no se declara.
- Si no hay datos, puntuar 0 y registrar la ausencia.

#### Preguntas de sondeo (si aplica)
- ¿Con qué frecuencia realizas esta actividad y en qué horarios?
- ¿Genera ingresos actualmente, cuánto, y con qué regularidad?
- ¿Este horario interfiere con el horario de la posicion?

#### Ejemplos aplicados
- Lectura, gimnasio ocasional, pasar tiempo con familia. Decisión: **12**. Justificación: recreativo sin interferencia.
- Clases de inglés pagadas cada tarde de lunes a viernes. Decisión: **0**. Justificación: actividad productiva en horarios laborales, interferencia probable.
- Clases de inglés pagadas cada día a las 9pm de lunes a viernes y no tengo ningún problema, priorizo el trabajo y no se me cruzan los horarios. Decisión: **12**. Justificación: actividad productiva fuera del horario laboral.
- Tutorías esporádicas fines de semana, confirma que no interfieren. Decisión: **12**. Justificación: fuera de jornada y sin conflicto.
- Practico arquería y cada fin de semana viajo fuera de la ciudad para participar en algunos torneos, y estoy postulado para participar y representar al país en las olimpiadas -- aunque confirma que no interfieren. Decisión: **0**. Justificación: actividad semiprofesional o profesional en el deporte por lo cual, aunque manifieste que está dispuesto, prevalece su sueño de deportista sobre el trabajo - interferencia probable.
- No se menciona ningún hobbie, pasatiempo. Decisión: **0**. Justificación: No se evidencia abordar este tema en la entrevista.

#### Campos CSV afectados
- `A2_Hobbies`: 12 o 0.
- `Justificacion`: Combinación de la evidencia textual (citas) y un breve análisis del riesgo. Ejemplo: "Evidencia: [cita textual sin comas sobre la actividad y su no interferencia] - Análisis: [Riesgo bajo/alto por motivo X]".

#### Errores comunes a evitar
- Asignar 12 sin confirmación de no interferencia cuando la actividad parece productiva.
- Usar inferencias sobre ingresos o frecuencia sin evidencia textual.

---

### A3 --- Foráneo o Local (5.6)

#### Objetivo
Evaluar riesgos de continuidad relacionados con la procedencia geográfica y la facilidad/dificultad para permanecer en la ciudad de la vacante.

#### Definiciones operativas
- **Local:** Vive en la misma ciudad/sede del trabajo.
- **Foráneo estable:** Mudado por estudios o trabajo, con arraigo, sin planes de retorno.
- **Foráneo en riesgo:** Planea regresar a su lugar de origen o mudarse pronto.

#### Evidencia válida
- Declaración de domicilio actual y planes de mudanza permanentes/temporales.
- Antecedentes de inestabilidad residencial o dificultades de traslado.

#### Regla de puntuación
- **5.6 puntos:** Local o foráneo estable, sin planes de migración en corto plazo.
- **0 puntos:** Plan probable o explícito de mudanza próxima, retorno a ciudad de origen o dificultad de permanencia.

#### No inferencia
- No asumir riesgo por ser foráneo si no declara intención de mudarse.
- Si no hay datos → marcar 5.6.

#### Preguntas de sondeo
- ¿Hace cuánto vives aquí?
- ¿Tienes planes de cambiar de ciudad en los próximos 1-2 años?
- ¿Tienes familia o red de apoyo en esta ciudad?

#### Ejemplos
- Local, menciona "soy de aquí y no planeo mudarme". → **5.6**.
- Foráneo "solo vine por estudios, me regreso en vacaciones cuando termine". → **0**.
- Trabajador desplazado reciente, dice "mi plan es quedarme indefinidamente". → **5.6**.
- Si no hay datos → **5.6**.

#### CSV
- `A3_ForeignLocal`: 5.6 / 0.
- `Justificacion`: Combinación de la evidencia textual (citas) y un breve análisis del riesgo. Ejemplo: "Evidencia: [cita literal sobre domicilio/planes] - Análisis: [Riesgo alto/bajo por motivo X]".

---

### A4 --- Entorno de Vida (5.6)

#### Objetivo
Identificar si su contexto familiar/social impacta su disponibilidad, estabilidad o rendimiento (ej: hijos sin apoyo, responsabilidades domésticas).

#### Definiciones
- **Estable:** Cuenta con red de apoyo, responsabilidades equilibradas.
- **Riesgo:** Hijos pequeños sin apoyo, cuidadores sin reemplazo, carga excesiva.

#### Evidencia válida
- Declaraciones: "mis hijos se quedan con...", "yo asumo todo el cuidado".
- Comentarios explícitos sobre equilibrio o falta de apoyo.

#### Regla de puntuación
- **5.6 puntos:** Estructura y apoyo claros, sin riesgo de interferencia.
- **0 puntos:** Expone falta de apoyo, responsabilidades principales incompatibles con jornada.

#### No inferencia
- Tener hijos ≠ interferencia, salvo evidencia que lo confirme.
- Tener adultos mayores a su cargo ≠ interferencia, salvo evidencia que lo confirme.
- Tener mascotas ≠ interferencia, salvo evidencia que lo confirme.
- Sin datos → **0.**

#### Ejemplos
- "Mis hijos están en colegio / los cuida un familiar / mi madre / me apoya mi esposa, no afecta trabajo". → **5.6**.
- "Mis mascotas (gatos, perros) se quedan en la casa y ya están acostumbrados, no afecta trabajo". → **5.6**.
- "Mi Madre y mi hermano todos trabajamos en la casa y ninguno depende de cuidados personales de cada uno, nos cuidamos como familia que somos y aportamos, no afecta trabajo". → **5.6**.
- "Vivo con mis padres y ellos todavía me mantienen por lo cual dependo de ellos, no afecta trabajo". → **5.6**.
- "Vivo con mis padres y ellos en las noches cuidan al niño mientras yo trabajaría en este horario nocturno que me ofrecen, no afecta trabajo". → **5.6**.
- "Soy única cuidadora y no tengo con quién dejar a mis hijos". → **0**.
- No hay datos en la entrevista. → **0**.

---

### A5 --- Ubicación y Metodología de Trabajo (4.8)

#### Objetivo
Evaluar riesgos logísticos y de adaptación a modalidad (presencial/híbrido/remoto).

#### Definiciones
- **Acceso viable:** Transporte confiable, tiempos aceptables <1h.
- **Acceso de riesgo:** Transporte limitado, distante, o demanda trabajo remoto sin ser opción.

#### Evidencia válida
- Declaraciones sobre distancias, rutas, experiencia previa con transporte.
- Comentarios sobre preferencia de modalidad.

#### Regla
- **4.8 puntos:** Declara comodidad con modalidad requerida y acceso viable.
- **0 puntos:** Señala dificultades de transporte o expectativas contrarias a modalidad.

#### Ejemplos
- Vive cerca, "me acomoda presencial". → **4.8**.
- Vivo bien, "me gusta la presencialidad y me queda en bus como a 30 minutos el site o la oficina que me mencionas". → **4.8**.
- Vive lejos o fuera de la ciudad + quejas previas por transporte. → **0**.
- Vive lejos o fuera de la ciudad, pero al ser la modalidad hibrida o remota de esta posición me queda muy bien. → **4.8**.
- Resido no muy cerca, y no tendría ningún problema con la presencialidad y la llegada al site llegaría en mi transporte privado en 45 minutos al site o la oficina que me comentas". → **4.8**.
- Yo vivo actualmente en otra ciudad, pero en 15 días me mudo a la que me mencionas en la posición y me encanta. → **0**. Debido a que no se conoce la cercanía de su lugar en el lugar que va a mudarse y a cuánto tiempo estaría del site o la oficina y qué medio de transporte utilizaría.
- Yo vivo actualmente en otra ciudad, pero en 15 días me mudo a la que me mencionas en la posición y me encanta, yo me quedaría en X barrio y moviéndome en transporte publico mientras me adapto llegaría al site en una hora y me queda muy bien. → **4.8**. Debido a que se indagó y/o comunicó la distancia, duración y medio de transporte para desplazarme al site.
- Pide remoto obligatorio cuando puesto es presencial. → **0**.

---

## B. SALARY / COMP (20%)

### B1 --- Current Salary Expectation (10)

#### Objetivo
Determinar si sus expectativas de salario son viables y sostenibles para el puesto.

#### Evidencia
- Declaraciones textuales sobre monto o rango esperado.

#### Regla
- **10 puntos:** Expectativa alineada a oferta (igual o ligeramente flexible).
- **0 puntos:** Expectativa mayor no negociable o no responde.

#### Ejemplo
- "Espero $X, pero estoy dispuesto a escuchar la oferta si se ajusta a rango". → **10**.
- "Espero $X, pero estoy dispuesto a negociar debido a que como te comenté quiero algo más estable". → **10**.
- "Mi rango esta entre $X y $Y y quiero algo en ese rango por mi experiencia". → **10**.
- "Solo acepto $Y o algo mucho mayor a la oferta". → **0**.

---

### B2 --- Solvo Payment Model (10)

#### Objetivo
Evaluar si se acepta la remuneración y la modalidad de pago de la empresa (mensual/quincenal, vía específica).

#### Evidencia
- Respuesta clara: aceptación o resistencia.

#### Regla
- **10 puntos:** Acepta explícitamente la remuneración y modelo de pago.
- **0 puntos:** Rechaza o pone condiciones diferentes y fuera de contexto.

#### Ejemplo
- "Sí, acepto la remuneración y la modalidad de pago quincenal que me han ofrecido. Me parece una propuesta muy atractiva." → **10**. El candidato no solo acepta la propuesta, sino que también la califica como "muy atractiva", lo que refuerza su conformidad.
- "La verdad, el salario me parece un poco bajo para la experiencia que tengo. ¿Habría la posibilidad de negociar un monto más alto? Además, preferiría que el pago fuera mensual en lugar de quincenal, ¿sería posible?" → **0**. Esta respuesta no muestra una aceptación clara, por lo que, de acuerdo con la regla, recibiría 0 puntos.
- "Estoy de acuerdo con la remuneración total y entiendo que la modalidad de 65% prestacional y 35% como pago extralegal. Para mí, esta estructura está bien." → **10**. El candidato demuestra que comprende la complejidad del modelo de pago propuesto y lo acepta sin condiciones.
- "He revisado la propuesta de sueldo. Acepto el monto total, pero no me siento cómodo con la división 65/35. Preferiría que el 100% de mi salario fuera prestacional para asegurar mis beneficios a futuro." → **0**. El candidato está rechazando el modelo de pago específico que la empresa ofrece.
- "Entendido. Acepto la remuneración y estoy de acuerdo en recibir el pago a través de Payoneer. Ya tengo una cuenta y me parece un método muy práctico." → **10**.
- "El salario me parece bien, pero nunca he usado Payoneer y no estoy seguro de cómo funciona o si tendría que pagar comisiones. ¿Podríamos hacerlo a través de una transferencia bancaria normal a mi cuenta ya que no me gusta eso que no conozco y no quiero utilizarlo?" → **0**.
- "El salario me parece bien, pero nunca he usado Payoneer y no estoy seguro de cómo funciona, pero si me explican sigamos adelante." → **10**.

---

## C. POSITION (20%)

### C1 --- Profile According to Position (6)

#### Objetivo
Determinar ajuste del candidato en competencias y experiencia al cargo.

#### Evidencia
- Experiencia previa, formación alineada, conocimientos directos del área.

#### Regla
- **6 puntos:** Claramente alineado a rol/cultura.
- **0 puntos:** Desalineación evidente.

#### Ejemplo
- "Durante mis 8 años de experiencia, he liderado equipos en el desarrollo de software y la implementación de sistemas CRM para empresas del sector financiero, utilizando metodologías ágiles como Scrum y Kanban. Mi maestría en Gerencia de Proyectos me ha permitido consolidar mis conocimientos en la planificación y ejecución estratégica." → **6**.
- "Tengo 10 años de experiencia como vendedor de productos de construcción. Mi principal habilidad es negociar con clientes y mi objetivo ahora es explorar un cambio de carrera. No tengo experiencia previa en marketing, pero soy una persona muy proactiva y aprendo rápido." → **0**.
- "Soy programador desde hace 5 años, especializado en desarrollo backend y bases de datos para plataformas de e-commerce. A nivel personal, soy un apasionado de los videojuegos, he participado en varias game jams y mi proyecto de tesis fue un motor gráfico en Unity. Considero que mi lógica de programación se aplica perfectamente a este campo." → **6**.
- "En mi puesto anterior, no solo me encargaba de la prospección y cierre de ventas a empresas, superando mis cuotas en un 15% en el último año, sino que también era el principal punto de contacto post-venta. Mi rol incluía gestionar las cuentas clave para asegurar su satisfacción continua, resolver cualquier incidencia con el producto y buscar oportunidades de *upselling* y *cross-selling* basadas en sus necesidades." → **6**.

---

### C2 --- Test the Workload (8)
#### Objetivo
Evaluar si el candidato demuestra la capacidad para manejar el tipo de carga y presión específicos del rol.

#### Lógica de Evaluación en Dos Pasos:
**Paso 1: Clasificación del Rol.** Primero, determina si el rol al que aplica el candidato es "Non-Core" o "Core" basándote en la información de la entrevista o el título del puesto.

- **Non-Core Accounts (Roles de Interacción con Cliente):** Customer Service, Ventas, Intake Specialists. Se centran en KPIs de interacción, volumen y satisfacción.
- **Core Accounts (Roles de Soporte y Desarrollo):** Desarrolladores, Staff, Backoffice, Contabilidad, Legal. Se centran en precisión, eficiencia y cumplimiento de plazos.

**Paso 2: Aplicación de la Regla.** Una vez clasificado el rol, aplica la regla correspondiente de forma estricta.

#### Regla de puntuación (8 o 0)
- **Para Non-Core (8 puntos):** El candidato debe validar la presión del entorno y proporcionar un ejemplo CONCRETO de manejo de alto volumen, un cliente difícil, o mencionar KPIs (AHT, CSAT, etc.). La evidencia debe demostrar resiliencia y proactividad.
- **Para Core (8 puntos):** El candidato debe validar la exigencia del rol y proporcionar un ejemplo CONCRETO de manejo de plazos ajustados, aseguramiento de la precisión (auditorías, revisiones), o aplicación de metodologías (Scrum, etc.).
- **Se asignan 0 puntos si:** La respuesta es vaga ("sí, puedo trabajar bajo presión"), evasiva, rechaza la presión, o no proporciona un ejemplo específico y relevante para el tipo de rol (Core/Non-Core). La ausencia de información también resulta en 0.

> **Ejemplo:**
- **Non-Core Account:** "En mi rol anterior de CSR, era responsable de gestionar las solicitudes de más de 100 clientes al día, con un KPI de satisfacción del 95%. Lo que me ayudó a lidiar con el alto volumen fue crear un sistema de etiquetas en mi bandeja de entrada para priorizar tickets urgentes..." → **8**.
- **Non-Core Account:** "La verdad, no estoy acostumbrado a trabajar con presión. Si un cliente se enojaba, simplemente transfería la llamada a mi supervisor..." → **0**.
- **Core Account:** "En mi último proyecto como desarrollador, trabajamos bajo la metodología Scrum, con sprints de dos semanas. A menudo enfrentábamos plazos ajustados, pero para asegurar la entrega a tiempo, implementamos revisiones diarias de código..." → **8**.
- **Core Account:** "En mi rol de analista de datos, la atención al detalle era fundamental... Recuerdo haber descubierto una discrepancia de $10,000 en un reporte. En lugar de pasarlo por alto, detuve mi trabajo y me dediqué a auditar las fuentes de datos..." → **8**.
- **Core Account:** "En mi último trabajo teníamos plazos, pero la verdad es que si no se cumplían, no pasaba nada... no me gusta trabajar bajo presión." → **0**.
- **Respuesta Evasiva:** "No recuerdo muy bien esa parte de mi trabajo anterior... Prefiero no hablar sobre mis KPI." → **0**.
- **Sin información:** Si no hay información en la entrevista porque no se comentó por omisión del reclutador → **0**.

---

### C3 --- Leadership (6)
#### Objetivo
(SOLO PARA CUENTAS CORE) Evaluar la adaptabilidad del candidato a una estructura de reporte matricial o dual (ej: líder de proyecto y líder funcional) y su potencial para gestionar prioridades complejas que se derivan de ella.

#### Regla de Aplicabilidad (Paso Previo)
Antes de evaluar, determina si el rol del candidato es Core o Non-Core (usando las mismas definiciones del criterio C2).
- Si el rol es Non-Core: Este criterio NO APLICA. Asigna automáticamente 6 puntos y en la justificación escribe: "Evidencia: N/A - Regla: Criterio no aplicable para rol Non-Core." No se requiere más análisis.
- Si el rol es Core: Procede con la evaluación detallada según la siguiente regla.

#### Regla de Puntuación (Solo para Cuentas Core)
La puntuación es binaria (6 o 0) y se basa en la reacción y comprensión del candidato ANTE LA EXPLICACIÓN de la estructura de liderazgo dual por parte del entrevistador.
- 6 puntos: El candidato valida y acepta explícitamente la estructura de liderazgo dual. La evidencia sólida incluye:
  - Expresar una actitud favorable y proactiva hacia este modelo de trabajo.
- 0 puntos: Se asignan 0 puntos si ocurre cualquiera de las siguientes situaciones:
  - El candidato rechaza, evade o expresa incomodidad con la estructura dual.
  - Caso Crítico (Falta de datos): Si el entrevistador omitió explicar la estructura de liderazgo, es imposible evaluar al candidato. En este caso, la puntuación es 0 y debe registrarse como un punto a verificar en las recomendaciones y dejar claridad de que el entrevistar no explico el modelo dual de liderazgo.

#### Ejemplos Aplicados (para Cuentas Core)
- Rol: Desarrollador (Core). El candidato dice: "En mi rol anterior, mi líder de proyecto estaba en Alemania y mi supervisor directo en Colombia. Me ayudó a desarrollar autonomía. Me siento muy cómodo con este modelo." → 6 puntos.
- Rol: Analista de Datos (Core). El candidato dice: "Prefiero tener un solo jefe para evitar confusiones. No estoy seguro de que me sentiría cómodo con una estructura así." → 0 puntos.
- Rol: Especialista de Backoffice (Core). El reclutador no menciona el liderazgo dual. → 0 puntos. Justificación: "Ausencia de evidencia. El entrevistador no explicó el modelo de liderazgo". Esto se añade a las recomendaciones de verificación.

#### Ejemplo de No Aplicabilidad
- Rol: Agente de Ventas (Non-Core). No se evalúa el contenido de la respuesta. → 6 puntos. Justificación: "Evidencia: N/A - Regla: Criterio no aplicable para rol Non-Core."

---

## D. MINIMUM REQUIREMENTS (20%)

### D1 --- Language Requirement (4)

#### Objetivo
Validar si el candidato cumple con el nivel de idioma conversacional requerido (ej. inglés B2+).

#### Evidencia
La entrevista (o una parte) se lleva a cabo en el idioma requerido.

#### Regla
- **4 puntos:** El candidato demuestra un dominio conversacional del idioma requerido (inglés B2+ o superior). También se otorga si la posición es exclusivamente en español (ej. para cuentas en España) y el candidato lo menciona para confirmar su entendimiento.
- **0 puntos:** El candidato no cumple con el nivel requerido o no hay evidencia de su habilidad.

### D2 --- Schedule Requirement (4)

#### Objetivo
Validar que el candidato conoce y acepta el horario de trabajo de la posición.

#### Evidencia
- El reclutador menciona el horario.
- El candidato confirma su disponibilidad sin objeciones.

#### Regla
- **4 puntos:** El candidato valida o confirma su disponibilidad para el horario propuesto sin objeciones.
- **0 puntos:** El candidato plantea objeciones o restricciones significativas.

### D3 --- Location Requirement (4)

#### Objetivo
Validar si el candidato acepta el requisito de ubicación (presencial, híbrido o remoto).

#### Evidencia
El reclutador menciona la dirección o modelo y el candidato confirma su capacidad para cumplirlo.

#### Regla de Puntuación
- **4 puntos:** El candidato valida y acepta el requisito de ubicación.
- **0 puntos:** El candidato rechaza el requisito de ubicación o el reclutador no menciona la sede ni informa que se le comunicará después.

### D4 --- Profile Requirement (4)

#### Objetivo
Validar que el candidato cumple con los requisitos mínimos de formación y experiencia.

#### Evidencia
- Confirmación por parte del candidato de que posee la formación académica requerida.
- El candidato demuestra que tiene la experiencia mínima exigida.

#### Regla de Puntuación
- **4 puntos:** El candidato confirma explícitamente que cumple con la formación y experiencia mínimas.
- **0 puntos:** El candidato no cumple con los requisitos mínimos o no hay evidencia.

### D5 --- Benefits and Compensation (4)

#### Objetivo
Validar que el reclutador mencionó los beneficios estándar y que el candidato está conforme.

#### Evidencia
El reclutador menciona los beneficios y el candidato muestra conformidad.

#### Regla de Puntuación
La IA debe aplicar la siguiente lógica:
- **Si la posición es para Colombia:**
    - **4 puntos:** El candidato está conforme con el esquema de beneficios y contrato mencionados.
    - **0 puntos:** El candidato objeta o rechaza los términos.
- **Si la posición es para Filipinas, Kenia, Perú, Argentina, Brasil o México:**
    - **4 puntos:** Este criterio se califica automáticamente con la puntuación máxima, ya que la evaluación no aplica para estas ubicaciones.

---

### GENERACIÓN DEL RESUMEN ANALÍTICO FINAL (PARA EL CAMPO Justificacion)
Al finalizar el análisis de todos los criterios individuales, debes construir un bloque de resumen analítico que se añadirá al final del campo Justificacion. Este bloque DEBE seguir la siguiente estructura y lógica de manera estricta.
1. Evidencia por Criterio (Parte Inicial)
Primero, genera el listado de justificaciones para cada criterio, tal como se definió antes. Ejemplo: A1 Evidencia: [Cita] - Regla: [Regla] - A2 Evidencia: [Cita] - Regla: [Regla] ...
2. Separador Principal
Después de la evidencia, inserta un separador claro: --- RESUMEN ANALÍTICO ---
3. Diagnóstico de Attrition
Inmediatamente después del separador, incluye estas dos líneas:
•¿Probable ATT en <3 meses?: Responde Sí o No. La respuesta es "Sí" si el criterio A1, A3 o cualquier otro revela un riesgo inminente de salida en menos de 3 meses. En todos los demás casos, es "No".
•Nivel de riesgo de attrition: Califica como Bajo, Medio o Alto siguiendo esta lógica:
oAlto: Si cualquier criterio en la categoría A (Attrition) tiene 0 puntos o si el total de la puntuación es inferior a 60.
oMedio: Si hay 1 o 2 criterios con 0 fuera de la categoría A, pero la categoría A está bien puntuada.
oBajo: Si la mayoría de los criterios tienen la puntuación máxima y no hay riesgos críticos identificados.
4. Factores y Recomendaciones
Crea las siguientes subsecciones, usando listas con guiones (-). Para cada punto, incluye la cita textual o la referencia de tiempo (timestamp) del VTT si está disponible.
•Factores de Riesgo:
oLista todos los puntos débiles o preocupaciones identificadas durante el análisis. Esto incluye criterios con puntuación 0 y cualquier otra observación que implique un riesgo, aunque no haya resultado en un 0.
oEjemplo: - Tiempo de desplazamiento de ~1h por trayecto (A5 - Cita: "vivo a una hora en metro").
•Factores de Estabilidad:
oLista los puntos más fuertes y los factores que apoyan la permanencia y el éxito del candidato. Corresponde a criterios con puntuación máxima.
oEjemplo: - Acepta esquema de turnos y modalidad presencial (D2 y D3 - Cita: "sí el horario me queda perfecto").
•Recomendaciones de verificación (pendientes por ausencia de datos):
oEsta lista es CRUCIAL. Incluye únicamente los subcriterios que fueron puntuados con 0 específicamente por "ausencia de evidencia" o "no se indagó".
oIndica qué información falta y qué se debe confirmar.
oEjemplo: - Aclarar estructura de liderazgo operacional (C3 - No abordado en la entrevista).
5. Resumen Final de Riesgos
Como último bloque, añade otro separador y el listado final que solicitaste.
•Separador: --- RESUMEN DE RIESGOS (CRITERIOS CON PUNTUACIÓN CERO) ---
•Riesgos: En una lista con guiones (-), menciona únicamente los nombres de los subcriterios que obtuvieron una calificación de Cero (0), junto a una justificación muy breve.
oEjemplo: - A1 Estudios e Intenciones Futuras: Prácticas presenciales obligatorias inician en 2 meses.
oEjemplo: - B1 Current Salary Expectation: Expectativa 30% por encima de la oferta no negociable.
 
Paso 3: Ejemplo Completo del Campo Justificacion Final
Para que la IA no tenga ninguna duda, aquí tienes un ejemplo completo que puedes poner en tu prompt para mostrar el formato esperado para el campo Justificacion.
"A1 Evidencia: Cursa virtualmente en la noche - Regla: Modalidad no interferente. • A5 Evidencia: Vive a 90 minutos y se queja del transporte público - Regla: Acceso de riesgo. • C3 Evidencia: No se abordó el tema - Regla: Ausencia de evidencia. • D2 Evidencia: Confirma disponibilidad para el horario - Regla: Requisito aceptado. --- RESUMEN ANALÍTICO --- ¿Probable ATT en <3 meses?: No Nivel de riesgo de attrition: Medio Factores de Riesgo: - Tiempo de desplazamiento de 90 minutos y dependencia de transporte público poco fiable (A5 - Cita: 'el bus a veces no pasa y tardo mucho'). - No tiene experiencia previa con liderazgo dual lo que podría ser un reto (C3). Factores de Estabilidad: - Estudios 100% compatibles con el horario laboral (A1 - Cita: 'mis clases son grabadas'). - Aceptación explícita del horario y modelo de pago (D2 y B2). - Fuerte alineación de su experiencia con el perfil del puesto (C1). Recomendaciones de verificación (pendientes por ausencia de datos): - Validar la adaptabilidad a una estructura de liderazgo dual ya que no fue abordado (C3). - Confirmar si posee equipo de cómputo propio si la posición lo requiere (no se preguntó). --- RESUMEN DE RIESGOS (CRITERIOS CON PUNTUACIÓN CERO) --- Riesgos: - A5 Ubicación y Metodología de Trabajo: Distancia y transporte generan un riesgo logístico. - C3 Leadership: Ausencia de datos sobre su adaptabilidad a liderazgo dual."

---

### Estructura del CSV de Salida (18 columnas)
NameInterview,A1_Studies_Intentions,A2_Hobbies,A3_Foreigner_Local,A4_Living_Environment,A5_Work_Location,B1_Salary_Expectation,B2_Payment_Model,C1_Profile_Fit,C2_Workload_Test,C3_Leadership,D1_Language_Req,D2_Schedule_Req,D3_Location_Req,D4_Profile_Req,D5_Benefits_Comp,Total,Justificacion

---

--- FLUJO DE EJECUCION OFICIAL ---
1.  **Setup de Base de Datos**: Ejecutar `database_setup.py` para crear la base de datos `arca_db.sqlite` si no existe.
2.  **Procesamiento Secuencial**: Ejecutar `main.py`.
3.  **Logica del Script `main.py`**:
    - El script itera sobre cada archivo `.vtt` en la carpeta `in/` que no haya sido procesado previamente.
    - Para cada archivo, el modelo (yo) realiza el analisis completo.
    - El script toma el resultado y lo pasa por una funcion de **validacion automatica** que confirma el numero de campos y el formato numerico de las puntuaciones.
    - Si el resultado es valido, se inserta en la tabla `evaluations` de la base de datos.
    - Una vez procesados todos los archivos, el script consulta la base de datos y exporta todos los registros a un unico archivo `consolidated_results.csv`.

--- INSTRUCCIONES DE ANALISIS PARA EL MODELO ---

Eres un experto evaluador de candidatos. Tu tarea es analizar la siguiente transcripción de entrevista en formato VTT y generar una única línea de texto en formato CSV.

La evaluación debe basarse estrictamente en los criterios y pesos definidos en el "Manual de Criterios de Evaluación de Candidatos" que se te ha proporcionado previamente.

REGLAS CRÍTICAS DE FORMATO (OBLIGATORIAS):
- La salida DEBE ser una única línea de texto en formato CSV con EXACTAMENTE 18 campos separados por comas.
- La coma (,) se usa EXCLUSIVAMENTE como separador de campos.
- Dentro del campo de texto (`Justificacion`), NUNCA uses comas. En su lugar, utiliza guiones (-), puntos (•) o saltos de linea literales (\n).
- NO INCLUIR ENCABEZADO CSV: La salida NO DEBE incluir la fila de encabezado (NameInterview, A1_Studies_Intentions, etc.). Solo se espera la línea de datos con los valores de la evaluación.
- ASEGÚRATE DE QUE LA SALIDA SEA UNA SOLA LÍNEA: La respuesta completa debe ser una única línea de texto, sin saltos de línea adicionales al final o entre los campos.

EJEMPLO DE FORMATO PARA Justificacion (SIN COMAS INTERNAS):
"A1 Evidencia: [Cita] (HH:MM:SS) - Regla: [Regla]. - C2 Evidencia: [Cita] (HH:MM:SS) - Regla: [Regla]. --- RESUMEN ANALITICO --- -Probable ATT..."

Ahora está la transcripción de la entrevista en formato VTT:

{VTT_CONTENT_PLACEHOLDER}

Genera la línea CSV de evaluación para este candidato.
