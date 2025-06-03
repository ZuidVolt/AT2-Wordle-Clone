import datetime as dt
import json
from pathlib import Path

LOG_FILE_PATH = Path("audit.jsonl")


class LogAppendError(Exception):
    pass


def create_audit_log(name, target_word, guess_word, score):
    return {
        "timestamp": format_datetime_as_string(dt.datetime.now()),
        "name": name,
        "target_word": target_word,
        "guess_word": guess_word,
        "score": score,
    }


def format_datetime_as_string(dt_obj):
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S")


def convert_audit_log_to_json_line(audit_log):
    json_str = json.dumps(audit_log)
    json_str_with_newline = json_str + "\n"
    return json_str_with_newline


def append_to_log_file(audit_log, log_file_path=LOG_FILE_PATH):
    """
    raises: LogAppendError if failed to append to log file
    """
    json_str_with_newline = convert_audit_log_to_json_line(audit_log)
    try:
        with log_file_path.open("a", encoding="utf-8") as file_handler:
            file_handler.writelines(json_str_with_newline)
    except OSError as e:
        raise LogAppendError from e


if __name__ == "__main__":
    mock_user_data = (
        "test_user",
        "test_user",
        "paper",
        (0, 2, 0, 1, 1),
    )
    mock_audit_log = create_audit_log(
        mock_user_data[0],
        mock_user_data[1],
        mock_user_data[2],
        mock_user_data[3],
    )
    append_to_log_file(mock_audit_log)
