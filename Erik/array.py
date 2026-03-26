class Solution(object):
    def combinationSum(self, candidates, target):
        resultado = []

        def backtrack(restante, combinacao_atual, indice_inicio):
            # Caso Base 1: Se o restante for 0, encontramos uma combinação válida!
            if restante == 0:
                resultado.append(list(combinacao_atual))
                return

            # Caso Base 2: Se o restante for negativo, a soma passou do alvo
            if restante < 0:
                return

            # Explorando os candidatos a partir do índice atual
            for i in range(indice_inicio, len(candidates)):
                # Adicionamos o número na combinação atual
                combinacao_atual.append(candidates[i])

                # Chamada recursiva: Note que passamos 'i' como início,
                # permitindo reutilizar o mesmo número (como o [2, 2, 3])
                backtrack(restante - candidates[i], combinacao_atual, i)

                # Backtrack: Removemos o último número para testar o próximo do loop
                combinacao_atual.pop()

        backtrack(target, [], 0)
        return resultado

if __name__ == "__main__":
    # 1. Instanciamos a classe (criamos o objeto)
    solucao = Solution()
    # 2. Definimos os dados de teste (Exemplo 1 do desafio)
    candidatos = [2, 3, 6, 7]
    alvo = 7
    # 3. Chamamos a função e guardamos o resultado
    resultado = solucao.combinationSum(candidatos, alvo)
    # 4. Imprimimos no terminal
    print("--- Desafio: Combination Sum ---")
    print(f"Candidatos: {candidatos}")
    print(f"Alvo: {alvo}")
    print(f"Combinações encontradas: {resultado}")