-- Lista os chamados abertos em ordem alfabética de título
SELECT titulo, prioridade FROM chamados WHERE status = 'aberto' ORDER BY titulo;

-- Faz u contagem de quantos status aberto temos na coluna prioridade em ordem maior pro menor
SELECT prioridade, COUNT(*) AS total FROM chamados WHERE status = 'aberto' GROUP BY prioridade ORDER BY total DESC;

-- Atualizar na tabela chamados na coluna status para fechado no id 2
UPDATE chamados SET status = 'fechado' WHERE id = 2;

-- Mostrar o ID onde a coluna Status esta como fechado
SELECT id, status FROM chamados WHERE status = 'fechado';
  
