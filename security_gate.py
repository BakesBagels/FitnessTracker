import json
import sys

try:
    with open('semgrep-report.json', 'r') as f:
        data = json.load(f)
    findings = len(data.get('results', []))
    print(f"Total findings: {findings}")
    if findings > 0:
        print("RESULT: FAILED")
        sys.exit(1)
    else:
        print("RESULT: PASSED")
        sys.exit(0)
except Exception:
    sys.exit(1)
