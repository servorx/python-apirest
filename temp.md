# 🧰 Entidades y Relación

## 1. Usuarios (User)
**Atributos:**
- `id`
- `nombre`
- `email`
- `contraseña_hash`
- `rol` (`user` / `admin`)

**Endpoints clave:**
- `POST /auth/register`
- `POST /auth/login`
- `GET /users/me`
- `GET /users/` (admin)
- `DELETE /users/{id}` (admin)

---

## 2. Salas (Room)
**Atributos:**
- `id`
- `nombre`
- `sede` (Bogotá, Medellín…)
- `capacidad`
- `recursos` (lista: pizarra, proyector…)

**Endpoints clave:**
- `GET /rooms`
- `POST /rooms` (admin)
- `PUT /rooms/{id}` (admin)
- `DELETE /rooms/{id}` (admin)

---

## 3. Reservas (Reservation)
**Atributos:**
- `id`
- `usuario_id`
- `sala_id`
- `fecha`
- `hora_inicio`
- `hora_fin`
- `estado` (`pendiente`, `confirmada`, `cancelada`)

**Endpoints clave:**
- `POST /reservations`
- `GET /reservations/me`
- `GET /reservations/room/{room_id}`
- `GET /reservations/date/{yyyy-mm-dd}`
- `DELETE /reservations/{id}` (cancelar)

---

# 🔢 Validaciones Clave
- Validar que no haya cruce de horarios para la misma sala.  
- Validar que las reservas sean de bloques de **1 hora exactos**.  
- Limitar acciones administrativas solo a usuarios con **rol admin**.  

---

# 📊 Reportes opcionales (Solo admin)
- “¿Qué sala se ha reservado más veces?”  
- “¿Cuántas horas ha reservado un usuario este mes?”  

---

# ✨ Características extra (opcional)
- Lógica de penalización si se cancelan muchas reservas.  

---

# 🏋️ Estructura de Rutas (Resumen)

## Autenticación
- `POST /auth/register`  
- `POST /auth/login`  

## Usuarios
- `GET /users/me`  
- `GET /users/` — Solo admin  
- `DELETE /users/{id}` — Solo admin  

## Salas
- `GET /rooms`  
- `POST /rooms` — Solo admin  
- `PUT /rooms/{id}` — Solo admin  
- `DELETE /rooms/{id}` — Solo admin  

## Reservas
- `POST /reservations`  
- `GET /reservations/me`  
- `GET /reservations/room/{room_id}`  
- `GET /reservations/date/{yyyy-mm-dd}`  
- `DELETE /reservations/{id}` — cancelar  
