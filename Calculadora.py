def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

print('Insira o valor a ser convertido de Byte para Bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def ByteParaKbyte(valorASerConvertido):
    print('Valor convertido de Byte para Kbyte')
    KilobytesCalculado = valorASerConvertido / 1024
    return KbytesCalculado

def KilobytesParaBytes(valorASerConvertido):
    print('Valor convertido de Kbyte para byte')
    BytesCalculado = valorASerConvertido * 1024
    return BytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KilobytesParaBytes(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def KilobyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de Kilobyte para Megabyte10')
    MegabytesCalculado = valorASerConvertido / 1024
    return MegabytesCalculado
def MegabytesParaKilobytes(valorASerConvertido):
    print('Valor convertido de Megabyte para Kilobyte')
    KilobytesCalculado = valorASerConvertido * 1024
    return KilobytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KilobytesParaBytes(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

