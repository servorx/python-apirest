
### Archivos SQL del proyecto

En el proyecto, deben crear una carpeta:

app/data/


Dentro deben incluir:

- `docsFlowEstructura.sql` → script de creación de tablas  
- `docsFlowData.sql` → datos de prueba (mock)

---

### Estructura del backend (FastAPI)

Cada entidad tendrá una organización en carpetas siguiendo este patrón:
```code
controllers/
└── users/
  └── UsersController.py

models/
└── users/
  └── UsersModel.py

routes/
└── users/
  └── UsersRoutes.py
```

**Convención:**

- Las carpetas van en **minúscula y en plural**.  
- Los nombres de archivo van en **CamelCase** y deben terminar en el tipo de archivo (por ejemplo: `UsersController`).  
- Esta misma convención se aplica a otras entidades como `documents`, `auth`, `tables`, etc.

---

## 💼 Proyecto: Gestor de Reservas de Salas de Coworking (Python Edition)

### 🎯 Objetivo General

Construir una API REST con Python que permita:

- Registro e inicio de sesión de usuarios con autenticación JWT
- Creación y administración de salas de coworking
- Sistema de reservas con validaciones de horarios
- Generación de reportes simples

---

### 🛠️ Tecnologías Sugeridas

- **Lenguaje:** Python 3.12.6  
- **Framework Backend:** FastAPI  
- **Base de Datos:** PostgreSQL o MySQL  
- **Autenticación:** JWT (p. ej. `fastapi-jwt-auth`)  
- **Documentación:** Swagger (auto-generado por FastAPI)

---

### 🧰 Entidades y Relación

#### 1. Usuarios (User)

- id
- nombre
- email
- contraseña_hash
- rol (user / admin)

**Endpoints clave:**

- `POST /auth/register`
- `POST /auth/login`
- `GET /users/me`
- `GET /users/` (admin)
- `DELETE /users/{id}` (admin)

---

#### 2. Salas (Room)

- id
- nombre
- sede (Bogotá, Medellín…)
- capacidad
- recursos (lista: pizarra, proyector…)

**Endpoints clave:**

- `GET /rooms`
- `POST /rooms` (admin)
- `PUT /rooms/{id}` (admin)
- `DELETE /rooms/{id}` (admin)

---

#### 3. Reservas (Reservation)

- id
- usuario_id
- sala_id
- fecha
- hora_inicio
- hora_fin
- estado (pendiente, confirmada, cancelada)

**Endpoints clave:**

- `POST /reservations`
- `GET /reservations/me`
- `GET /reservations/room/{room_id}`
- `GET /reservations/date/{yyyy-mm-dd}`
- `DELETE /reservations/{id}` (cancelar)

---

### 🔢 Validaciones Clave

- Validar que no haya cruce de horarios para la misma sala.  
- Validar que las reservas sean de bloques de 1 hora exactos.  
- Limitar acciones administrativas solo a usuarios con rol **admin**.  

---

### 📊 Reportes opcionales (Solo admin)

- “¿Qué sala se ha reservado más veces?”  
- “¿Cuántas horas ha reservado un usuario este mes?”  

---

### ✨ Características extra (opcional)

- Lógica de penalización si se cancelan muchas reservas  

---

## 🏋️ Estructura de Rutas (Resumen)

### Autenticación
- `POST /auth/register`
- `POST /auth/login`

### Usuarios
- `GET /users/me`
- `GET /users/` # Solo admin
- `DELETE /users/{id}` # Solo admin

### Salas
- `GET /rooms`
- `POST /rooms` # Solo admin
- `PUT /rooms/{id}` # Solo admin
- `DELETE /rooms/{id}` # Solo admin

### Reservas
- `POST /reservations`
- `GET /reservations/me`
- `GET /reservations/room/{room_id}`
- `GET /reservations/date/{yyyy-mm-dd}`
- `DELETE /reservations/{id}` # cancelar

---

## 🚀 Por qué es un buen proyecto para practicar

- Manejo de relaciones reales entre entidades  
- Autenticación y roles en FastAPI  
- Validaciones de negocio no triviales  
- Construcción de reportes  