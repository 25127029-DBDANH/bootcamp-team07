# Python Bootcamp

Bài tập Python 3 tuần của nhóm 07, nộp qua repo này (dùng cho W1, W2, W3).

## Quy tắc
- Mỗi người chỉ viết code trong `members/<thu_muc_cua_minh>/wN/`.
- Tên thư mục: username GitHub viết thường, đổi dấu `-` thành `_`.
- Mỗi tuần một nhánh `py/wN-<username>`, một Pull Request, ít nhất 5 commit.
- Commit dạng `feat(py-w1): W1-2 word counter`.
- PR cần reviewer xoay vòng approve và test pass mới được merge.
- Dùng AI: ghi rõ trong mục "AI use" của PR và trong `docs/ai-use-log.md`.

## Thành viên và thư mục
| Username GitHub | Thư mục |
|---|---|
| 25127029-DBDANH | 25127029_dbdanh |
| ankhang-maker | ankhang_maker |
| dhdang2523-coder | dhdang2523_coder |
| DMH554 | dmh554 |
| EddieOuttaHere | eddieouttahere |
| LamNotNam1607 | lamnotnam1607 |
| pghung2516-netizen | pghung2516_netizen |

## Cấu trúc
    members/   mỗi người một thư mục, trong đó w1/ w2/ w3/
    shared/    code chung của nhóm (tuần 2 và 3)
    tests/     test do giảng viên cung cấp

## Chạy test
    pytest -q python-bootcamp/tests/test_w1.py --member <thu_muc> --variant <so_thu_tu>

## Kiểm tra code
    ruff check python-bootcamp