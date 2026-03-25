class Solution:
    def maxArea(self, height):
        # Ponteiro da esquerda começa no início da lista
        left = 0
        
        # Ponteiro da direita começa no final da lista
        right = len(height) - 1
        
        # Variável para armazenar a maior área encontrada
        max_area = 0

        # Loop continua enquanto os ponteiros não se cruzarem
        while left < right:
            
            # ----------------------------------------
            # 1. CALCULAR A ALTURA DO CONTAINER
            # ----------------------------------------
            # A altura é limitada pela menor parede
            h = min(height[left], height[right])
            
            # ----------------------------------------
            # 2. CALCULAR A LARGURA
            # ----------------------------------------
            # Distância entre os dois ponteiros
            w = right - left
            
            # ----------------------------------------
            # 3. CALCULAR A ÁREA
            # ----------------------------------------
            # Fórmula: área = altura * largura
            area = h * w

            # ----------------------------------------
            # 4. ATUALIZAR A MAIOR ÁREA
            # ----------------------------------------
            # Guarda o maior valor entre o atual e o anterior
            max_area = max(max_area, area)

            # ----------------------------------------
            # 5. MOVER OS PONTEIROS
            # ----------------------------------------
            # Move o lado com menor altura, pois ele limita a área
            if height[left] < height[right]:
                left += 1  # Move ponteiro esquerdo para a direita
            else:
                right -= 1  # Move ponteiro direito para a esquerda

        # Retorna a maior área encontrada
        return max_area