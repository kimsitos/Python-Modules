print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
print("Initializing new storage unit: new_discovery.txt")

to_write = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""

fd = open("new_discovery.txt", "w")
print("Storage unit created successfully...")
print("\nInscribing preservation data...")
fd.write(to_write)
fd.close()
print(to_write)
print("\nData inscription complete. Storage unit sealed."
      "\nArchive 'new discovery.txt' ready for long-term preservation.")
