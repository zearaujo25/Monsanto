def NewYearChaos(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    
    # verifica se as interaoes sao caoticas 
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # aplicando o bubble sort para achar a resposta
    for i in xrange(0, lastIndex):
        for j in xrange(0, lastIndex):
            if queue[j] > queue[j+1]:
                queue[j], queue[j+1] = queue[j+1], queue[j]
                swaps += 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break
    return swaps
def NewYearChaos2(queue):
	ans=0
	lastIndex = len(queue) - 1
	#Passando por todos os elementos do array
	for i in xrange(0, lastIndex):
		#checa se o valor do numero nesta posicao menos seu indice e maior que dois. se sim, e muito caotico
		if (queue[i] - (i+1)) > 2:
			return "Too chaotic"
		
		for j in xrange(i, min(lastIndex+1,i+3)):
			if queue[i]>q[j]:
				ans+=1
	
	return ans

#LENDO A QUANTIDADE DE CASOS TESTES
print "Digite a quantidade de casos de Teste: "
T = int(raw_input().strip())

for a0 in xrange(T):
	print "Digite o tamanho do caso de teste de numero  " + str(a0+1)
	#LE O TAMANHO DO CASO DE TESTE ANALISADO NAQUELE INSTANTE
	n = int(raw_input().strip())
	#LE OS VALORES DAQUELE CASO DE TESTE EM ESPECIFICO, SEPARADOS DOR ESPACO
	print "Digite os valores do caso de teste separados por espaco"
	q = map(int,raw_input().strip().split(' '))
	#
	print "Esse caso de teste possui "+str(NewYearChaos2(q))+" subornos"