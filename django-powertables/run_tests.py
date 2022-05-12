#!/usr/bin/env python
import sys
from unittest import TestSuite

from setup_django import setup_django

setup_django()

default_labels = [
    "tests",
]


def get_suite(*, labels=default_labels):
    from django.test.runner import DiscoverRunner

    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    return TestSuite()


if __name__ == "__main__":
    suite_labels = default_labels
    if len(sys.argv[1:]) > 0:
        suite_labels = sys.argv[1:]

    get_suite(labels=suite_labels)
