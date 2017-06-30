def NewYearChaos(queue):
	ans=0
	lastIndex = len(queue) - 1
	#Passando por todos os elementos do array
	for i in xrange(0, lastIndex):
		#checa se o valor do numero nesta posicao menos seu indice e maior que dois. se sim, e muito caotico
		if (queue[i] - (i+1)) > 2:
			return "muito caotico para analise"
			
		#compara o valor atual com os dois a frente. Se os dois forem menores que o atual, houve dois subornos. se apenas um , houve um suborno. se nenhum entao nao houve nenhum 
		for j in xrange(i, min(lastIndex+1,i+3)):
			if queue[i]>q[j]:
				ans+=1	
	
	return "de pelo menos "+str(ans)+" subornos"

#LENDO A QUANTIDADE DE CASOS TESTES
print "Digite a quantidade de casos de Teste: "
T = int(raw_input().strip())

for a0 in xrange(T):
	print "Digite o tamanho do caso de teste de numero  " + str(a0+1)
	#LE O TAMANHO DO CASO DE TESTE ANALISADO NAQUELE INSTANTE
	n = int(raw_input().strip())
	#LE OS VALORES DAQUELE CASO DE TESTE EM ESPECIFICO, SEPARADOS POR ESPACO
	print "Digite os valores do caso de teste separados por espaco"
	q = map(int,raw_input().strip().split(' '))
	print "Esse caso de teste possui um resultado "+str(NewYearChaos(q))
