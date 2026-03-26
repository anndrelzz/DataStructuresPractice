class Solution(object):
    def isValid(self, s):
        # A pilha (stack) armazenará apenas os símbolos de abertura
        pilha = []
        # Mapeamento: a chave é o fechamento, o valor é a abertura correspondente
        mapeamento = {")": "(", "}": "{", "]": "["}

        for caractere in s:
            # Se o caractere for um símbolo de fechamento
            if caractere in mapeamento:
                # Removemos o elemento do topo da pilha se ela não estiver vazia
                # Caso esteja vazia, usamos um símbolo 'coringa' (#) que nunca dará match
                elemento_topo = pilha.pop() if pilha else '#'
                # Se o símbolo que saiu da pilha não for o par correto, é inválido
                if mapeamento[caractere] != elemento_topo:
                    return False
            else:
                # Se for um símbolo de abertura (, {, [, nós empilhamos
                pilha.append(caractere)

        # No final, se a pilha estiver vazia, significa que todos os pares foram fechados
        return not pilha

# --- Para rodar no seu Terminal ---
if __name__ == "__main__":
    sol = Solution()
    print("Teste '()[]{}':", sol.isValid("()[]{}")) # True
    print("Teste '([)]':", sol.isValid("([)]"))     # False
    print("Teste '((()))':", sol.isValid("((()))")) # True