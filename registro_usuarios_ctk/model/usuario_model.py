class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar  # ruta relativa en assets/

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []  # lista de Usuario
        # Cargar datos de ejemplo para la Fase 1
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        # Añadimos algunos usuarios de prueba para que la vista los muestre
        # Nombres con acentos para parecerse a la imagen de referencia
        try:
            self.anadir(Usuario("Ana García", 28, "femenino", "avatar1.png"))
            self.anadir(Usuario("Luis Pérez", 35, "masculino", "avatar2.png"))
            self.anadir(Usuario("Sofía Romero", 22, "femenino", "avatar3.png"))
        except Exception:
            # Si por alguna razón los validadores fallan, volver a ascii simple
            self.anadir(Usuario("Ana Garcia", 28, "femenino", "avatar1.png"))
            self.anadir(Usuario("Luis Perez", 35, "masculino", "avatar2.png"))
            self.anadir(Usuario("Sofia Romero", 22, "femenino", "avatar3.png"))

    def listar(self):
        return list(self._usuarios)

    def anadir(self, usuario: Usuario):
        if not usuario.nombre.strip():
            raise ValueError("Nombre no puede estar vacío")
        if not (0 <= usuario.edad <= 100):
            raise ValueError("Edad debe estar entre 0 y 100")
        if usuario.genero not in ["masculino", "femenino", "otro"]:
            raise ValueError("Género no válido")
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
        else:
            raise IndexError("Índice fuera de rango")

    def actualizar(self, indice: int, usuario_actualizado: Usuario):
        if 0 <= indice < len(self._usuarios):
            self._usuarios[indice] = usuario_actualizado
        else:
            raise IndexError("Índice fuera de rango")

    def guardar_csv(self, ruta: str = "usuarios.csv"):
        import csv
        try:
            with open(ruta, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "edad", "genero", "avatar"])
                for u in self._usuarios:
                    writer.writerow([u.nombre, u.edad, u.genero, u.avatar])
        except Exception as e:
            raise Exception(f"Error al guardar CSV: {e}")

    def cargar_csv(self, ruta: str = "usuarios.csv"):
        import csv
        # Intentar abrir el CSV; si no existe, no hacer nada
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                # Saltar la cabecera si existe
                next(reader, None)
                # Limpiar la lista actual antes de repoblarla
                self._usuarios.clear()
                for i, row in enumerate(reader, start=1):
                    try:
                        if not row:
                            continue
                        if len(row) != 4:
                            # fila con formato inesperado, la saltamos
                            continue
                        nombre, edad_s, genero, avatar = row
                        edad = int(edad_s)
                        # Añadir usando validaciones del método anadir
                        self.anadir(Usuario(nombre, edad, genero, avatar))
                    except Exception:
                        # Saltar filas corruptas o con datos inválidos
                        continue
        except FileNotFoundError:
            # No existe el archivo: nada que cargar
            return
        except Exception as e:
            # Propagar errores inesperados para que el controlador los maneje
            raise Exception(f"Error al cargar CSV: {e}")