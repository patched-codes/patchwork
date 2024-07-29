# Build from source

PatchWork is built using Poetry, a dependency management and packaging tool for Python. To install PatchWork using Poetry, follow these steps:

1. Make sure you have Poetry installed. If you don't have it installed, you can install it by running:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   
   If you are on macOS you can also install poetry using brew:
   
   ```
   brew install poetry
   ```

3. Clone the PatchWork repository:
   ```
   git clone https://github.com/patched-codes/patchwork.git
   ```

4. Navigate to the project directory:
   ```
   cd patchwork
   ```

5. Activate a shell using virtual environment:
   ```
   poetry shell
   ```

6. Install the dependencies using Poetry:
   ```
   poetry install --all-extras
   ```
