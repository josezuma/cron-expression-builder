#!/usr/bin/env python3
"""CLI: cron-expression-builder"""
import sys, json, argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Cron Expression Builder")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "cron-expression-builder", "version": "1.0.0", "author": "Jose Zuma", "time": datetime.utcnow().isoformat() + "Z"}
    if args.json: print(json.dumps(result, indent=2))
    else: print(f"{name} v1.0.0")
if __name__ == "__main__": main()
