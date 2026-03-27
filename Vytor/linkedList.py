# Definição do nó da lista fornecida pelo LeetCode:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior = None
        atual = head
        
        while atual:
            proximo_temporario = atual.next  # Salva o próximo nó
            atual.next = anterior            # Inverte o ponteiro
            anterior = atual                 # Move o 'anterior' um passo à frente
            atual = proximo_temporario       # Move o 'atual' um passo à frente
            
        return anterior