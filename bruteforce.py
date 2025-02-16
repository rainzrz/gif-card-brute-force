codigoGerado = 111112222233333
codigoGiftCard = 111112222233333

 
def verificarCodigoGiftCard(codigoGerado,codigoGiftCard):
    if codigoGerado == codigoGiftCard:
        print("Código Encontrado")
        return True
    else:
        print("Código Inválido")
        return False
        

verificarCodigoGiftCard(codigoGerado,codigoGiftCard)
