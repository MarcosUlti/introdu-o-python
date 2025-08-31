partida_normal = 5
partida_ranked = 10
partida_especial = 15

jogador1 = "Lucas"
lucas_normal = 3
lucas_ranked = 2
lucas_especial = 1

jogador2 = "Mariana"
mariana_normal = 1
mariana_ranked = 4
mariana_especial = 2

jogador3 = "Rafael"
rafael_normal = 5
rafael_ranked = 0
rafael_especial = 3

pontos_lucas = (lucas_normal * partida_normal) + (lucas_ranked * partida_ranked) + (lucas_especial * partida_especial)
pontos_mariana = (mariana_normal * partida_normal) + (mariana_ranked * partida_ranked) + (mariana_especial * partida_especial)
pontos_rafael = (rafael_normal * partida_normal) + (rafael_ranked * partida_ranked) + (rafael_especial * partida_especial)

print(f"{jogador1} fez {pontos_lucas} pontos!")
print(f"{jogador2} fez {pontos_mariana} pontos!")
print(f"{jogador3} fez {pontos_rafael} pontos!")

if pontos_lucas > pontos_mariana and pontos_lucas > pontos_rafael:
    print(f"O campeão foi {jogador1} com {pontos_lucas} pontos!")
elif pontos_mariana > pontos_lucas and pontos_mariana > pontos_rafael:
    print(f"A campeã foi {jogador2} com {pontos_mariana} pontos!")
elif pontos_rafael > pontos_lucas and pontos_rafael > pontos_mariana:
    print(f"O campeão foi {jogador3} com {pontos_rafael} pontos!")
else:
    print("Empate! Precisa de desempate!")
