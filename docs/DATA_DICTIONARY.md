# Data Dictionary - events_sample.csv

**Grain:** 1 fila = 1 evento etiquetado (acción) en un partido.

## Campos
- `event_id`: Identificador único incremental del evento.
- `session_id`: Identificador de partido/sesión (S001, S002).
- `category`: Categoría (ej: U10).
- `opponent`: Rival.
- `date`: Fecha (YYYY-MM-DD).
- `player_id`: ID del jugador.
- `player_name`: Nombre del jugador.
- `position`: Posición (MID/DEF/FWD/WNG).
- `minute`: Minuto del evento.
- `second`: Segundo del evento.
- `action`: Tipo de acción (PASS/SHOT/RECOVERY/DUEL).
- `result`: Resultado de la acción (Complete, Incomplete, Won, Lost, etc.).
- `zone`: Zona simplificada (Z1..Z9).
- `is_positive`: 1 si el evento se considera positivo según regla simple; 0 si no.
