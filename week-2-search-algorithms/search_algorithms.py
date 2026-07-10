# Week 2 of AI Internship at DevSphere
# Topic: Search Algorithms

import time
import random

# LINEAR SEARCH (with step-by-step output)

def linear_search(arr, target):
    print(f"\nLinear Search: looking for {target}")

    for i in range(len(arr)):
        print(f"  Checking index {i}: value = {arr[i]}")
        if arr[i] == target:
            print(f"  Found {target} at index {i}!")
            return i

    print(f"  {target} not found.")
    return -1


# BINARY SEARCH (with step-by-step output)

def binary_search(arr, target):
    print(f"\nBinary Search: looking for {target}")
    low = 0
    high = len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        print(f"  Step {step}: low={low}, high={high}, mid={mid}, value={arr[mid]}")

        if arr[mid] == target:
            print(f"  Found {target} at index {mid}!")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        step += 1

    print(f"  {target} not found.")
    return -1


# SILENT VERSIONS (used for performance timing)

def linear_search_silent(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_silent(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:   # move right
            low = mid + 1
        else:                     # move left
            high = mid - 1
    return -1
