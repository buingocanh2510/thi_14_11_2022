# Họ tên: Bùi Thị Ngọc Ánh
# Mã sinh viên: 1451020013
# Đề bài:
# Bài 3, Viết chương trình kiểm tra một số n là số thuận nghịch trong Python. Số nguyên dương n được nhập từ bàn phím. 
# a, Nhập và in ra màn hình tên đầy đủ của mình 
# b, chạy chương trình bằng cách nhập n từ bàn phím bằng cách tạo n như sau lấy số lượng họ , tên đệm, tên 
# Ví dụ  DINH MANH CUONG thi n = 445 

# Hàm tìm n theo họ và tên
def timNtheoHoVaTen(hoVaTen):
    # tách họ và tên theo dấu cách và lưu vào mảng array
    array = hoVaTen.split(" ")
    # Biến lưu n dạng chuỗi
    nString = ""

    for i in range(0, len(array)):
        # lấy độ dài của họ, tên đệm, tên
        doDai = len(array[i])
        # cộng vào chuỗi n
        nString = nString + str(doDai)
    return int(nString)

# Hàm kiểm tra xem n có phải số thuận nghịch hay không
def laSoThuanNghich(n):
    str1 = str(n) # ép sang kiểu chuỗi
    str2 = str1[::-1] # Đảo ngược chuỗi s1
    return str1==str2

# a
print("a)")
hoVaTen = input("Mời bạn nhập vào họ và tên: ")
print("Họ và tên:", hoVaTen)

# b
print("\nb)")
# Tìm n theo họ và tên
n = timNtheoHoVaTen(hoVaTen)
print("Số n theo họ và tên là:", n)

# In kết quả
if(laSoThuanNghich(n)):
    print(n, "là số thuận nghịch!")
else:
    print(n, "không phải là số thuận nghịch!")


