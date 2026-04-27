import json
import os
import sys

def check_gate():
    report_file = 'report_json.json'
    
    if not os.path.exists(report_file) or os.path.getsize(report_file) == 0:
        print("CRITICAL: DAST report is missing or empty!")
        sys.exit(1)

    with open(report_file) as f:
        data = json.load(f)
    
    high_alerts = 0
    total_alerts = 0
    
    for site in data.get('site', []):
        for alert in site.get('alerts', []):
            total_alerts += 1
            if alert.get('riskcode') == '3': # High Risk
                high_alerts += 1

    print(f"--- DAST Security Gate Results ---")
    print(f"Total vulnerabilities found: {total_alerts}")
    print(f"High-risk vulnerabilities: {high_alerts}")

    if high_alerts > 0:
        print("RESULT: FAILED (High risk alerts found)")
        sys.exit(1)
    else:
        print("RESULT: PASSED (No high risk alerts)")
        sys.exit(0)

if __name__ == "__main__":
    check_gate()
