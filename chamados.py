chamados = []
proximo_id = 1
def criar_chamado(titulo, prioridade):
    prioridadeslista = ['baixa','alta', 'media']
    global proximo_id

    if prioridade not in prioridadeslista:
        raise ValueError("Precisa colocar a prioridade correta")
    elif titulo is None:
        raise ValueError("Precisa colocar titulo")
    elif titulo.strip() == "":
        raise ValueError("Precisa colocar titulo")
    
    chamado = {
        "id": proximo_id,
        "titulo": titulo,
        "prioridade": prioridade,
        "status": "aberto",
    }
    chamados.append(chamado)
    proximo_id += 1
    return chamado

def listar_por_status(status):
    resultado = []
    for chamado in chamados:
        if chamado['status'] == status:
            resultado.append(chamado)
    return resultado

def fechar_chamado(id):
    for chamado in chamados:

        if chamado["id"] == id:
            chamado["status"] = "fechado"
            return chamado
    raise ValueError("nao encontrei o ID")

def contar_por_prioridade():
    contagem_prioridades = {}
    for chamado in chamados:

        if chamado["prioridade"] in contagem_prioridades:
            contagem_prioridades[chamado["prioridade"]] += 1
        else:
            contagem_prioridades[chamado["prioridade"]] = 1
    return contagem_prioridades
