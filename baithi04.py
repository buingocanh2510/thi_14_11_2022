# Họ tên: Bùi Thị Ngọc Ánh
# Mã sinh viên: 1451020013
# Đề bài:
# Bài 4, Viết chương trình chấp nhận một chuỗi ký tự, 
# phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
# a, Nhập và in màn hình tên của mình và id sinh viên ví dụ dinhmanhcuong123456
# b, Chạy và in ra màn hình bằng chuỗi tạo ra ở câu a

#a
# Nhập họ tên
hoTenVaMaSV = input("Nhập vào họ và tên và id sinh viên: ")

# In họ tên + id sinh viên
print("a)")
print(hoTenVaMaSV)

#b
# Tạo danh sách phân tách dấu phẩy
list = hoTenVaMaSV.split(",")
 # Tạo tuple
tuple = tuple(list)

# In kết quả
print("\nb)")
print ("Danh sách:", list)
print ("Tuple:", tuple)