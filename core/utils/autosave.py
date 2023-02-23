import sqlite3


def save(data: list[tuple[str, str]], file: str = "autosave.db"):
    db = sqlite3.connect(file)
    values = ",\n".join([f"({repr(chunk[0])}, {repr(chunk[1])})" for chunk in data])

    db.execute("CREATE TABLE IF NOT EXISTS saves (path STRING, [data] BLOB)")
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_title ON saves (path)")
    db.execute(
        f"INSERT OR REPLACE INTO saves (path, data)\nVALUES\n{values}"
    )
    db.commit()
