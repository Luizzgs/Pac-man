
# define graph
grafo = {
    "A1" : ["A2","B1"],
    "A2" : ["A1", "A3"],
    "A3" : ["A2", "A4"],
    "A4" : ["A3","B4"],
    "A6" : ["A7", "B6"],
    "A7" : ["A6", "A8"],
    "A8" : ["A7", "A9"],
    "A9" : ["A8", "A10"],
    "A10" : ["A9", "A11"],
    "A11" : ["A10", "A12"],
    "A12" : ["A11", "A13"],
    "A13" : ["A12", "B13"],
    "A15" : ["A16", "B15"],
    "A16" : ["A15", "A17"],
    "A17" : ["A16", "A18"],
    "A18" : ["A17", "B18"],
    "B1" : ["A1", "C1"],
    "B4" : ["A4","C4"],
    "B13" : ["A13", "C13"],
    "B15" : ["A15", "C15"],
    "B18" : ["A18", "C18"],
    "C1" : ["B1", "D1"],
    "C3" : ["C4", "D3"],
    "C4" : ["B4", "C3", "C5"],
    "C5" : ["C4", "C6"],
    "C6" : ["B6", "C5", "C7", "D6"],
    "C7" : ["C6", "C8"],
    "C8" : ["C7", "C9"],
    "C9" : ["C8", "C10", "D9"],
    "C10" : ["C9", "C11", "D10"],
    "C11" : ["C10", "C12"],
    "C12" : ["C11", "C13"],
    "C13" : ["B13", "C12", "C14", "D13"],
    "C14" : ["C13", "C15"],
    "C15" : ["B15", "C14", "C16"],
    "C16" : ["C15", "D16"],
    "C18" : ["B18", "D18"],
    "D1" : ["C1", "E1"],
    "D3" : ["C3", "E3"],
    "D6" : ["C6", "E6"],
    "D9" : ["C9", "D10", "E9"],
    "D10" : ["C10", "D9", "E10"],
    "D13" : ["C13", "E13"],
    "D16" : ["C16", "E16"],
    "D18" : ["C18", "E18"],
    "E1" : ["D1", "E2", "F1"],
    "E2" : ["E1", "E3"],
    "E3" : ["D3", "E2", "E4", "F3"],
    "E4" : ["E3", "E5"],
    "E5" : ["E4", "E6"],
    "E6" : ["D6", "E5", "F6"],
    "E8" : ["D8", "E9", "F8"],
    "E9" : ["D9", "E8", "E10"],
    "E10" : ["D10", "E9", "E11"],
    "E11" : ["E10"],
    "E13" : ["D13", "E14", "F13"],
    "E14" : ["E13", "E15"],
    "E15" : ["E14", "E16"],
    "E16" : ["D16", "E15", "E17", "F16"],
    "E17" : ["E16", "E18"],
    "E18" : ["D18", "E17", "F18"],
    "F1" : ["E1", "G1"],
    "F3" : ["E3", "G3"],
    "F6" : ["E6", "G6"],
    "F13" : ["E13", "G13"],
    "F16" : ["E16", "G16"],
    "F18" : ["E18", "G18"],
    "G1" : ["F1", "H1"],
    "G3" : ["F3", "G4"],
    "G4" : ["G3", "G5", "H4"],
    "G5" : ["G4", "G6"],
    "G6" : ["F6", "G5", "G7", "H6"],
    "G7" : ["G6", "G8"],
    "G8" : ["G7", "G9"],
    "G9" : ["G8", "G10"],
    "G10" : ["G9", "G11"],
    "G11" : ["G10", "G12"],
    "G12" : ["G11", "G13"],
    "G13" : ["F13", "G12", "G14", "H13"],
    "G14" : ["G13", "G15"],
    "G15" : ["G14", "G16", "H15"],
    "G16" : ["F16", "G15"],
    "G18" : ["F18", "H18"],
    "H1" : ["G1", "I1"],
    "H4" : ["G4", "I4"],
    "H6" : ["G6", "I6"],
    "H13" : ["G13", "I13"],
    "H15" : ["G15", "I15"],
    "H18" : ["G18", "I18"],
    "I1" : ["H1", "I2"],
    "I2" : ["H2", "I1"],
    "I4" : ["H4", "I3"],
    "I6" : ["H6", "I7"],
    "I7" : ["I6", "I8"],
    "I8" : ["I7", "I9"],
    "I9" : ["I8", "I10"],
    "I10" : ["I9", "I11"],
    "I11" : ["I10", "I12"],
    "I12" : ["I11", "I13"],
    "I13" : ["H13", "I12"],
    "I15" : ["H15", "I16"],
    "I16" : ["I15", "I17"],
    "I17" : ["I16", "I18"],
    "I18" : ["H18", "I17"]
}




#define o local de origem 
origem = "E18"

#define o destino
destino = "A2"

def busca_em_extensao():
    # fila de busca
    fila = [origem]

    # nós visitados
    visitados = [origem]

    # define o caminho 
    parentes = {}

    # enquanto a fila não estiver vazia
    while fila:
        no = fila.pop(0)

        # verifica se é o destino
        if no == destino:
            destino_atual = destino
            caminho = [destino_atual]
            while destino_atual != origem:
                caminho.append(parentes[destino_atual])
                destino_atual = parentes[destino_atual]
            return caminho[::-1]


        for vizinho in grafo[no]:
            # verifica se o nó vizinho está nos nós visitados
            if vizinho not in visitados:
                # adiciona o nó como visitado
                visitados.append(vizinho)

                fila.append(vizinho)

                # adiciona o pai do vizinho sendo o nó
                parentes[vizinho] = no

    return False

resultado = busca_em_extensao()

if not resultado:
    print("Não foi encontrado um caminho!")
else:
    print("Caminho: ", resultado)

