"""W1-4: insertion sort translated from C++."""


def insertion_sort(a: list[int]) -> list[int]:
    """Sắp xếp danh sách a ngay tại chỗ và trả về danh sách đó.
    Điểm khác biệt so với phiên bản C++: hàm C++ trả về void (không trả về giá trị) và cần một tham số tham chiếu (std::vector<int>&) để thay đổi vector của bên gọi hàm.
    Hàm Python cũng thay đổi danh sách được truyền vào ngay tại chỗ, nhưng trả về danh sách đó để kết quả có thể được sử dụng trực tiếp."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
