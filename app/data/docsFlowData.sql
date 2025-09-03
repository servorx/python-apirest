-- en este documento van archivos de prueba
INSERT INTO users (nombre, email, contraseña_hash, rol) VALUES
('Carlos López', 'carlos.lopez@campusdev.com', 'hash_123', 'Administrador'),
('María Pérez', 'maria.perez@campusdev.com', 'hash_124', 'Estudiante'),
('Juan Torres', 'juan.torres@campusdev.com', 'hash_125', 'Profesor'),
('Laura Gómez', 'laura.gomez@campusdev.com', 'hash_126', 'Estudiante'),
('Andrés Castro', 'andres.castro@campusdev.com', 'hash_127', 'Profesor'),
('Diana Ramírez', 'diana.ramirez@campusdev.com', 'hash_128', 'Estudiante'),
('Felipe Sánchez', 'felipe.sanchez@campusdev.com', 'hash_129', 'Administrador'),
('Camila Rojas', 'camila.rojas@campusdev.com', 'hash_130', 'Profesor'),
('Julián Méndez', 'julian.mendez@campusdev.com', 'hash_131', 'Estudiante'),
('Valentina Ruiz', 'valentina.ruiz@campusdev.com', 'hash_132', 'Profesor');

INSERT INTO rooms (nombre, sede, capacidad, recursos) VALUES
('Sala 101', 'Sede Norte', 30, 'Proyector, Pizarra'),
('Sala 102', 'Sede Norte', 25, 'TV, Audio'),
('Auditorio A', 'Sede Centro', 100, 'Sonido, Iluminación, Pantalla'),
('Laboratorio 1', 'Sede Sur', 20, 'Computadores, Proyector'),
('Laboratorio 2', 'Sede Sur', 25, 'Computadores'),
('Sala 201', 'Sede Norte', 40, 'Pizarra'),
('Sala 202', 'Sede Centro', 50, 'Proyector, Audio'),
('Biblioteca', 'Sede Centro', 80, 'Mesas de estudio, WiFi'),
('Sala Virtual 1', 'Online', 9999, 'Zoom, Grabación'),
('Sala 301', 'Sede Sur', 35, 'Proyector, Pizarra');

INSERT INTO reservations (usuario_id, sala_id, fecha, hora_inicio, hora_fin, estado) VALUES
(2, 1, '2025-09-05', '08:00:00', '10:00:00', 'Confirmada'),
(3, 2, '2025-09-05', '10:00:00', '12:00:00', 'Pendiente'),
(4, 3, '2025-09-06', '09:00:00', '11:00:00', 'Confirmada'),
(5, 4, '2025-09-06', '14:00:00', '16:00:00', 'Cancelada'),
(6, 5, '2025-09-07', '08:00:00', '10:00:00', 'Confirmada'),
(7, 6, '2025-09-07', '11:00:00', '13:00:00', 'Pendiente'),
(8, 7, '2025-09-08', '15:00:00', '17:00:00', 'Confirmada'),
(9, 8, '2025-09-08', '09:00:00', '11:00:00', 'Confirmada'),
(10, 9, '2025-09-09', '07:00:00', '09:00:00', 'Pendiente'),
(2, 10, '2025-09-09', '12:00:00', '14:00:00', 'Confirmada'),
(3, 1, '2025-09-10', '08:00:00', '10:00:00', 'Confirmada'),
(4, 2, '2025-09-10', '10:00:00', '12:00:00', 'Pendiente'),
(5, 3, '2025-09-11', '13:00:00', '15:00:00', 'Confirmada'),
(6, 4, '2025-09-11', '16:00:00', '18:00:00', 'Cancelada'),
(7, 5, '2025-09-12', '09:00:00', '11:00:00', 'Confirmada'),
(8, 6, '2025-09-12', '11:00:00', '13:00:00', 'Pendiente'),
(9, 7, '2025-09-13', '15:00:00', '17:00:00', 'Confirmada'),
(10, 8, '2025-09-13', '08:00:00', '10:00:00', 'Confirmada'),
(2, 9, '2025-09-14', '07:00:00', '09:00:00', 'Pendiente'),
(3, 10, '2025-09-14', '12:00:00', '14:00:00', 'Confirmada');
