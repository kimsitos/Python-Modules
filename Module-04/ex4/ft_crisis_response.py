print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

print("\nCRISIS ALERT: access to 'lost_archive.txt...")
try:
    with open("lost_archive.txt", "r") as fd:
        print(f"SUCCESS: Archive recovered - ``{fd.read()}''")
        print("STATUS: Normal operations resumed")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix\n"
          "STATUS: Crisis handled, system stable")


print("\nCRISIS ALERT: access to 'corrupted_archive.txt'...")
try:
    with open("corrupted_archive.txt", "r") as fd:
        print(f"SUCCESS: Archive recovered - ``{fd.read()}''")
        print("STATUS: Normal operations resumed")
except PermissionError:
    print("RESPONSE: Security protocols deny access\n"
          "STATUS: Crisis handled, system maintained")


print("\nCRISIS ALERT: Attempting access to 'standard_archive.txt'...")
try:
    to_write = "[CLASSIFIED] i want hamburguer"
    with open("security_protocols.txt", "w") as fd:
        fd.write(to_write)
        print(f"SUCCESS: Archive write - ``{to_write}''")
        print("STATUS: Normal operations resumed")
except PermissionError:
    print("RESPONSE: Security protocols deny access\n"
          "STATUS: Crisis handled, system maintained")


print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as fd:
        print(f"SUCCESS: Archive recovered - ``{fd.read()}''")
        print("STATUS: Normal operations resumed")
except (FileNotFoundError, PermissionError):
    print("RESPONSE: Security protocols deny access or"
          "Archive not found in storage matrix\n"
          "STATUS: Crisis handled, system maintained")


print("\nAll crisis scenarios handled successfully. Archives secure.")
