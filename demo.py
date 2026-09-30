from chamados import criar_chamado, fechar_chamado, listar_por_status, contar_por_prioridade

#VALIDOS
try:
    print(criar_chamado("valido", "alta"))
except ValueError as erro:
    print(f"Erro: {erro}")
try:
    print(criar_chamado("valido2", "baixa"))
except ValueError as erro:
    print(f"Erro: {erro}")
try:
    
    print(criar_chamado('valido2', 'media'))
except ValueError as erro:
    print(f"Erro: {erro}")
#PRIORIDADE INVALIDA
try:
    print(criar_chamado("titulo", "altissima"))
except ValueError as erro:
    print(f"Erro: {erro}")
#TITULO INVALIDO
try:
    print(criar_chamado("", "alta"))
except ValueError as erro:
    print(f"Erro: {erro}")
#FECHAMENDO ID
try:
    print(fechar_chamado(1))
except ValueError as erro:
    print(f"Erro: {erro}")
try:
    print(fechar_chamado(11))
except ValueError as erro:
    print(f"Erro: {erro}")
print(listar_por_status("fechado"))
print(contar_por_prioridade())