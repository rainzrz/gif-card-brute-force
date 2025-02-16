def gerarCodigoManual(tamanho, caracteres='0123456789'):
    if tamanho == 0:
        yield ""  
    else:
        for caractere in caracteres:
            for codigo in gerarCodigoManual(tamanho - 1, caracteres):
                yield caractere + codigo 
                
def verificarCodigoGiftCard(codigoGerado,codigoGiftCard):
    if codigoGerado == codigoGiftCard:
        print("Código Encontrado: " + codigoGerado)
        return True
        
def bruteForceGiftCard(codigoGiftCard, tamanho):
    for codigoGerado in gerarCodigoManual(tamanho):
        if verificarCodigoGiftCard(codigoGerado, codigoGiftCard):
            return codigoGerado

# Exemplo de uso
codigoGiftCard = "12345678"
tamanhoCodigo = len(codigoGiftCard)
bruteForceGiftCard(codigoGiftCard, tamanhoCodigo)