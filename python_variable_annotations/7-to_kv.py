#!/usr/bin/env python3
"""Function that returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
   """Return tuple with string and square of v"""
   return (k, v * v)