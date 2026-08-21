import json
import shutil
from pathlib import Path

ALUNOS_JSON = Path("alunos.json")
#comentario TODO


def criar_entregas(tarefa: str):
    """

    Uso:
        python criar_entregas.py 02-variaveis-e-prints
    """
    tarefa_path = Path("tarefas") / tarefa
    notebook_base = tarefa_path / "notebook.ipynb"
    entregas_path = tarefa_path / "entregas"

    if not tarefa_path.exists():
        print(f"Tarefa não encontrada: {tarefa_path}")
        return

    alunos = json.loads(ALUNOS_JSON.read_text(encoding="utf-8"))

    for aluno in alunos:
        nome = aluno["nome"]
        pasta = entregas_path / nome
        pasta.mkdir(parents=True, exist_ok=True)

        gitkeep = pasta / ".gitkeep"
        if gitkeep.exists():
            gitkeep.unlink()

        if notebook_base.exists():
            destino = pasta / "notebook.ipynb"
            if not destino.exists():
                shutil.copy(notebook_base, destino)
                print(f"  criado: {destino}")
            else:
                print(f"  já existe: {destino}")
        else:
            (pasta / ".gitkeep").touch()
            print(f"  pasta criada (sem notebook base): {pasta}")

    print(f"\nEntregas criadas para {len(alunos)} alunos em '{tarefa_path}'.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python criar_entregas.py <nome-da-tarefa>")
        print("Exemplo: python criar_entregas.py 02-variaveis-e-prints")
        sys.exit(1)

    criar_entregas(sys.argv[1])
