# Definição para um nó da lista encadeada simples (padrão do LeetCode)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Criamos um nó "dummy" (fictício) que aponta para o início da lista.
        # Isso ajuda a lidar com casos onde precisamos remover o primeiro nó.
        dummy = ListNode(0, head)
        esquerda = dummy
        direita = head

        # Passo 1: Movemos o ponteiro da direita 'n' vezes para frente.
        # Isso cria um "atraso" ou espaço de tamanho 'n' entre os ponteiros.
        while n > 0 and direita:
            direita = direita.next
            n -= 1

        # Passo 2: Movemos os dois ponteiros juntos até que o da direita chegue ao fim.
        # Quando 'direita' chegar no nulo, 'esquerda' estará exatamente ANTES do nó que queremos remover.
        while direita:
            esquerda = esquerda.next
            direita = direita.next

        # Passo 3: "Pulamos" o nó indesejado ajustando o ponteiro .next
        esquerda.next = esquerda.next.next

        # Retornamos a lista a partir do nó real (ignorando o dummy)
        return dummy.next

if __name__ == "__main__":
    # Criando a lista: 1 -> 2 -> 3 -> 4 -> 5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    sol = Solution()
    # Removendo o 2º nó de trás para frente (o nó 4)
    nova_lista = sol.removeNthFromEnd(n1, 2)

    # Imprimindo o resultado
    atual = nova_lista
    while atual:
        print(atual.val, end=" -> " if atual.next else "")
        atual = atual.next
    # Saída esperada: 1 -> 2 -> 3 -> 5