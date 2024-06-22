# Build from source

PatchWork is built using Poetry, a dependency management and packaging tool for Python. To install PatchWork using Poetry, follow these steps:

1. Make sure you have Poetry installed. If you don't have it installed, you can install it by running:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the PatchWork repository:
   ```
   git clone https://github.com/patched-codes/patchwork.git
   ```

3. Navigate to the project directory:
   ```
   cd patchwork
   ```

4. Activate a shell using virtual environment:
   ```
   poetry shell
   ```

5. Install the dependencies using Poetry:
   ```
   poetry install --all-extras
   ```
