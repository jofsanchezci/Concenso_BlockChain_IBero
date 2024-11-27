import random

class Validator:
    """
    Representa un validador en el sistema de Prueba de Participación (PoS).
    """
    def __init__(self, name, stake):
        self.name = name          # Nombre del validador
        self.stake = stake        # Participación (stake) del validador
        self.rewards = 0          # Recompensas obtenidas por validar bloques

    def add_reward(self, amount):
        self.rewards += amount

class ProofOfStake:
    """
    Implementación del mecanismo de selección de validadores basado en PoS.
    """
    def __init__(self):
        self.validators = []      # Lista de validadores

    def add_validator(self, validator):
        """
        Agrega un validador a la lista de validadores.
        """
        self.validators.append(validator)

    def select_validator(self):
        """
        Selecciona un validador en función de su stake.
        """
        total_stake = sum(v.stake for v in self.validators)
        selection_point = random.uniform(0, total_stake)
        cumulative_stake = 0

        for validator in self.validators:
            cumulative_stake += validator.stake
            if cumulative_stake >= selection_point:
                return validator

# Simulación de PoS
if __name__ == "__main__":
    # Crear una lista de validadores
    validators = [
        Validator("Alice", 50),   # Alice tiene 50 unidades de stake
        Validator("Bob", 30),     # Bob tiene 30 unidades de stake
        Validator("Charlie", 20)  # Charlie tiene 20 unidades de stake
    ]

    # Inicializar el sistema PoS
    pos_system = ProofOfStake()
    for validator in validators:
        pos_system.add_validator(validator)

    # Simular la selección de validadores para 5 bloques
    for i in range(5):
        selected_validator = pos_system.select_validator()
        print(f"Bloque {i+1} será validado por: {selected_validator.name}")
        selected_validator.add_reward(10)  # Recompensa por validar un bloque

    # Mostrar las recompensas finales de los validadores
    print("\nRecompensas finales:")
    for validator in validators:
        print(f"{validator.name}: {validator.rewards} unidades")
