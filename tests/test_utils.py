import os
import time
import logging
import main

def test_validate_username():
    assert main.validate_username("user_123")
    assert not main.validate_username("us")
    assert not main.validate_username("user!@#")
    assert main.validate_username("UserName30CharsLong___")

def test_log_login_attempt_creates_log():
    log_file = "auth_events.log"

    # Eliminar archivo previo para prueba limpia
    if os.path.exists(log_file):
        os.remove(log_file)

    # Configurar logging explícitamente para que escriba al archivo en el test
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        force=True  # Esto fuerza a reconfigurar logging aunque ya esté configurado
    )

    # Llamar a la función que genera el log
    main.log_login_attempt("127.0.0.1", "logtestuser", "login_failed")

    # Esperar un poco para asegurarse que se escriba el log
    time.sleep(0.2)

    # Verificar que el archivo de log fue creado
    assert os.path.exists(log_file), "No se encontró el archivo de log generado"

    # Opcional: verificar contenido
    with open(log_file, "r") as f:
        content = f.read()
    assert "logtestuser" in content
    assert "login_failed" in content
    assert "127.0.0.1" in content
