def calPoints(ops):
    pilha = []  # Nossa estrutura de pilha (lista vazia)

    for op in ops:  # Percorre cada operação da lista

        if op == "C":
            pilha.pop()  # Remove a última pontuação registrada (topo da pilha)

        elif op == "D":
            pilha.append(pilha[-1] * 2)  # Pega o topo (pilha[-1]) e empilha o dobro

        elif op == "+":
            # pilha[-1] = última pontuação, pilha[-2] = penúltima
            pilha.append(pilha[-1] + pilha[-2])  # Empilha a soma das duas últimas

        else:
            pilha.append(int(op))  # É um número: converte string → int e empilha

    return sum(pilha)  # Soma tudo que ficou válido na pilha e retorna