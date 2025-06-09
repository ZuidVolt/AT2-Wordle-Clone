import datetime as dt
import json
from pathlib import Path
from typing import TypedDict

# uses jsonl format which i learned about here https://jsonlines.org/examples/
LOG_FILE_PATH = Path("audit.jsonl")


class LogAppendError(Exception):
    pass


type FiveIntTuple = tuple[int, int, int, int, int]
type AuditLogList = list[AuditLog]
type DateTimeStr = str


class AuditLog(TypedDict):
    timestamp: DateTimeStr
    name: str
    target_word: str
    guess_word: str  # valid guess only
    score: FiveIntTuple


def create_audit_log(
    name: str, target_word: str, guess_word: str, score: FiveIntTuple
) -> AuditLog:
    return {
        "timestamp": format_datetime_as_string(dt.datetime.now()),
        "name": name,
        "target_word": target_word,
        "guess_word": guess_word,
        "score": score,
    }


def format_datetime_as_string(dt_obj: dt.datetime) -> DateTimeStr:
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S")


def convert_audit_log_to_json_line(audit_log: AuditLog) -> str:
    json_str = json.dumps(audit_log)
    json_str_with_newline = json_str + "\n"
    return json_str_with_newline


def append_to_log_file(
    audit_log: AuditLog, log_file_path: Path = LOG_FILE_PATH
) -> None:
    """
    raises: LogAppendError if failed to append to log file
    """
    json_str_with_newline = convert_audit_log_to_json_line(audit_log)
    try:
        with (
            log_file_path.open("a", encoding="utf-8") as file_handler
        ):  # if the file does not exist, it will be created because i'm using a path object
            file_handler.writelines(json_str_with_newline)
    except OSError as e:
        raise LogAppendError from e  # re-raise to be handled by the caller


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
