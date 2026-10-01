chamados=# CREATE TABLE chamados (
    id  SERIAL PRIMARY KEY,
    titulo  TEXT NOT NULL CHECK (trim(titulo) <> ''),
    prioridade TEXT NOT NULL CHECK (prioridade IN ('baixa', 'media', 'alta')),
    status TEXT NOT NULL DEFAULT 'aberto'
);