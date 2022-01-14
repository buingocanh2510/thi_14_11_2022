# Họ tên: Bùi Thị Ngọc Ánh
# Mã sinh viên: 1451020013
# Đề bài:
# Bài 2 Viết chương trình tính tổng của các chữ số của một số nguyên n trong Python.
# Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10 
# a, Nhập và in ra màn hình tên đệm của mình 
# b, Chạy chương trình bằng cách nhập n bằng độ dài tên của mình và tên đệm ví dụ MANH CUONG thi n = 4 + 5 = 9

from ctypes import sizeof
from operator import le

# Hàm tính tổng các chữ số của 1 số tự nhiên
def tinhTongCacChuSo(n):
    tong = 0
    while n > 0:
        du = n % 10
        tong = tong + du
        n =  int(n/10)
    return tong

# Hàm tìm n theo tên đệm
def timNtheoTenDem(hoVaTen):
    array = hoVaTen.split(" ")
    nString = ""
    for i in range(0, len(array)):
        doDai = len(array[i])
        nString = nString + str(doDai)
    return int(nString)

# a
print("a)")
tenDem = input("Nhập tên đệm: ")
print("Tên đệm:", tenDem)

# b
print("\nb)")
n = int(timNtheoTenDem(tenDem))
print("Số nguyên n theo tên đệm là:", n)

# In kết quả ra màn hình
print("Tổng các chữ số nguyên dương của", n, "=", tinhTongCacChuSo(n))