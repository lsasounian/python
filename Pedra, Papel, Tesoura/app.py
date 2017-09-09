loose = "Computador vence"
win = "Voce venceu"
vidas = 5
placar = 0
drew = 0
vidas_pc = 7
novamente = 1

while True:
	print ("Para começar, digite as informações abaixo:")
	user = input("Entre com seu nome: ")
	#senha = input("Insira uma senha: ")
	#buscaArquivo = open("accounts.csv","r")
	#for line in buscaArquivo:
	if (novamente == 1):
		print("Acesso liberado")
		print("Bem vindo ao jogo")
		print("Algumas regras...")
		print("Vc começa com", vidas, "vidas")
		print("Se ganhar, ganha uma vida extra")
		print("Se perder, perde uma vida")
		print("Se empatar, nada muda")
		print("----------------------------------")
		print("Nada de letras maiusculas")
		print("Se quiser sair, basta digitar sair")
		print("----------------------------------")
		print("O computador também tem vidas, vença-o")
		while vidas < 0:
			rps = input("Pedra, papel ou tesoura?   ")
			import random
			computador = ("pedra", "papel", "tesoura")
			computador = random.choice(computador)
			#Condições de escolha: pedra
			if (rps == "pedra" and computador == "papel"):
				print("Computador escolheu: ", computador)
				print("Voce perdeu")
				vidas -=1
				print("Agora voce tem", vidas,"vidas")

			if(rps == "pedra" and computador =="pedra"):
				print("Computador escolheu: ", computador)
				print("Empatou!!!")

			if(rps == "pedra" and computador == "tesoura"):
				print("Computador escolheu: ", computador)
				print("Voce ganhou")
				vidas += 1
				print("Agora voce tem",vidas, "vidas")

			#Condições de escolha: papel
			if (rps == "papel" and computador == "tesoura"):
				print("Computador escolheu: ", computador)
				print("Voce perdeu")
				vidas -=1
				print("Agora voce tem", vidas,"vidas")

			if(rps == "papel" and computador =="papel"):
				print("Computador escolheu: ", computador)
				print("Empatou!!!")

			if(rps == "papel" and computador == "pedra"):
				print("Computador escolheu: ", computador)
				print("Voce ganhou")
				vidas += 1
				print("Agora voce tem",vidas, "vidas")

			#Condições de escolha: tesoura
			if (rps == "tesoura" and computador == "pedra"):
				print("Computador escolheu: ", computador)
				print("Voce perdeu")
				vidas -=1
				print("Agora voce tem", vidas,"vidas")

			if(rps == "tesoura" and computador =="tesoura"):
				print("Computador escolheu: ", computador)
				print("Empatou!!!")

			if(rps == "tesoura" and computador == "papel"):
				print("Computador escolheu: ", computador)
				print("Voce ganhou")
				vidas += 1
				print("Agora voce tem",vidas, "vidas")

		print("Suas vidas chegaram a 0 :'(")
		novamente = input("Deseja jogar novamente? Digite 1 para sim, 2 para não")

