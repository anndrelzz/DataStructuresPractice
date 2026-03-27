# Definimos a classe que conterá a nossa lógica
class Solution:
    # Função principal que recebe a lista de números 'nums'
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        # Criamos uma lista vazia para guardar todas as combinações que encontrarmos
        resultado = []
        
        # Criamos uma função interna (recursiva)
        def backtrack(caminho_atual):
            
            # SE o tamanho do caminho atual for igual ao tamanho da lista original
            if len(caminho_atual) == len(nums):
                # significa que terminamos uma combinação! 
                # Tiramos uma cópia [:] e guardamos na nossa lista de resultados.
                resultado.append(caminho_atual[:])
                return

            # Para cada número que existe na nossa lista de entrada...
            for num in nums:
                
                # Verificamos se o número já foi usado no caminho que estamos montando
                if num in caminho_atual:
                    continue
                
                # 1. ESCOLHA: Adicionamos o número no final da nossa lista temporária
                caminho_atual.append(num)
                
                # 2. EXPLORAÇÃO: Chamamos a função novamente para escolher o PRÓXIMO número
                # Isso faz o código "mergulhar" mais fundo na árvore de decisões
                backtrack(caminho_atual)
                
                # 3. DESFAZER (Backtrack): Removemos o último número colocado
                # Isso "limpa o rastro" para que o laço 'for' possa testar um número diferente
                caminho_atual.pop()

        # Damos o pontapé inicial na função enviando uma lista vazia
        backtrack([])
        
        # No final de tudo, devolvemos a lista com todas as permutações
        return resultado

# --- CÓDIGO DE EXECUÇÃO (DRIVER CODE) ---

if __name__ == "__main__":
    # Criamos o objeto 'solucionador' baseado na nossa classe
    solucionador = Solution()
    
    # Definimos o array que queremos permutar
    meu_array = [1, 2, 3, 4, 5, 6, 7,]
    
    # Exibimos mensagens no terminal para ficar organizado
    print(f"Gerando permutas para: {meu_array}")
    print("-" * 30)
    
    # Chamamos a função e guardamos o retorno na variável 'todas_permutas'
    todas_permutas = solucionador.permute(meu_array)
    
    # Usamos um laço para imprimir cada permutação em uma linha nova
    for p in todas_permutas:
        print(p)
        
    # Mostramos o total de combinações encontradas (deve ser 6 para o array [1,2,3])
    print("-" * 30)
    print(f"Total de permutações encontradas: {len(todas_permutas)}")
