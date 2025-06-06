import json
from pathlib import Path
from typing import Final, TypedDict

from audit_log import AuditLog, AuditLogList, FiveIntTuple, LogAppendError

MOCK_LOG_FILE_PATH = Path("mock_audit.jsonl")


class AuditLogParseError(Exception):
    pass


class MockAuditData(TypedDict):
    name: str
    target_word: str
    guess_word: str
    score: FiveIntTuple


def audit_log_parser(path: Path = MOCK_LOG_FILE_PATH) -> AuditLogList:
    """Parse audit log file and return list of audit logs.

    raises:
        AuditLogParseError if failed to parse audit log file (should be handled by the caller)
    """
    try:
        audit_log_list: AuditLogList = []
        with path.open("r", encoding="utf-8") as file_handler:
            for line in file_handler:
                stripped_line = line.strip()
                if stripped_line:
                    audit_log: AuditLog = json.loads(stripped_line)
                    audit_log_list.append(audit_log)
        return audit_log_list
    except Exception as e:
        print(f"Error parsing audit log: {e}")
        raise AuditLogParseError from e


def test_sequential_audit_log_file_writes(
    file_path: Path, mock_data: list[MockAuditData]
) -> bool:
    from audit_log import append_to_log_file, create_audit_log

    if file_path.exists():
        file_path.unlink()

    for data in mock_data:
        audit_log = create_audit_log(
            data["name"],
            data["target_word"],
            data["guess_word"],
            data["score"],
        )
        try:
            append_to_log_file(audit_log, file_path)
        except LogAppendError as e:
            print(f"Failed to append to log file: {e}")
            return False
    return True


def test_audit_log_script() -> None:
    audit_log_path: Final[Path] = MOCK_LOG_FILE_PATH

    # Define test data
    mock_audit_data: list[MockAuditData] = [
        {
            "name": "test_user1",
            "target_word": "apple",
            "guess_word": "paper",
            "score": (0, 2, 0, 1, 1),
        },
        {
            "name": "test_user2",
            "target_word": "banana",
            "guess_word": "bread",
            "score": (1, 0, 0, 0, 0),
        },
    ]

    print("--- TEST audit_log CASES ---")

    print("Test case 1, Sequential audit log file writes with mock data:")
    result = test_sequential_audit_log_file_writes(
        audit_log_path, mock_audit_data
    )
    assert result, "Failed to write mock audit logs sequentially"
    print("PASSED")

    print("Test case 2, Validating audit log data length:")
    try:
        audit_log_list = audit_log_parser(audit_log_path)
    except AuditLogParseError as e:
        raise AssertionError(
            "Audit log parser failed, all test results are invalid"
        ) from e
    assert len(audit_log_list) == len(mock_audit_data), (
        "Audit log count mismatch"
    )
    print("PASSED")

    print("Test case 3, Validating audit log data content:")
    for i in range(len(audit_log_list)):
        log = audit_log_list[i]
        expected = mock_audit_data[i]
        assert log["name"] == expected["name"], "Name mismatch"
        assert log["target_word"] == expected["target_word"], (
            "Target word mismatch"
        )
        assert log["guess_word"] == expected["guess_word"], (
            "Guess word mismatch"
        )
        # Convert both to list for comparison (as they are tuples)
        assert list(log["score"]) == list(expected["score"]), "Score mismatch"
    print("PASSED")

    print("all test cases passed for audit_log.py, removing mock log file")
    if audit_log_path.exists():
        audit_log_path.unlink()


def try_log_parser() -> None:
    audit_log_list = audit_log_parser()
    print(f"Parsed {len(audit_log_list)} audit logs.")
    for log in audit_log_list:
        print(log)


def test_all() -> None:
    test_audit_log_script()


if __name__ == "__main__":
    test_all()
