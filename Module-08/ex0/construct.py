import sys
import os
import site

virtual_env = os.getenv('VIRTUAL_ENV')

print("\nMATRIIX STATUS:",
      "Welcome to the construct" if virtual_env else "You're still plugged in")

print("\nCurrent Python:", sys.executable)
print(f"Virtual Environment: {os.path.basename(sys.prefix)}"
      f"\nEnvironment Path: {sys.prefix}" if virtual_env else
      'Virtual Environment: None detected')

if not virtual_env:
    print("\nWARNING: You're in the global environment!"
          "\nThe machines can see everything you install."
          "\nTo enter the construct, run:"
          "\npython3 -m venv matrix_env"
          "\nsource matrix_env/bin/activate # On Unix"
          "\nmatrix_env"
          "\nScripts"
          "\nactivate # On Windows"
          "\n\nThen run this program again.")
else:
    print("\nSUCCESS: You're in an isolated environment!"
          "\nSafe to install packages without affecting"
          "\nthe global system."
          "\n\nPackage installation path:"
          f"\n{site.getsitepackages()[0]}")
