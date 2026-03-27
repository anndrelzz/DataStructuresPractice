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
            
        return anteriorclass MinStack:
    def __init__(self):
        self.pilha = []
        self.pilha_minimos = [] # Pilha auxiliar para rastrear o menor valor

    def push(self, val: int) -> None:
        self.pilha.append(val)
        # O novo mínimo é o menor valor entre o valor atual e o topo da pilha de mínimos
        if not self.pilha_minimos:
            val_minimo = val
        else:
            val_minimo = min(val, self.pilha_minimos[-1])
        self.pilha_minimos.append(val_minimo)

    def pop(self) -> None:
        self.pilha.pop()
        self.pilha_minimos.pop()

    def top(self) -> int:
        return self.pilha[-1]

    def getMin(self) -> int:
        return self.pilha_minimos[-1]