print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print("Accessing Storage Vault: ancient_fragment.txt")
try:
    fd = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(fd.read())
    fd.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
