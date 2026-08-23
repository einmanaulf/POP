import sqlite3
from pathlib import Path

db_paths = [
    Path(".venv/instance/app.db"),
    Path(".venv/var/app-instance/app.db"),
    Path("instance/app.db"),
]

tables_to_check = ["user", "task", "liste", "resource", "protocole", "argent", "sub_task"]

for db_path in db_paths:
    print("=" * 80)
    print(db_path.resolve())
    print("Existe :", db_path.exists())
    print("Taille :", db_path.stat().st_size if db_path.exists() else "N/A")

    if not db_path.exists() or db_path.stat().st_size == 0:
        print("Base vide ou absente.")
        continue

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    tables = [row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()]

    print("Tables :", tables)

    for table in tables_to_check:
        if table in tables:
            count = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"{table}: {count}")
        else:
            print(f"{table}: ABSENTE")

    if "task" in tables:
        print("--- Aperçu des 10 dernières tâches ---")
        rows = cur.execute(
            "SELECT id, name, plan_date, due_date, is_done FROM task ORDER BY created_at DESC LIMIT 10"
        ).fetchall()
        for row in rows:
            print(row)

    if "liste" in tables:
        print("--- Listes ---")
        rows = cur.execute(
            "SELECT id, name, task_ids, task_orders FROM liste ORDER BY id"
        ).fetchall()
        for row in rows:
            print(row)

    con.close()
