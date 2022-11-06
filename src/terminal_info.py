"""
    Module to hold some helpers for terminal output
"""

#===== IMPORT ====================================
import datetime

#===== FUNCTION ======================================
def info(info_text):
    print(f"[INFO]\t{info_text}")

def error(error_text):
    print(f"[ERROR]\t{error_text}")