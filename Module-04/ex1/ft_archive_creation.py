print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
print("Initializing new storage unit: new_discovery.txt")

to_write = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""
try:
    fd = open("new_discovery.txt", "x")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    print(to_write)
    fd.write(to_write)
    fd.close()
    print("\nData inscription complete. Storage unit sealed."
          "\nArchive 'new discovery.txt' ready for long-term preservation.")
except FileExistsError:
    print("Error: new_discovery.txt already exist")
