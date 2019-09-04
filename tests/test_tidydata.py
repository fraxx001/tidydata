#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tidydata` package."""

import pytest


from tidydata import tibble

def test_tibble():
    """Sample pytest test function with the pytest fixture as an argument."""

    tb = tibble.Tibble()
    assert tb.say_my_name() == "Alex"
