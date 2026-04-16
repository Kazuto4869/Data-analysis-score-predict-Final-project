import sqlite3
import csv
from pathlib import Path

db_path = "database.sqlite"   # nếu file cùng thư mục với file .py
export_dir = Path("csv_tables")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# xem tất cả bảng
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables:")
for t in tables:
    print("-", t[0])

export_dir.mkdir(exist_ok=True)

print(f"\nExporting tables to: {export_dir.resolve()}")
for (table_name,) in tables:
    if table_name == "sqlite_sequence":
        continue

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    column_names = [description[0] for description in cur.description]

    csv_path = export_dir / f"{table_name}.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)

    print(f"- {table_name}: {len(rows)} rows -> {csv_path}")

def show_table_info(table_name):
    print(f"\n{table_name} columns:")
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = cur.fetchall()
    for column in columns:
        print("-", column[1], f"({column[2]})")

    print(f"\nFirst 5 rows from {table_name}:")
    cur.execute(f"SELECT * FROM {table_name} LIMIT 5")
    rows = cur.fetchall()
    for row in rows:
        print(row)


player_tables = [table_name for (table_name,) in tables if "player" in table_name.lower()]

if player_tables:
    for table_name in player_tables:
        show_table_info(table_name)
else:
    print("\nKhông tìm thấy bảng nào liên quan đến player.")

conn.close()