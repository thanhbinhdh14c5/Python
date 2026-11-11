import math
import sqlite3
import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk
from typing import Any

from csdl_sinhvien import DATABASE_PATH, StudentDatabase


COLORS = {
    "background": "#f3f6fb",
    "navy": "#17324d",
    "blue": "#2878c8",
    "green": "#198754",
    "red": "#dc3545",
    "text": "#243447",
    "muted": "#718096",
    "white": "#ffffff",
}


class StudentManagementApp:
    def __init__(self, root: tk.Tk, database: StudentDatabase) -> None:
        self.root = root
        self.database = database
        self.selected_student_id: str | None = None
        self.sort_descending = False
        self.fields: dict[str, tk.StringVar] = {
            "student_id": tk.StringVar(),
            "full_name": tk.StringVar(),
            "gender": tk.StringVar(value="Nam"),
            "date_of_birth": tk.StringVar(),
            "class_name": tk.StringVar(),
            "phone": tk.StringVar(),
            "email": tk.StringVar(),
            "average_score": tk.StringVar(),
        }
        self.keyword = tk.StringVar()
        self.class_filter = tk.StringVar(value="Tat ca lop")
        self._configure_window()
        self._build_interface()
        self.refresh_students()

    def _configure_window(self) -> None:
        self.root.title("Quan ly sinh vien")
        self.root.geometry("1280x760")
        self.root.minsize(1080, 680)
        self.root.configure(bg=COLORS["background"])
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            rowheight=32,
            font=("Segoe UI", 10),
            background=COLORS["white"],
            fieldbackground=COLORS["white"],
            foreground=COLORS["text"],
        )
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#e8eef5",
            foreground=COLORS["navy"],
            relief="flat",
        )
        style.map("Treeview", background=[("selected", "#cfe4fa")])
        style.configure("TCombobox", padding=6)

    def _build_interface(self) -> None:
        header = tk.Frame(self.root, bg=COLORS["navy"], height=92)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(
            header,
            text="QUAN LY SINH VIEN",
            bg=COLORS["navy"],
            fg=COLORS["white"],
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w", padx=28, pady=(18, 0))
        tk.Label(
            header,
            text="Thong tin sinh vien | Du lieu duoc luu tu dong bang SQLite",
            bg=COLORS["navy"],
            fg="#cbd8e5",
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=30, pady=(3, 10))

        self.summary_frame = tk.Frame(self.root, bg=COLORS["background"])
        self.summary_frame.pack(fill="x", padx=22, pady=(16, 10))

        content = tk.Frame(self.root, bg=COLORS["background"])
        content.pack(fill="both", expand=True, padx=22, pady=(0, 14))
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)
        self._build_form(content)
        self._build_table(content)

        self.status = tk.StringVar(value="San sang")
        tk.Label(
            self.root,
            textvariable=self.status,
            anchor="w",
            bg=COLORS["background"],
            fg=COLORS["muted"],
            font=("Segoe UI", 9),
        ).pack(fill="x", padx=26, pady=(0, 8))

    def _build_form(self, parent: tk.Frame) -> None:
        form = tk.Frame(parent, bg=COLORS["white"], padx=18, pady=16)
        form.grid(row=0, column=0, sticky="ns", padx=(0, 16))
        tk.Label(
            form,
            text="THONG TIN SINH VIEN",
            bg=COLORS["white"],
            fg=COLORS["navy"],
            font=("Segoe UI", 13, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))

        field_specs = [
            ("student_id", "Ma sinh vien"),
            ("full_name", "Ho va ten"),
            ("gender", "Gioi tinh"),
            ("date_of_birth", "Ngay sinh (YYYY-MM-DD)"),
            ("class_name", "Lop"),
            ("phone", "So dien thoai"),
            ("email", "Email"),
            ("average_score", "Diem trung binh (0-10)"),
        ]
        for row, (key, label) in enumerate(field_specs, start=1):
            tk.Label(
                form, text=label, bg=COLORS["white"], fg=COLORS["text"]
            ).grid(row=row, column=0, sticky="w", pady=5)
            if key == "gender":
                widget: Any = ttk.Combobox(
                    form,
                    textvariable=self.fields[key],
                    values=("Nam", "Nu", "Khac"),
                    state="readonly",
                    width=23,
                )
            else:
                widget = ttk.Entry(form, textvariable=self.fields[key], width=26)
            widget.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=5)

        buttons = tk.Frame(form, bg=COLORS["white"])
        buttons.grid(row=9, column=0, columnspan=2, sticky="ew", pady=(14, 0))
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)
        self._button(buttons, "Them moi", self.add_student, COLORS["blue"]).grid(
            row=0, column=0, sticky="ew", padx=(0, 5), pady=4
        )
        self._button(buttons, "Cap nhat", self.update_student, COLORS["green"]).grid(
            row=0, column=1, sticky="ew", padx=(5, 0), pady=4
        )
        self._button(buttons, "Xoa", self.delete_student, COLORS["red"]).grid(
            row=1, column=0, sticky="ew", padx=(0, 5), pady=4
        )
        self._button(buttons, "Lam moi", self.clear_form, "#64748b").grid(
            row=1, column=1, sticky="ew", padx=(5, 0), pady=4
        )
        self._button(
            buttons, "Bieu do diem theo lop", self.show_chart, COLORS["navy"]
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    def _build_table(self, parent: tk.Frame) -> None:
        panel = tk.Frame(parent, bg=COLORS["white"], padx=16, pady=15)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.rowconfigure(1, weight=1)
        panel.columnconfigure(0, weight=1)
        tk.Label(
            panel,
            text="DANH SACH SINH VIEN",
            bg=COLORS["white"],
            fg=COLORS["navy"],
            font=("Segoe UI", 13, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        filters = tk.Frame(panel, bg=COLORS["white"])
        filters.grid(row=0, column=1, sticky="e", pady=(0, 12))
        search_entry = ttk.Entry(filters, textvariable=self.keyword, width=25)
        search_entry.pack(side="left", padx=(0, 8))
        search_entry.bind("<Return>", lambda _event: self.refresh_students())
        ttk.Button(filters, text="Tim kiem", command=self.refresh_students).pack(
            side="left", padx=(0, 8)
        )
        self.class_combo = ttk.Combobox(
            filters,
            textvariable=self.class_filter,
            values=("Tat ca lop",),
            state="readonly",
            width=14,
        )
        self.class_combo.pack(side="left")
        self.class_combo.bind(
            "<<ComboboxSelected>>", lambda _event: self.refresh_students()
        )

        table_frame = tk.Frame(panel, bg=COLORS["white"])
        table_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        columns = (
            "student_id", "full_name", "class_name", "gender",
            "date_of_birth", "phone", "email", "average_score",
        )
        headings = {
            "student_id": "Ma SV", "full_name": "Ho va ten",
            "class_name": "Lop", "gender": "Gioi tinh",
            "date_of_birth": "Ngay sinh", "phone": "Dien thoai",
            "email": "Email", "average_score": "Diem TB",
        }
        widths = {
            "student_id": 78, "full_name": 155, "class_name": 75,
            "gender": 70, "date_of_birth": 100, "phone": 100,
            "email": 170, "average_score": 70,
        }
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )
        for column in columns:
            self.tree.heading(
                column,
                text=headings[column],
                command=lambda selected=column: self.sort_table(selected),
            )
            self.tree.column(column, width=widths[column], minwidth=60, anchor="center")
        self.tree.column("full_name", anchor="w")
        self.tree.column("email", anchor="w")
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.bind("<<TreeviewSelect>>", self.select_student)

    @staticmethod
    def _button(
        parent: tk.Widget, text: str, command: Any, color: str
    ) -> tk.Button:
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=COLORS["white"],
            activebackground=color,
            activeforeground=COLORS["white"],
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=8,
            font=("Segoe UI", 9, "bold"),
        )

    def refresh_students(self) -> None:
        self._refresh_class_filter()
        students = self.database.list_students(
            self.keyword.get().strip(), self.class_filter.get()
        )
        self.tree.delete(*self.tree.get_children())
        for student in students:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    student["student_id"], student["full_name"],
                    student["class_name"], student["gender"],
                    student["date_of_birth"], student["phone"],
                    student["email"], f'{student["average_score"]:.1f}',
                ),
            )
        self._refresh_summary()
        self.status.set(f"Dang hien thi {len(students)} sinh vien")

    def _refresh_class_filter(self) -> None:
        current = self.class_filter.get()
        values = ["Tat ca lop", *self.database.class_names()]
        self.class_combo.configure(values=values)
        self.class_filter.set(current if current in values else "Tat ca lop")

    def _refresh_summary(self) -> None:
        for child in self.summary_frame.winfo_children():
            child.destroy()
        count, average, class_count = self.database.summary()
        cards = (
            ("Tong sinh vien", str(count), COLORS["blue"]),
            ("Diem trung binh", f"{average:.2f}", COLORS["green"]),
            ("So lop", str(class_count), COLORS["navy"]),
        )
        for index, (title, value, color) in enumerate(cards):
            card = tk.Frame(self.summary_frame, bg=COLORS["white"], padx=18, pady=10)
            card.grid(row=0, column=index, sticky="ew", padx=(0, 12))
            self.summary_frame.columnconfigure(index, weight=1)
            tk.Label(
                card, text=title, bg=COLORS["white"], fg=COLORS["muted"]
            ).pack(anchor="w")
            tk.Label(
                card,
                text=value,
                bg=COLORS["white"],
                fg=color,
                font=("Segoe UI", 18, "bold"),
            ).pack(anchor="w")

    def _read_form(self) -> tuple[object, ...] | None:
        student_id = self.fields["student_id"].get().strip()
        full_name = self.fields["full_name"].get().strip()
        gender = self.fields["gender"].get().strip()
        birth_date = self.fields["date_of_birth"].get().strip()
        class_name = self.fields["class_name"].get().strip()
        phone = self.fields["phone"].get().strip()
        email = self.fields["email"].get().strip()
        score_text = self.fields["average_score"].get().strip()

        if not student_id or not full_name or not class_name:
            messagebox.showwarning(
                "Thieu thong tin",
                "Ma sinh vien, ho va ten, va lop la cac truong bat buoc.",
                parent=self.root,
            )
            return None
        if gender not in {"Nam", "Nu", "Khac"}:
            messagebox.showwarning(
                "Du lieu khong hop le", "Vui long chon gioi tinh.", parent=self.root
            )
            return None
        try:
            parsed_date = date.fromisoformat(birth_date)
        except ValueError:
            messagebox.showwarning(
                "Du lieu khong hop le",
                "Ngay sinh can dung dinh dang YYYY-MM-DD.",
                parent=self.root,
            )
            return None
        if parsed_date > date.today():
            messagebox.showwarning(
                "Du lieu khong hop le",
                "Ngay sinh khong the o trong tuong lai.",
                parent=self.root,
            )
            return None
        try:
            score = float(score_text)
        except ValueError:
            messagebox.showwarning(
                "Du lieu khong hop le",
                "Diem trung binh phai la mot so tu 0 den 10.",
                parent=self.root,
            )
            return None
        if not math.isfinite(score) or not 0 <= score <= 10:
            messagebox.showwarning(
                "Du lieu khong hop le",
                "Diem trung binh phai nam trong khoang tu 0 den 10.",
                parent=self.root,
            )
            return None
        if email and ("@" not in email or email.startswith("@") or email.endswith("@")):
            messagebox.showwarning(
                "Du lieu khong hop le",
                "Vui long nhap dia chi email hop le.",
                parent=self.root,
            )
            return None
        return (
            student_id, full_name, gender, birth_date, class_name,
            phone, email, score,
        )

    def add_student(self) -> None:
        student = self._read_form()
        if student is None:
            return
        try:
            self.database.add_student(student)
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Khong the them",
                "Ma sinh vien da ton tai. Vui long kiem tra lai.",
                parent=self.root,
            )
            return
        self.clear_form()
        self.refresh_students()
        self.status.set("Da them sinh vien moi")

    def update_student(self) -> None:
        if self.selected_student_id is None:
            messagebox.showwarning(
                "Chua chon sinh vien",
                "Chon mot sinh vien trong bang truoc khi cap nhat.",
                parent=self.root,
            )
            return
        student = self._read_form()
        if student is None:
            return
        try:
            self.database.update_student(self.selected_student_id, student)
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Khong the cap nhat",
                "Ma sinh vien moi da duoc su dung.",
                parent=self.root,
            )
            return
        self.clear_form()
        self.refresh_students()
        self.status.set("Da cap nhat thong tin sinh vien")

    def delete_student(self) -> None:
        if self.selected_student_id is None:
            messagebox.showwarning(
                "Chua chon sinh vien",
                "Chon mot sinh vien trong bang truoc khi xoa.",
                parent=self.root,
            )
            return
        if not messagebox.askyesno(
            "Xac nhan xoa",
            f"Ban co chac muon xoa sinh vien {self.selected_student_id} khong?",
            parent=self.root,
        ):
            return
        self.database.delete_student(self.selected_student_id)
        self.clear_form()
        self.refresh_students()
        self.status.set("Da xoa sinh vien")

    def clear_form(self) -> None:
        for field in self.fields.values():
            field.set("")
        self.fields["gender"].set("Nam")
        self.selected_student_id = None
        for selection in self.tree.selection():
            self.tree.selection_remove(selection)

    def select_student(self, _event: tk.Event) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0], "values")
        self.selected_student_id = values[0]
        for key, value in zip(
            (
                "student_id", "full_name", "class_name", "gender",
                "date_of_birth", "phone", "email", "average_score",
            ),
            values,
        ):
            self.fields[key].set(value)

    def sort_table(self, column: str) -> None:
        items = [
            (self.tree.set(item, column), item)
            for item in self.tree.get_children("")
        ]
        try:
            items.sort(
                key=lambda row: float(row[0]), reverse=self.sort_descending
            )
        except ValueError:
            items.sort(
                key=lambda row: row[0].casefold(), reverse=self.sort_descending
            )
        for index, (_value, item) in enumerate(items):
            self.tree.move(item, "", index)
        self.sort_descending = not self.sort_descending

    def show_chart(self) -> None:
        averages = self.database.class_averages()
        if not averages:
            messagebox.showinfo(
                "Thong ke",
                "Chua co du lieu sinh vien de ve bieu do.",
                parent=self.root,
            )
            return
        try:
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            from matplotlib.figure import Figure
        except ImportError:
            messagebox.showerror(
                "Thieu thu vien",
                "Can cai dat Matplotlib:\npython -m pip install matplotlib",
                parent=self.root,
            )
            return

        window = tk.Toplevel(self.root)
        window.title("Diem trung binh theo lop")
        window.geometry("720x480")
        window.transient(self.root)
        figure = Figure(figsize=(7, 4.2), dpi=100)
        axes = figure.add_subplot(111)
        classes = [item[0] for item in averages]
        scores = [item[1] for item in averages]
        bars = axes.bar(classes, scores, color=COLORS["blue"], width=0.58)
        axes.set_title("Diem trung binh theo lop")
        axes.set_ylabel("Diem trung binh")
        axes.set_ylim(0, 10)
        axes.grid(axis="y", alpha=0.25)
        axes.bar_label(bars, fmt="%.2f", padding=3)
        figure.tight_layout()
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=12)


def main() -> None:
    root = tk.Tk()
    try:
        database = StudentDatabase()
    except sqlite3.Error as error:
        messagebox.showerror(
            "Loi co so du lieu",
            f"Khong the mo co so du lieu:\n{error}",
            parent=root,
        )
        root.destroy()
        return
    StudentManagementApp(root, database)
    root.mainloop()


if __name__ == "__main__":
    main()
