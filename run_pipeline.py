from pathlib import Path
from src.paths import PIPELINE_DIR
from nbclient import NotebookClient
import nbformat

pipeline = [
    "01_import.ipynb",
    "02_cleaning.ipynb",
    #"03_transformation.ipynb",
]

def execute_notebook(notebook_path: Path):
    print(f"\nRunning {notebook_path.name}...")

    with notebook_path.open(encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    client = NotebookClient(
        notebook,
        timeout=None,
        kernel_name="python3",
    )

    client.execute()

    with notebook_path.open("w", encoding="utf-8") as f:
        nbformat.write(notebook, f)

    print(f"Finished {notebook_path.name}")

def main():
    for notebook in pipeline:
        execute_notebook(PIPELINE_DIR / notebook)

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    main()