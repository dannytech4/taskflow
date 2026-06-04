-- borrado logico
UPDATE tasks
SET is_deleted = 1 WHERE id = 1;

-- Consultar solo tareas activas
SELECT t.id, t.title, t.description, t.status, u.name FROM tasks t
INNER JOIN users u ON t.user_id = u.id
WHERE t.is_deleted = 0; -- 1 = Pendiente, 2 = En progreso, 3 = Completada, 4 = Cancelada

--consultar Pendientes
SELECT * FROM tasks
WHERE status = 1
AND is_deleted = 0;

-- Cambiar estado, Cuando el frontend haga: PUT /tasks/1/status
UPDATE tasks
SET status = 2
WHERE id = 1;

--consulta para el dashboard
SELECT t.id, t.title, t.description,
    CASE
        WHEN t.status = 1 THEN 'Pendiente'
        WHEN t.status = 2 THEN 'En progreso'
        WHEN t.status = 3 THEN 'Completada'
        WHEN t.status = 4 THEN 'Cancelada'
    END AS status_name,
    u.name AS assigned_user,
    t.created_at
FROM tasks t
INNER JOIN users u ON t.user_id = u.id
WHERE t.is_deleted = 0
ORDER BY t.created_at DESC;

-- 
SELECT
    t.id,
    t.title,
    ts.name AS status,
    u.name AS assigned_user,
    t.created_at
FROM tasks t
INNER JOIN users u
    ON t.user_id = u.id
INNER JOIN task_statuses ts
    ON t.status_id = ts.id
WHERE t.is_deleted = 0
ORDER BY t.created_at DESC;

--union de usuario, tarea, estado
SELECT t.id, t.title, ts.name AS status, u.name AS assigned_user
FROM tasks t
INNER JOIN users u ON t.user_id = u.id
INNER JOIN task_statuses ts ON t.status_id = ts.id
WHERE t.is_deleted = 0;


--Total tareas activas
SELECT COUNT(*) AS active_tasks
FROM tasks
WHERE is_deleted = 0;

--filtrar por estado
SELECT
    t.title,
    ts.name
FROM tasks t
INNER JOIN task_statuses ts
    ON t.status_id = ts.id
WHERE ts.name = 'En progreso'
AND t.is_deleted = 0; -- 1 = Pendiente, 2 = En progreso, 3 = Completada, 4 = Cancelada



