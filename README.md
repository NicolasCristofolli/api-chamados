# API de Chamados
estudo de APIs e python

## Funcionalidades atuais

criar_chamado
fechar_chamado
listar_por_status
contar_por_prioridade

## Como rodar

python demo.py


SELECT prioridade, COUNT(*) AS total
FROM chamados
WHERE status = 'aberto'
GROUP BY prioridade ORDER BY total;