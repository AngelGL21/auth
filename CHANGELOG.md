# CHANGELOG

## [v1.2.0] - 2025-06-08
### Agregado
- Implementación de prácticas CMMI-DEV: CAR (análisis de causa raíz), DAR (análisis de decisiones) y CM (gestión de configuración).
- Endpoint de refresh token para renovar sesión sin reautenticación.
- Control de intentos fallidos con bloqueo temporal de usuario.
- Respuestas personalizadas: usuario no existe, contraseña incorrecta, usuario bloqueado.
- Endpoint de recuperación de contraseña con envío de correo.
- Manejo seguro de configuraciones con archivo `.env` y `pydantic`.

## [v1.1.0] - 2025-06-06
### Agregado
- Aplicación técnica de áreas de proceso del modelo CMMI-DEV (MANAGING):
  - EST: estimaciones por tarea y complejidad.
  - PLAN: planificación y gestión de entregables.
  - MC: seguimiento de tareas.
  - RSK: matriz de riesgos.
  - OT: registro de capacidades organizativas.
- Documentación de estimaciones, matriz de tareas y gestión de riesgos.
- Archivos técnicos: `estimaciones.xlsx`, `risk_matrix.md`, `planificacion.md`.

## [v1.0.0] - 2025-06-05
### Inicial
- Configuración de FastAPI como framework base.
- Endpoint básico de login utilizando autenticación con nombre de usuario y contraseña.
- Inicio del archivo `.env` y configuración básica de entorno.

