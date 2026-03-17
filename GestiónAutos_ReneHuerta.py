from abc import ABC, abstractmethod #importamos las librerías necesarias

class tipo_motor: #definimos la clase tipo de motor
  Variacion = {
      "gasolina": 1.00,
      "hibrido": 1.15,
      "electrico": 1.25
  }

  def __init__(self, tipo_motor_str): #string porque podemos usar 3 palabras diferentes
    self.tipo_motor_str = tipo_motor_str

  def get_factor(tipo_motor_str): #get es para que python busque las palabras clave
    return tipo_motor.Variacion.get(tipo_motor_str.lower(), 1.00) #Aquí el lower es para evitar errores cuando el usuario teclee mayúsculas o minúsculas

class vehiculo: #Definimos nuestra clase como vehículo

  def __init__(self, marca, modelo, año, costo_base, tipo_motor): #definimos el constructor y sus atributos
    self.marca = marca #atributo de marca
    self.modelo = modelo #Atributo de modelo
    self.año = año #atributo de año
    self.costo_base = costo_base #atributo del costo
    self.tipo_motor = tipo_motor #atributo del tipo de motor (string 'gasolina', 'hibrido', 'electrico')

  def calcular_costo(self): #definimos el método calcular costo
    # This method should be abstract as it's implemented by subclasses
    # But for now, we'll keep it as a placeholder if not abstract
    return self.costo_base # Base implementation, should be overridden

  def mostrar_detalles(self): #definimos el método mostrar detalles del vehículo
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Año: {self.año}")
    print(f"Tipo de motor: {self.tipo_motor}")
    # Correctly format costo_base, it should be a float from solicitar_numero
    print(f"Costo Base: ${self.costo_base:.2f}")

class auto(vehiculo): #definimos la clase carro que hereda de vehículo

  def __init__(self, marca, modelo, año, costo_base, num_puertas, tipo_motor_str): #Constructor de la clase auto
    super().__init__(marca, modelo, año, costo_base, tipo_motor_str) #usamos string ya que al poder usar 3 palabras diferentes, de esta manera evitamos errores del usuario
    self.num_puertas = num_puertas #atributo de número de puertas del vehículo

  def calcular_costo(self): #definimos el método calcular costo
    subtotal = self.costo_base + (self.costo_base * 0.15) #Ajustamos el 0.15 para tener un margen de ganancias
    factor_motor = tipo_motor.get_factor(self.tipo_motor) #Busca de manera segura según el tipo de motor para que se ajuste en automático el costo
    return subtotal * factor_motor

  def mostrar_detalles(self): #definimos el método mostrar detalles del vehículo
    super().mostrar_detalles() #usamos el constructor de la clase padre
    print(f"Número de Puertas: {self.num_puertas}")

class camion(vehiculo):

  def __init__(self, marca, modelo, año, costo_base, tipo_motor_str, capacidad_carga): #constructor de la clase camion
    super().__init__(marca, modelo, año, costo_base, tipo_motor_str)
    self.capacidad_carga = capacidad_carga

  def calcular_costo(self):
    subtotal = self.costo_base + (self.costo_base * 0.15)
    factor_motor = tipo_motor.get_factor(self.tipo_motor)
    return subtotal * factor_motor

  def mostrar_detalles(self):
    super().mostrar_detalles()
    print(f"Capacidad de Carga: {self.capacidad_carga}")

class Motocicleta(vehiculo):
  def __init__(self, marca, modelo, año, costo_base, tipo_motor_str, cilindrada): #Constructor de la clase moto
    super().__init__(marca, modelo, año, costo_base, tipo_motor_str) 
    self.cilindrada = cilindrada

  def calcular_costo(self):
    subtotal = self.costo_base + (self.costo_base * 0.15)
    factor_motor = tipo_motor.get_factor(self.tipo_motor)
    return subtotal * factor_motor

  def mostrar_detalles(self):
    super().mostrar_detalles()
    print(f"Cilindrada: {self.cilindrada}")


def solicitar_dato_no_vacio(mensaje): #aquí le estamos indicando al usuario que no puede dejar el campo vacío en el input
    while True:
        dato = input(mensaje).strip() #con la función strip se borran espacios en blanco y saltos de linea
        if dato:
            return dato
        print("Error: El campo no puede estar vacío.")

def solicitar_numero(mensaje): #Con esto validamos que el usuario use un valor numérico válido
    while True:
        try:
            valor = float(input(mensaje)) # Convert to float here
            return valor
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido.")

def menu(): #menú para interacción del usuario
  autos = [] #usaremos un diccionario
  while True:
    print("Autogesión AMERIKE")
    print("1. Registrar auto")
    print("2. Registrar camion")
    print("3. Registrar motocicleta")
    print("4. Mostrar vehículos")
    print("5. Calcular costos")
    print("6. Buscar vehículo por modelo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1": #le indicamos al usuario que registre un auto
      marca_input = solicitar_dato_no_vacio("Ingrese la marca del auto: ")
      modelo_input = solicitar_dato_no_vacio("Ingrese el modelo del auto: ")
      año_input = solicitar_numero("Ingrese el año del auto: ")
      costo_base_input = solicitar_numero("Ingrese el costo base del auto: ")
      num_puertas_input = solicitar_numero("Ingrese el número de puertas del auto: ")
      tipo_motor_input = solicitar_dato_no_vacio("Ingrese el tipo de motor (gasolina, hibrido, electrico): ") # Assuming 'combustion' was meant to be 'tipo_motor'

      nuevo_auto = auto(marca_input, modelo_input, año_input, costo_base_input, num_puertas_input, tipo_motor_input)
      autos.append(nuevo_auto)
      print("Auto registrado exitosamente!")

    elif opcion == "2": #le indicamos al usuario que registre un camion
      marca_input = solicitar_dato_no_vacio("Ingrese la marca del camión: ")
      modelo_input = solicitar_dato_no_vacio("Ingrese el modelo del camión: ")
      año_input = solicitar_numero("Ingrese el año del camión: ")
      costo_base_input = solicitar_numero("Ingrese el costo base del camión: ")
      capacidad_carga_input = solicitar_numero("Ingrese la capacidad de carga del camión: ")
      tipo_motor_input = solicitar_dato_no_vacio("Ingrese el tipo de motor (gasolina, hibrido, electrico): ")

      nuevo_camion = camion(marca_input, modelo_input, año_input, costo_base_input, tipo_motor_input, capacidad_carga_input)
      autos.append(nuevo_camion)
      print("Camión registrado exitosamente!")

    elif opcion == "3": #le indicamos al usuario que registre una moto
      marca_input = solicitar_dato_no_vacio("Ingrese la marca de la motocicleta: ")
      modelo_input = solicitar_dato_no_vacio("Ingrese el modelo de la motocicleta: ")
      año_input = solicitar_numero("Ingrese el año de la motocicleta: ")
      costo_base_input = solicitar_numero("Ingrese el costo base de la motocicleta: ")
      cilindrada_input = solicitar_numero("Ingrese la cilindrada de la motocicleta: ")
      tipo_motor_input = solicitar_dato_no_vacio("Ingrese el tipo de motor (gasolina, hibrido, electrico): ")

      nueva_motocicleta = Motocicleta(marca_input, modelo_input, año_input, costo_base_input, tipo_motor_input, cilindrada_input)
      autos.append(nueva_motocicleta)
      print("Motocicleta registrada exitosamente!")

    elif opcion == "4": #aquí el usuario quiere mostrar los vehículos registrados
      if not autos:
        print("No hay vehículos registrados.")
      else:
        print("\n--- Vehículos Registrados ---")
        for v in autos:
          v.mostrar_detalles() # Changed from v.mostrar_info() to v.mostrar_detalles()
          print("-----------------------------")

    elif opcion == "5": #aquí el usuario quiere calcular los costos
      if not autos:
            print("No hay vehículos registrados.")
      else:
        print("\n--- Costos de Vehículos ---")
        for v in autos:
          costo_final = v.calcular_costo()
          print(f"{v.marca} {v.modelo}: Costo Total con gestión: ${costo_final:.2f}")
        print("-----------------------------")

    elif opcion == "6": #aquí el usuario quiere buscar un vehículo por modelo
      modelo_buscar = solicitar_dato_no_vacio("Ingrese el modelo del vehículo que desea buscar: ")
      encontrado = False
      for v in autos:
            if v.modelo.lower() == modelo_buscar.lower(): # usamos de nuevo lower para evitar errores en la búsqueda por mayúsculas o minúsculas
                v.mostrar_detalles()
                encontrado = True
                break
      if not encontrado:
          print("Vehículo no encontrado, intenta registrarlo primero.")

    elif opcion == "7": #aquí el usuario quiere salir del programa
      print("¡Hasta luego!")
      break

    else:
      print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()