class Solution:
    def deleteDuplicates(self, head):
        
        # ----------------------------------------
        # 1. CRIA UM NÓ FAKE (ANTES DO HEAD)
        # ----------------------------------------
        # Serve pra evitar problemas ao remover elementos do início
        fake_head = ListNode(0)
        fake_head.next = head

        # ----------------------------------------
        # 2. DOIS PONTEIROS
        # ----------------------------------------
        # prev → último nó válido (sem duplicata)
        # curr → nó atual que estamos analisando
        prev = fake_head
        curr = head

        # ----------------------------------------
        # 3. PERCORRE A LISTA
        # ----------------------------------------
        while curr:
            
            # ----------------------------------------
            # 4. VERIFICA SE É DUPLICADO
            # ----------------------------------------
            # Se o valor atual é igual ao próximo → temos duplicata
            if curr.next and curr.val == curr.next.val:
                
                # guarda o valor duplicado
                duplicate = curr.val

                # ----------------------------------------
                # 5. PULA TODOS OS NÓS COM ESSE VALOR
                # ----------------------------------------
                # continua andando enquanto for igual
                while curr and curr.val == duplicate:
                    curr = curr.next
                
                # ----------------------------------------
                # 6. REMOVE TODOS OS DUPLICADOS
                # ----------------------------------------
                # liga o último válido direto ao próximo diferente
                prev.next = curr

            else:
                # ----------------------------------------
                # 7. SE NÃO É DUPLICADO → MANTÉM
                # ----------------------------------------
                # avança normalmente
                prev = prev.next
                curr = curr.next

        # ----------------------------------------
        # 8. RETORNA A LISTA (SEM O FAKE_HEAD)
        # ----------------------------------------
        return fake_head.next