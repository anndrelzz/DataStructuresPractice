class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        tamanho = len(nums)
        resultado = [1] * tamanho
        
        # Primeira passagem: calculando os produtos à esquerda (prefix)
        prefixo = 1
        for i in range(tamanho):
            resultado[i] = prefixo
            prefixo *= nums[i]
            
        # Segunda passagem: calculando os produtos à direita (postfix) e multiplicando
        sufixo = 1
        for i in range(tamanho - 1, -1, -1):
            resultado[i] *= sufixo
            sufixo *= nums[i]
            
        return resultado