# Study Planner demo

Các lệnh dưới đây chạy từ thư mục `python-bootcamp` với Python 3.12.14. Mỗi output được ghi lại từ lần chạy CLI thực tế; exit code được lấy ngay sau lệnh.

## 1. Chạy bình thường với danh sách công việc mẫu

Lệnh đọc `samples/tasks.csv`, lập kế hoạch tối đa 2 giờ và cố định ngày tham chiếu để kết quả có thể lặp lại. Tổng effort lớn hơn thời gian có sẵn nên planner in cảnh báo, vẫn tạo kế hoạch từng phần và trả exit code 0.

```console
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
warning: need 7.5 h but only 2.0 h available
Tonight (2.0 h):
1. Assignment - 1.5 h
2. DS exam - 0.5 h
exit_code=0
```

## 2. Báo lỗi khi file không tồn tại

Lệnh dùng một đường dẫn không có trong thư mục `samples`. CLI báo rõ file bị thiếu và kết thúc với exit code 1.

```console
python -m shared.study_planner samples/missing.csv --hours 2 --today 2026-10-26
error: File 'samples/missing.csv' not found
exit_code=1
```

## 3. Báo lỗi khi CSV có dữ liệu sai

Trong `samples/tasks_bad.csv`, giá trị `importance` ở dòng 3 là `high`, không thể chuyển thành số nguyên. Parser báo số dòng bị lỗi và CLI trả exit code 1.

```console
python -m shared.study_planner samples/tasks_bad.csv --hours 2 --today 2026-10-26
error: line 3: invalid literal for int() with base 10: 'high'
exit_code=1
```
