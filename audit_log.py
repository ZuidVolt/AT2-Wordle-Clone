import datetime as dt
from pathlib import Path
from typing import TypedDict

LOG_FILE_PATH = Path("audit.jsonl")


class LogAppendError(Exception):
    pass


type FiveIntTuple = tuple[int, int, int, int, int]
type AuditLogList = list[AuditLog]


class AuditLog(TypedDict):
    timestamp: dt.datetime
    name: str
    target_word: str
    guess_word: str  # valid guess only
    score: FiveIntTuple


def write_log_file(
    user_json_object, log_file_path: Path = LOG_FILE_PATH
) -> None:
    try:
        with log_file_path.open("a", encoding="utf-8") as file_handler:
            file_handler.writelines(user_json_object)
    except OSError as e:
        raise LogAppendError from e


if __name__ == "__main__":
    mock_audit_log_data: AuditLog = {
        "timestamp": dt.datetime.now(),
        "name": "test_user",
        "target_word": "apple",
        "guess_word": "paper",
        "score": (0, 2, 0, 1, 1),
    }
    write_log_file(mock_audit_log_data)
