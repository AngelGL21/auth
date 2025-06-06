
import bcrypt 
password = b"clave_segura" 
hashed = bcrypt.hashpw(password, bcrypt.gensalt()) 
print("Hash generado:", hashed) 
# Verificación 
assert bcrypt.checkpw(password, hashed) 