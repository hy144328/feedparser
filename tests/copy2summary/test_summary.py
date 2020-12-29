#!/usr/bin/env python3

import feedparser
import itertools
import pytest

test_summary_args = ["content", "description", "summary"]

@pytest.mark.parametrize("a,b,c", list(itertools.permutations(test_summary_args)))
def test_summary(a, b, c):
    with open(f"tests/copy2summary/item_{a}_{b}_{c}.xml", 'r') as f:
        d = feedparser.parse(f.read())
    assert(d.entries[0].summary == "Example summary")
