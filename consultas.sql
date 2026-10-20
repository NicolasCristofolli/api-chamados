-- Lista os chamados abertos em ordem alfabética de título
SELECT titulo, prioridade FROM chamados WHERE status = 'aberto' ORDER BY titulo;

-- Mostra, para cada prioridade, quantos chamados abertos existem, do maior para o menor
SELECT prioridade, COUNT(*) AS total FROM chamados WHERE status = 'aberto' GROUP BY prioridade ORDER BY total DESC;

-- Atualizar na tabela chamados na coluna status para fechado no id 2
UPDATE chamados SET status = 'fechado' WHERE id = 2;

-- Mostrar o ID onde a coluna Status esta como fechado
SELECT id, status FROM chamados WHERE status = 'fechado';
  
-- Deletar as linhas onde o status esta em fechado
DELETE FROM chamados WHERE status = 'fechado';