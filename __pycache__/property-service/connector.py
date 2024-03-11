import mysql.connector

# Configuración de conexión
config = {
  'user': 'pruebas',
  'password': 'VGbt3Day5R',
  'host': '3.138.156.32',
  'database': 'habi_db',
  'port': 3309,
  'raise_on_warnings': True
}

# Establecer la conexión
try:
    conn = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos MySQL: {err}")
