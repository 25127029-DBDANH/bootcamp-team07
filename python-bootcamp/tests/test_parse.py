from datetime import date

import pytest
from shared.contract import Task
from shared.study_planner.parse import parse_csv


def test_parse_csv_valid(tmp_path):
    # Trường hợp bình thường: file đúng định dạng
    file_path = tmp_path / "valid_tasks.csv"
    file_path.write_text("title,importance,effort_h,deadline\nDS exam,5,6.0,2026-10-30\n")
    
    tasks = parse_csv(str(file_path))
    assert len(tasks) == 1
    assert tasks[0] == Task("DS exam", 5, 6.0, date(2026, 10, 30))

def test_parse_csv_missing_columns(tmp_path):
    # Trường hợp biên: file thiếu cột
    file_path = tmp_path / "missing_col.csv"
    file_path.write_text("title,importance,effort_h\nDS exam,5,6.0\n")
    
    with pytest.raises(ValueError):
        parse_csv(str(file_path))

def test_parse_csv_invalid_importance(tmp_path):
    # Trường hợp lỗi: importance nằm ngoài 1-5
    file_path = tmp_path / "invalid_imp.csv"
    file_path.write_text("title,importance,effort_h,deadline\nDS exam,6,6.0,2026-10-30\n")
    
    with pytest.raises(ValueError):
        parse_csv(str(file_path))

def test_parse_csv_invalid_date(tmp_path):
    # Trường hợp lỗi: ngày sai định dạng
    file_path = tmp_path / "invalid_date.csv"
    file_path.write_text("title,importance,effort_h,deadline\nDS exam,5,6.0,30-10-2026\n")
    
    with pytest.raises(ValueError):
        parse_csv(str(file_path))

def test_parse_csv_empty_header_only(tmp_path):
    # Trường hợp biên: file rỗng chỉ có header
    file_path = tmp_path / "empty.csv"
    file_path.write_text("title,importance,effort_h,deadline\n")
    
    tasks = parse_csv(str(file_path))
    assert tasks == []