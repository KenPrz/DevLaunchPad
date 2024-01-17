# DevLaunchPad

DevLaunchPad is a Python script that allows you to easily navigate and launch your development projects from the terminal. It provides a convenient way to open folders in Visual Studio Code and run specific development environments.

## Features

- List and select folders within your development directory.
- Open selected folder in Visual Studio Code.
- Choose a development environment:
  - Run `npm run dev` for Node projects.
  - Run `php artisan serve` for Laravel projects.
  - Run both for mixed projects.

## Prerequisites

- Python 3.x
- Visual Studio Code installed and available in the system's PATH.

## Usage

1. Clone or download the DevLaunchPad repository.

2. Open a terminal and navigate to the DevLaunchPad directory:

    ```bash
    cd path/to/DevLaunchPad
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. Follow the prompts to select a folder, open it in Visual Studio Code, and choose a development environment.

## Configuration

- The script saves the selected folder path in a `config.txt` file.

## Troubleshooting

- If you encounter issues opening Visual Studio Code, ensure that the `code` command is in your system's PATH or provide the full path in the script.