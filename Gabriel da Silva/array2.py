class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Não retorne nada, modifique o array 'nums' in-place.
        """
        # Este ponteiro indica a posição onde o próximo número diferente de zero deve ficar
        proxima_posicao_livre = 0
        
        # O 'i' percorre todo o array procurando números que não são zero
        for i in range(len(nums)):
            # Se encontrarmos um número que NÃO é zero...
            if nums[i] != 0:
                # ...nós trocamos ele de lugar com a posição que o ponteiro livre aponta.
                # Isso joga o número para frente e o zero para trás em um único passo.
                nums[proxima_posicao_livre], nums[i] = nums[i], nums[proxima_posicao_livre]
                
                # Movemos o ponteiro livre uma casa para a direita
                proxima_posicao_livre += 1

# --- TESTE NO CODESPACES ---
if __name__ == "__main__":
    sol = Solution()
    
    # Exemplo 1
    teste1 = [0, 0, 3, 1, 12]
    sol.moveZeroes(teste1)
    print(f"Exemplo 1: {teste1}") # Saída: [1, 3, 12, 0, 0]
    
    # Exemplo 2
    teste2 = [0]
    sol.moveZeroes(teste2)
    print(f"Exemplo 2: {teste2}") # Saída: [0]