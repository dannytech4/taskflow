
CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(150) NOT NULL UNIQUE,
    is_active BIT NOT NULL DEFAULT 1,
    created_at DATETIME2 NOT NULL DEFAULT GETDATE()
);

CREATE TABLE tasks (
    id INT PRIMARY KEY IDENTITY(1,1),
    title NVARCHAR(200) NOT NULL,
    description NVARCHAR(MAX),
    status_id TINYINT NOT NULL,
    user_id INT NOT NULL,
    is_deleted BIT NOT NULL DEFAULT 0,
    created_at DATETIME2 NOT NULL DEFAULT GETDATE(),
    updated_at DATETIME2 NULL,

    CONSTRAINT FK_tasks_users
        FOREIGN KEY (user_id)
        REFERENCES users(id),

    CONSTRAINT FK_tasks_statuses
        FOREIGN KEY (status_id)
        REFERENCES task_statuses(id)
);

INSERT INTO users(name,email) VALUES
('Juan Perez','juan@test.com'),
('Ana Lopez','ana@test.com'),
('Carlos Ruiz','carlos@test.com');

INSERT INTO tasks (title,description,status_id,user_id) VALUES 
( 'Crear API', 'Construir endpoints FastAPI', 1, 1 );
( 'Diseñar Angular', 'Crear componentes iniciales', 2, 2 );

CREATE TABLE task_statuses (
    id TINYINT PRIMARY KEY,
    name NVARCHAR(50) NOT NULL,
    is_active BIT NOT NULL DEFAULT 1
);

INSERT INTO task_statuses(id, name) VALUES
(1, 'Pendiente'),
(2, 'En progreso'),
(3, 'Completada'),
(4, 'Cancelada');

