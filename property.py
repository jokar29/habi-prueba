from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from connector import conn
import json

# Conexión a la base de datos
cursor = conn.cursor()


# Microservicio de consulta porperty
def get_property(filtros):
    # Consulta SQL basada en los filtros
    query = """
        SELECT p.address, p.city, p.price, p.description, year, st.label
        FROM property p
        INNER JOIN status_history s ON p.id = s.property_id
        INNER JOIN status st ON s.status_id = st.id
    """
    query += " AND " + """s.status_id IN( 3, 4, 5 )
        and s.update_date = (SELECT MAX(s.update_date)FROM status_history) """
    conditions = []
    for key, value in filtros.items():
        # Si la clave pertenece a la tabla property, se aplican los filtros
        if key in ['address', 'city', 'price', 'status_id', 'year']:
            conditions.append(f"{key} = '{value}'")
    if conditions:
        query += " AND " + " AND ".join(conditions)

    # Ejecutar la consulta SQL
    cursor.execute(query)
    rows = cursor.fetchall()

    # Se formatea los datos
    resultado = []
    for row in rows:
        if row[0]:
            resultado.append({
                'address': row[0],
                'city': row[1],
                'price': row[2],
                'description': row[3],
                'year': row[4],
                'label': row[5]
            })

    return resultado


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        for key, value in query_params.items():
            query_params[key] = value[0]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        resultado_consulta = get_property(query_params)
        json_data = json.dumps(resultado_consulta, indent=4)
        self.wfile.write(json_data.encode())


# Función para ejecutar el servidor
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
