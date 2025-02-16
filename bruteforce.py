# Defina todas as variáveis globais em um único lugar
CARACTERES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Caracteres possíveis
TAMANHO_PADRAO = 5  # Tamanho padrão do código
MENSAGEM_ACERTO = "Código Encontrado: {}"  # Mensagem de sucesso
MENSAGEM_COMBINACOES = "Total de combinações possíveis: {}"  # Mensagem de log

def gerarCodigoManual(tamanho, caracteres=CARACTERES):
    if tamanho == 0:
        yield ""  
    else:
        for caractere in caracteres:
            for codigo in gerarCodigoManual(tamanho - 1, caracteres):
                yield caractere + codigo 
                
def verificarCodigoGiftCard(codigoGerado, codigoGiftCard):
    if codigoGerado == codigoGiftCard:
        print(MENSAGEM_ACERTO.format(codigoGerado))  # Usa a mensagem global
        return True
        
def bruteForceGiftCard(codigoGiftCard, tamanho=TAMANHO_PADRAO, caracteres=CARACTERES):
    total_combinacoes = len(caracteres) ** tamanho
    print(MENSAGEM_COMBINACOES.format(total_combinacoes))  # Usa a mensagem global
    
    for codigoGerado in gerarCodigoManual(tamanho, caracteres):
        if verificarCodigoGiftCard(codigoGerado, codigoGiftCard):
            return codigoGerado
    return None

# Exemplo de uso
codigoGiftCard = "12345"
bruteForceGiftCard(codigoGiftCard)  # Usa o tamanho padrão definido globalmente