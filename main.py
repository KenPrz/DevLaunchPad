import os
import subprocess
import platform

CONFIG_FILE = 'config.txt'

def list_folders(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return folders

def open_vscode(folder_path):
    vscode_path = r'C:\Users\UserName\AppData\Local\Programs\Microsoft VS Code\code.exe'  # Adjust this path to your VS Code installation
    subprocess.run([vscode_path, '.'], cwd=folder_path)


def launch_environment(environment, folder_path):
    # Determine the command to open a new terminal based on the operating system
    if platform.system() == 'Windows':
        terminal_command = 'start'
    elif platform.system() == 'Linux':
        terminal_command = 'gnome-terminal'  # Adjust based on your Linux terminal
    elif platform.system() == 'Darwin':
        terminal_command = 'open -a Terminal'

    if environment == 'node':
        subprocess.run(['npm', 'run', 'dev'], cwd=folder_path)
    elif environment == 'laravel':
        subprocess.run(['php', 'artisan', 'serve'], cwd=folder_path)
    elif environment == 'mixed':
        subprocess.run([terminal_command, 'cmd', '/k', 'php artisan serve'], cwd=folder_path)
        subprocess.run([terminal_command, 'cmd', '/k', 'npm run dev'], cwd=folder_path)

def save_folder_path(path):
    with open(CONFIG_FILE, 'w') as config_file:
        config_file.write(path)

def load_folder_path(dev_folder):
    config_path = os.path.join(dev_folder, CONFIG_FILE)
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            return config_file.read().strip()
    return None

def main():
    dev_folder = 'D:\\Dev'
    saved_folder = load_folder_path(dev_folder)

    if saved_folder:
        full_path = os.path.join(dev_folder, saved_folder)
        print(f"Last opened folder: {full_path}")
        open_vscode(full_path)
        environment = input("Select the dev environment (node/laravel/mixed): ").lower()
        launch_environment(environment, full_path)
    else:
        folders = list_folders(dev_folder)

        print("Folders in dev folder:")
        for i, folder in enumerate(folders, start=1):
            print(f"{i}. {folder}")

        selected_index = int(input("Enter the number of the folder you want to open: ")) - 1
        selected_folder = os.path.join(dev_folder, folders[selected_index])

        open_vscode(selected_folder)
        save_folder_path(os.path.relpath(selected_folder, dev_folder))

        environment = input("Select the dev environment (node/laravel/mixed): ").lower()
        launch_environment(environment, selected_folder)

if __name__ == "__main__":
    main()
