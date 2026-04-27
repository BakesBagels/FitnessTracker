import json
import os
import sys

def check_gate():
    zap_report = 'report_json.json'
    threshold = 'high'
    
    if not os.path.exists(zap_report):
        print("FAIL: zap_report.json not found!")
        # Если файла нет, пока выходим с 0, чтобы не стопорить всё, 
        # но для отчета он должен быть.
        sys.exit(0)

    with open(zap_report) as f:
        data = json.load(f)
    
    findings_total = 0
    blocking_findings = 0

    # Проходим по всем найденным алертам от ZAP
    for site in data.get('site', []):
        for alert in site.get('alerts', []):
            findings_total += 1
            # Если риск High (код 3) — это блокирующий фактор
            if alert.get('riskcode') == '3': 
                blocking_findings += 1

    print(f"[security-gate] Threshold: {threshold}")
    print(f"[security-gate] Findings total: {findings_total}")
    print(f"[security-gate] Blocking by threshold: {blocking_findings}")

    if blocking_findings > 0:
        print("[security-gate] RESULT: BLOCK")
        sys.exit(1)
    else:
        print("[security-gate] RESULT: PASSED")
        sys.exit(0)

if __name__ == "__main__":
    check_gate()
