arquivo = open('numeros.txt')
numeros = str(arquivo.read()).split()
numeros = [int(g) for g in numeros]
print(numeros)

def print_zeros(binario):
    binario = binario[2:]
    n_zeros = str("0"*(8-len(binario)))
    binario = str(binario)
    return n_zeros+binario

def comp_a_um_negativo(binario):
    binario1 = binario[3:]
    binario2 = ''
    for i in binario1:
        if i == '0':
            binario2 += '1'
        else:
            binario2 += '0'
    
    n_uns = str("1"*(8-len(binario2)))

    return n_uns+binario2

def comp_a_um(binario):
    binario1 = binario[2:]
    binario2 = ''
    for i in binario1:
        if i == '0':
            binario2 += '1'
        else:
            binario2 += '0'
    
    n_uns = str("1"*(8-len(binario2)))

    return n_uns+binario2

def comp_a_dois(binario2):
    binario3 = ''
    binario4 = ''
    if(binario2[7] == "0"):
        for i in range(0,len(binario2)-1):
            if(i != 7):
                binario3 += binario2[i]
        binario3 += "1"
        return binario3
    
    x = len(binario2) - 1
    while (x>=0):
        if (binario2[x]=="1"):
            binario3 += "0"
        else:
            break
        x = x - 1

    binario3 += "1"
    for i in range(len(binario2)-len(binario3)-1,-1,-1):
        binario3 += binario2[i]
    for i in range(len(binario2)-1,-1,-1):
        binario4 += binario3[i]
    return binario4
        
        

def soma(lista):
    print("-"*30, "SOMA", "-"*30)
    for i in range(0,len(lista)-1):
        if(i%2==0):
            a = lista[i]
            b = lista[i+1]
            somaint = a+b
            bin_a = bin(a)
            bin_b = bin(b)
            bin_soma = bin(somaint)
            print("Soma decimal: ",a," + ",b," = ",somaint,"\nSoma binária: ",print_zeros(bin_a)," + ",print_zeros(bin_b)," = ",print_zeros(bin_soma),"\n\n")

def subtração(lista):
    print("\n","-"*30, "SUBTRAÇÃO", "-"*30)
    for i in range(0,len(lista)-1):
        if(i%2==0):
            a = lista[i]
            b = lista[i+1]
            b_neg = 0-b
            subint = a-b
            bin_a = bin(a)
            bin_b = bin(b)
            bin_b_neg = bin(b_neg)
            bin_sub = bin(subint)
            if(subint >= 0):
                print("Subtração decimal: ",a," - ",b," = ",a," + (-",b,") = ",subint,"\nSubtração binária(usando complemento a 2):\n",print_zeros(bin_a)," - ",print_zeros(bin_b)," = ",print_zeros(bin_a)," + ",comp_a_dois(comp_a_um_negativo(bin_b_neg))," = ",print_zeros(bin_sub),"\n\n")
            if(subint < 0):
                print("Subtração decimal: ",a," - ",b," = ",a," + (-",b,") = ",subint,"\nSubtração binária(usando complemento a 2):\n",print_zeros(bin_a)," - ",print_zeros(bin_b)," = ",print_zeros(bin_a)," + ",comp_a_dois(comp_a_um_negativo(bin_b_neg))," = ",comp_a_dois(comp_a_um_negativo(bin_sub)),"\n\n")

soma(numeros)

subtração(numeros)