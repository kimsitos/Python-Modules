import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

ID = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")

print(f"\n[STANDARD] Archive status from {ID}: {status}", file=sys.stdout)
print("[ALERT] System diagnostic: Communication channels verified",
      file=sys.stderr)
print("[STANDARD] Data transmission complete", file=sys.stdout)

print("\nThree-channel communication test successful")
