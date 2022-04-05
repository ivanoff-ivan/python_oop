from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for cd in attacker.card_repository.cards:
                cd.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for cd in enemy.card_repository.cards:
                cd.damage_points += 30

        attacker.health += sum([cd.health_points for cd in attacker.card_repository.cards])
        enemy.health += sum([cd.health_points for cd in enemy.card_repository.cards])

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)
