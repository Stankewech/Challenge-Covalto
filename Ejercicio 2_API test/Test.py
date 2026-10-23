import requests
import time

def test_rick_and_morty_api():
    # Consultamos a los dos personajes principales
    url = "https://rickandmortyapi.com/api/character/1,2"
    
    start_time = time.time()
    response = requests.get(url)
    response_time = time.time() - start_time
    
    # 1. Validación de Status Code
    assert response.status_code == 200, f"Error: Status code inesperado {response.status_code}"
    
    data = response.json()
    
    for character in data:
        # 2. Validación de tipos de datos 
        assert isinstance(character['id'], int), "El ID debe ser un entero"
        assert isinstance(character['name'], str), "El nombre debe ser una cadena de texto"
        assert isinstance(character['status'], str), "El status debe ser una cadena de texto"
        
        # 3. Validación de vivos
        status = character['status']
        assert status == 'Alive', f"El personaje {character['name']} no está vivo. Status actual: {status}"

    # Resultados esperados
    print("TEST COMPLETADO CON ÉXITO")
    print(f"Tiempo de respuesta: {response_time:.4f} segundos")
    print(f"Status Code: {response.status_code}")
    print(f"Personajes (Vivos): {[c['name'] for c in data]}")

if __name__ == "__main__":
    test_rick_and_morty_api()