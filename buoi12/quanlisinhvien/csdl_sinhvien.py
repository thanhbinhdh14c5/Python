import sqlite3
import sys
from contextlib import closing
from pathlib import Path


if getattr(sys, "frozen", False):
    DATABASE_PATH = Path(sys.executable).resolve().parent / "quanly_sinhvien.db"
else:
    DATABASE_PATH = Path(__file__).resolve().with_name("quanly_sinhvien.db")

DEMO_STUDENTS = (
    ("SV001", "Nguyen Minh Anh", "Nu", "2005-03-14", "CNTT1", "0901234567", "minhanh@example.com", 8.6),
    ("SV002", "Tran Quoc Bao", "Nam", "2005-07-22", "CNTT1", "0912345678", "quocbao@example.com", 7.8),
    ("SV003", "Le Thu Ha", "Nu", "2004-11-08", "CNTT2", "0923456789", "thuha@example.com", 9.1),
    ("SV004", "Pham Duc Huy", "Nam", "2005-01-30", "CNTT2", "0934567890", "duchuy@example.com", 6.9),
    ("SV005", "Vo Ngoc Linh", "Nu", "2004-09-17", "QTKD1", "0945678901", "ngoclinh@example.com", 8.2),
    ("SV006", "Do Tuan Kiet", "Nam", "2005-05-05", "QTKD1", "0956789012", "tuankiet@example.com", 7.4),
)


class StudentDatabase:
    def __init__(self, path: Path = DATABASE_PATH) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._create_table()
        self._add_demo_students()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection

    def _create_table(self) -> None:
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    date_of_birth TEXT NOT NULL,
                    class_name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    average_score REAL NOT NULL
                        CHECK (average_score >= 0 AND average_score <= 10)
                )
                """
            )

    def _add_demo_students(self) -> None:
        with closing(self._connect()) as connection, connection:
            connection.executemany(
                """
                INSERT OR IGNORE INTO students
                    (student_id, full_name, gender, date_of_birth, class_name,
                     phone, email, average_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                DEMO_STUDENTS,
            )

    def list_students(
        self, keyword: str = "", class_name: str = ""
    ) -> list[sqlite3.Row]:
        conditions: list[str] = []
        parameters: list[str] = []
        if keyword:
            pattern = f"%{keyword}%"
            conditions.append(
                "(student_id LIKE ? OR full_name LIKE ? OR class_name LIKE ?)"
            )
            parameters.extend((pattern, pattern, pattern))
        if class_name and class_name != "Tat ca lop":
            conditions.append("class_name = ?")
            parameters.append(class_name)

        query = "SELECT * FROM students"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY student_id"
        with closing(self._connect()) as connection:
            return list(connection.execute(query, parameters).fetchall())

    def add_student(self, student: tuple[object, ...]) -> None:
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                INSERT INTO students
                    (student_id, full_name, gender, date_of_birth, class_name,
                     phone, email, average_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                student,
            )

    def update_student(self, original_id: str, student: tuple[object, ...]) -> None:
        with closing(self._connect()) as connection, connection:
            connection.execute(
                """
                UPDATE students
                SET student_id = ?, full_name = ?, gender = ?, date_of_birth = ?,
                    class_name = ?, phone = ?, email = ?, average_score = ?
                WHERE student_id = ?
                """,
                (*student, original_id),
            )

    def delete_student(self, student_id: str) -> None:
        with closing(self._connect()) as connection, connection:
            connection.execute(
                "DELETE FROM students WHERE student_id = ?", (student_id,)
            )

    def class_names(self) -> list[str]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                "SELECT DISTINCT class_name FROM students ORDER BY class_name"
            ).fetchall()
        return [row["class_name"] for row in rows]

    def summary(self) -> tuple[int, float, int]:
        with closing(self._connect()) as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS student_count,
                       COALESCE(AVG(average_score), 0) AS average_score,
                       COUNT(DISTINCT class_name) AS class_count
                FROM students
                """
            ).fetchone()
        return row["student_count"], row["average_score"], row["class_count"]

    def class_averages(self) -> list[tuple[str, float]]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT class_name, AVG(average_score) AS average_score
                FROM students
                GROUP BY class_name
                ORDER BY class_name
                """
            ).fetchall()
        return [(row["class_name"], row["average_score"]) for row in rows]
