import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0  # Número que se incrementará para resolver el problema
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calcula el hash del bloque combinando los atributos principales.
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Implementación de la prueba de trabajo.
        Resuelve un problema encontrando un hash que comience con un número de ceros igual a `difficulty`.
        """
        target = "0" * difficulty
        print(f"Minando el bloque con dificultad {difficulty}...")
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"¡Bloque minado! Nonce: {self.nonce}, Hash: {self.hash}")

# Ejemplo de uso
if __name__ == "__main__":
    # Datos para el bloque
    index = 1
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    data = "Transacción: Juan envía 2 BTC a Pedro"
    difficulty = 4  # Número de ceros iniciales requeridos en el hash

    # Crear y minar un bloque
    new_block = Block(index, previous_hash, data)
    start_time = time.time()
    new_block.mine_block(difficulty)
    end_time = time.time()

    print("\nInformación del bloque:")
    print(f"Índice: {new_block.index}")
    print(f"Hash previo: {new_block.previous_hash}")
    print(f"Datos: {new_block.data}")
    print(f"Timestamp: {new_block.timestamp}")
    print(f"Nonce: {new_block.nonce}")
    print(f"Hash: {new_block.hash}")
    print(f"Tiempo de minería: {end_time - start_time:.2f} segundos")
