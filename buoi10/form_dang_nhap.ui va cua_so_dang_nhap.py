
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        # Lấy đường dẫn thư mục chứa file Python
        thu_muc = os.path.dirname(os.path.abspath(__file__))
        duong_dan_ui = os.path.join(thu_muc, "form_dang_nhap.ui")

        # Nạp giao diện
        uic.loadUi(duong_dan_ui, self)

        # Kết nối nút đăng nhập
        self.nut_dang_nhap.clicked.connect(
            self.xu_ly_dang_nhap
        )

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(
                self,
                "Lỗi",
                "Vui lòng nhập đầy đủ tài khoản và mật khẩu."
            )
            return

        if tai_khoan == "thanhbinh" and mat_khau == "12345678":
            QMessageBox.information(
                self,
                "Thành công",
                f"Xin chào {tai_khoan}, đăng nhập thành công!"
            )
        else:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Sai tài khoản hoặc mật khẩu!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = CuaSoDangNhap()
    cua_so.show()

    sys.exit(app.exec_())
