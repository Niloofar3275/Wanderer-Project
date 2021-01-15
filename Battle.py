from random import *

import time




def battle(player, monster, monsters, monsters_move):


	
	player.get_monster_stat(monster)


	# determines the attacker
	if monsters_move:
		attacker = monster
		defender = player

	else:
		attacker = player
		defender = monster


	player.fighting = True

	while player.attack:


		player.attack = False
		#strike value of attacker and defender
		attacker_sv = randint(1,6) * 2 + attacker.SP
		defender_sv = randint(1,6) * 2 + defender.SP

		if attacker_sv > defender.DP:

			defender.HP = defender.HP - (attacker_sv - defender.DP)

			if defender.HP <= 0:
				defender.dead()
				player.fighting = False


		if defender_sv > attacker.DP and player.fighting:

			attacker.HP = attacker.HP - (defender_sv - attacker.DP)

			if attacker.HP <= 0:

				attacker.dead()
				player.fighting = False

	# checks if fight is finished
	if not player.fighting:

		# if hero won the battle
		if not monster.alive:

			player.level_up()
			if not monsters.monsters[0].alive and not monsters.monsters[1].alive:
				#if boss and key bearer die call next level for hero and monsters
				monsters.next_level()
				player.next_level()


		# if monster won
		else:

			# resets monsters level
			restart = True
			monsters.next_level(restart)



	



	







