import os
import shutil
import winshell

# Directory to scan
scan_directory = "G:/games"
# Directory to create shortcuts
shortcut_directory = "G:/game_shortcuts"

# Function to scan the directory and create shortcuts
def create_shortcuts(directory):
    # Create shortcut directory if it doesn't exist
    if not os.path.exists(shortcut_directory):
        os.makedirs(shortcut_directory)

    # Iterate through each file in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is a .exe file
            if file.endswith(".exe"):
                # Exclude uninstallers and settings
                if "uninstall" not in file.lower() and "settings" not in file.lower() and "unin" not in file.lower():
                    # Create shortcut
                    game_exe_path = os.path.join(root, file)
                    shortcut_name = file.replace(".exe", ".lnk")
                    try:
                        winshell.CreateShortcut(
                            Path=os.path.join(shortcut_directory, shortcut_name),
                            Target=game_exe_path
                        )
                        print(f"Shortcut created for: {game_exe_path}")
                    except Exception as e:
                        print(f"Error creating shortcut for {game_exe_path}: {e}")

# Call the function to create shortcuts
print("Creating shortcuts...")
create_shortcuts(scan_directory)
print("Shortcut creation complete.")
