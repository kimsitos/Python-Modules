print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")

with open("bkp_classified_data.txt", "r+") as fd:
    to_save = "[CLASSIFIED] New security protocols archived"
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    print(fd.read())

    print("\nSECURE PRESERVATION:")
    print(to_save)
    fd.write("\n" + to_save)


print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
