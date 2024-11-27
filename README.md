
# Introducción a Blockchain: Consenso y Tipos de Blockchain

Este archivo proporciona una descripción general sobre los mecanismos de consenso y los tipos de blockchain.

## 1. Consenso en Blockchain

El **consenso** es el mecanismo mediante el cual los nodos en una red blockchain acuerdan el estado actual de la cadena. Esto asegura que todos los nodos tengan una copia válida y consistente del registro, manteniendo la integridad del sistema descentralizado.

### **Mecanismos de Consenso más comunes:**

1. **Prueba de Trabajo (Proof of Work, PoW):**
   - Utilizado por Bitcoin.
   - Requiere que los nodos resuelvan problemas matemáticos complejos.
   - Seguridad alta pero consume mucha energía.

2. **Prueba de Participación (Proof of Stake, PoS):**
   - Utilizado por Ethereum 2.0.
   - Los validadores son seleccionados según la cantidad de criptomonedas que poseen y están dispuestos a "apostar".
   - Más eficiente energéticamente.

3. **Prueba Delegada de Participación (Delegated Proof of Stake, DPoS):**
   - Usado por EOS.
   - Los participantes votan por delegados para validar bloques.

4. **Prueba de Autoridad (Proof of Authority, PoA):**
   - Usado en redes privadas.
   - Nodos validadores seleccionados por su identidad y confianza.

5. **Prueba de Capacidad (Proof of Capacity, PoC):**
   - Utiliza espacio de almacenamiento como recurso.
   - Ejemplo: Burstcoin.

6. **Byzantine Fault Tolerance (BFT):**
   - Tolerante a fallos bizantinos en sistemas distribuidos.
   - Variantes: PBFT, Tendermint.

---

## 2. Tipos de Blockchain

Las blockchains se clasifican según su acceso y control.

### **a) Blockchain Pública**
- **Acceso:** Abierta a cualquier persona.
- **Características:** Transparente, descentralizada.
- **Ejemplos:** Bitcoin, Ethereum.
- **Ventajas:** Transparencia, resistencia a la censura.
- **Desventajas:** Escalabilidad limitada, alto consumo energético.

### **b) Blockchain Privada**
- **Acceso:** Restringido a participantes autorizados.
- **Características:** Operada por una entidad central o consorcio.
- **Ejemplos:** Hyperledger Fabric, Corda.
- **Ventajas:** Alto rendimiento, privacidad.
- **Desventajas:** Menor descentralización.

### **c) Blockchain Híbrida**
- **Acceso:** Combina pública y privada.
- **Características:** Control compartido, privacidad selectiva.
- **Ejemplo:** IBM Food Trust.
- **Ventajas:** Transparencia y privacidad equilibradas.
- **Desventajas:** Implementación compleja.

### **d) Blockchain de Consorcio**
- **Acceso:** Controlada por un grupo de organizaciones.
- **Características:** Requiere permisos, colaborativa.
- **Ejemplo:** Quorum (basada en Ethereum).
- **Ventajas:** Eficiencia entre entidades.
- **Desventajas:** Compromiso en descentralización.

---

## Conclusión

El consenso asegura confiabilidad en blockchains, mientras que los tipos de blockchain se adaptan a diferentes necesidades, desde redes públicas abiertas como Bitcoin hasta soluciones privadas empresariales como Hyperledger.

---

# Implementación de un Algoritmo de Prueba de Trabajo (Proof of Work, PoW) en Python

Este proyecto es una implementación básica de un algoritmo de Prueba de Trabajo (Proof of Work, PoW) utilizando Python. 

## ¿Qué es Proof of Work (PoW)?

Proof of Work es un mecanismo de consenso utilizado en redes blockchain para validar bloques de datos y asegurar la cadena contra modificaciones maliciosas. Los nodos participantes (mineros) deben resolver un problema criptográfico para añadir nuevos bloques a la cadena. 

En este ejemplo, la dificultad del problema está determinada por la cantidad de ceros iniciales requeridos en el hash del bloque.

---

## Archivos

- `pow.py`: Contiene la implementación del algoritmo PoW.

---

## Características Principales

1. **Clase `Block`:**
   - Representa un bloque en la cadena con atributos como:
     - `index`: Identificador del bloque.
     - `previous_hash`: Hash del bloque anterior en la cadena.
     - `data`: Datos del bloque (por ejemplo, una transacción).
     - `timestamp`: Marca de tiempo cuando se creó el bloque.
     - `nonce`: Número que se ajusta para cumplir con los requisitos del problema criptográfico.
     - `hash`: Hash del bloque.

2. **Métodos principales:**
   - `calculate_hash`: Genera el hash del bloque utilizando los atributos principales.
   - `mine_block`: Implementa el algoritmo PoW ajustando el `nonce` hasta que el hash cumpla con el requisito de dificultad.

3. **Dificultad:**
   - Se define como el número de ceros iniciales requeridos en el hash.

---

## Requisitos

- **Python 3.6 o superior**
- No se requieren bibliotecas externas, ya que utiliza la biblioteca estándar de Python (`hashlib` y `time`).

---

## Ejemplo de Uso

```bash
python pow.py
```

### Salida esperada:
Dependiendo de la dificultad, obtendrás una salida similar a esta:

```
Minando el bloque con dificultad 4...
¡Bloque minado! Nonce: 54584, Hash: 0000a7b3cde8f9fa69d5f1ef1d6b0a3f93a2be4a6a580c7f7e6f8bfc2e54a5c6

Información del bloque:
Índice: 1
Hash previo: 0000000000000000000000000000000000000000000000000000000000000000
Datos: Transacción: Juan envía 2 BTC a Pedro
Timestamp: 1699998361.0193298
Nonce: 54584
Hash: 0000a7b3cde8f9fa69d5f1ef1d6b0a3f93a2be4a6a580c7f7e6f8bfc2e54a5c6
Tiempo de minería: 2.45 segundos
```

---

## Personalización

- **Dificultad:** Puedes ajustar el valor de `difficulty` en el archivo `pow.py` para aumentar o disminuir la dificultad del problema criptográfico.
- **Datos:** Cambia el valor de `data` para incluir diferentes transacciones u otra información.

---

## Conceptos Importantes

- **Hashing:** Utiliza la función de hash `sha256` de Python para generar un hash seguro.
- **Nonce:** Número que cambia continuamente hasta encontrar un hash válido.
- **Dificultad:** Aumenta el tiempo de minería al requerir más ceros iniciales en el hash.

---
# Implementación de un Algoritmo de Prueba de Participación (Proof of Stake, PoS) en Python

Este proyecto es una implementación básica de un algoritmo de Prueba de Participación (Proof of Stake, PoS) utilizando Python. 

## ¿Qué es Proof of Stake (PoS)?

Proof of Stake es un mecanismo de consenso utilizado en redes blockchain donde los validadores se seleccionan para crear o validar bloques en función de la cantidad de participación (stake) que poseen en la red. Este enfoque reduce significativamente el consumo de energía en comparación con la Prueba de Trabajo (PoW).

---

## Archivos

- `pos.py`: Contiene la implementación del algoritmo PoS.

---

## Características Principales

1. **Clase `Validator`:**
   - Representa un validador en el sistema.
   - Atributos principales:
     - `name`: Nombre del validador.
     - `stake`: Cantidad de participación que posee en la red.
     - `rewards`: Recompensas acumuladas por validar bloques.

2. **Clase `ProofOfStake`:**
   - Gestiona los validadores y realiza la selección proporcional al stake.
   - Atributos y métodos principales:
     - `add_validator`: Agrega un validador a la lista.
     - `select_validator`: Selecciona un validador basado en su participación proporcional.

3. **Proceso de Selección:**
   - Se calcula el stake total en la red.
   - Se genera un punto aleatorio dentro del rango del stake total.
   - Se selecciona al validador cuya participación acumulada alcanza o supera ese punto.

---

## Requisitos

- **Python 3.6 o superior**
- No se requieren bibliotecas externas.

---

## Ejemplo de Uso

```bash
python pos.py
```

### Salida esperada:

Dependiendo de las participaciones y la aleatoriedad, la salida mostrará algo como:

```
Bloque 1 será validado por: Alice
Bloque 2 será validado por: Bob
Bloque 3 será validado por: Alice
Bloque 4 será validado por: Charlie
Bloque 5 será validado por: Alice

Recompensas finales:
Alice: 30 unidades
Bob: 10 unidades
Charlie: 10 unidades
```

---

## Personalización

- **Stake de los validadores:** Cambia los valores de stake para simular diferentes escenarios.
- **Número de bloques:** Ajusta el número de bloques para observar cómo las recompensas se distribuyen con el tiempo.
- **Recompensas:** Modifica las recompensas otorgadas por bloque.

---

## Conceptos Importantes

- **Stake:** Representa la participación de un validador en la red.
- **Selección proporcional:** Los validadores con más stake tienen mayor probabilidad de ser seleccionados, pero no están garantizados.
- **Eficiencia energética:** PoS no requiere cálculos intensivos, lo que lo hace más eficiente que PoW.

---
