
import subprocess 
print("Analizando dependencias con Bandit...") 
subprocess.run(["bandit", "-r", "src/"]) 