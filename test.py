def wordle_tests():
    from test.test_wordle import test_all

    test_all()


def audit_log_test():
    from test.test_audit_log import test_all

    test_all()


def run_test_suite():
    wordle_tests()
    audit_log_test()


if __name__ == "__main__":
    run_test_suite()
