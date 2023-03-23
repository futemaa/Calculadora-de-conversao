from Calculadora import converterStringParaFloat, bitParaByte, byteParaBit, ByteParaKilobyte, KilobytesParaBytes, Kilobytesparamegabytes, megabytesparakilobytes, MegabyteParaGigabyte, GigabytesParaMegabytes, gigabyteParaTerabyte, terabytesParagigabytes, terabyteparapetabyte, petabytesparaterabytes  

print('-Escreva 1 para bitParaByte\n -Escreva 2 byteParaBit\n -Escreva 3 ByteParaKilobyte\n -Escreva 4 KilobytesParaBytes\n -Escreva 5 Kilobytesparamegabytes\n -Escreva 6 megabytesparakilobytes\n -Escreva 7 MegabyteParaGigabyte\n -Escreva 8 GigabytesparaMegabytes\n -Escreva 9 gigabyteParaTerabyte\n -Escreva 10 terabytesParagigabytes\n -Escreva 11 terabyteparapetabyte \n -Escreva 12 petabytesparaterabytes')
funcEscolha = input()

if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = ByteParaKilobyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = KilobytesParaBytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = Kilobytesparamegabytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)
    
elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = megabytesparakilobytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = MegabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = GigabytesParaMegabytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)
    
elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = gigabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = terabytesParagigabytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '11'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = terabyteparapetabyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '12'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    ValorConvertido = petabytesparaterabytes(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

else:
    print('error')

