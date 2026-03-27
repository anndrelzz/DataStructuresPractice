from typing import Optional  # Import necessário para usar o tipo 'Optional'

# 1. Definição do Nó (A "caixinha" da lista)
class ListNode:
    def __init__(self, x):
        self.val = x          # Guarda o número (ex: 10, 20)
        self.next = None      # Guarda o endereço do próximo nó

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Iniciamos dois ponteiros no começo da lista (head)
        lento = head
        rapido = head
        
        # Enquanto o ponteiro RÁPIDO não encontrar o fim da lista (None)
        # Verificamos 'rapido' (ele mesmo) e 'rapido.next' (o próximo dele)
        while rapido and rapido.next:
            
            lento = lento.next          # O lento anda de 1 em 1 nó
            rapido = rapido.next.next    # O rápido pula de 2 em 2 nós
            
            # Se em algum momento o endereço de memória for IGUAL...
            if lento == rapido:
                return True             # ...então a "Lebre" alcançou a "Tartaruga" (Ciclo!)
                
        # Se o 'while' terminar, significa que o ponteiro rápido achou o fim da linha
        return False

# --- ÁREA DE TESTE (Para rodar no seu terminal) ---
if __name__ == "__main__":
    # Criando 3 nós isolados
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    # Ligando eles: 1 -> 2 -> 3
    n1.next = n2
    n2.next = n3

    # CRIANDO O CICLO: O nó 3 aponta de volta para o nó 1
    n3.next = n1 

    # Instanciamos a classe e testamos
    sol = Solution()
    if sol.hasCycle(n1):
        print(">>> CICLO DETECTADO! (A lebre alcançou a tartaruga)")
    else:
        print(">>> LISTA LIMPA! (Sem ciclos)")