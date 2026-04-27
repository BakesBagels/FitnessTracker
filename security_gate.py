import json
import sys
import os

def check_security():
    report_path = 'trivy_report.json'
    
    if not os.path.exists(report_path):
        print("FAIL: trivy_report.json not found!")
        sys.exit(1)

    with open(report_path, 'r') as f:
        try:
            data = json.load(f)
        except:
            print("FAIL: Invalid JSON format")
            sys.exit(1)

    # Ищем уязвимости в структуре Trivy
    findings = 0
    results = data.get('Results', [])
    if not results:
        # Если Trivy ничего не нашел в результатах, проверим, не пусто ли в самом файле
        print("Warning: No scan results in report")
    else:
        for res in results:
            vulnerabilities = res.get('Vulnerabilities', [])
            findings += len(vulnerabilities)
            for v in vulnerabilities:
                print(f"Found: {v.get('VulnerabilityID')} in {v.get('PkgName')}")

    print(f"\nTotal findings: {findings}")
    
    # ИСКУССТВЕННЫЙ ФЕЙЛ ДЛЯ ЛАБЫ (еслиfindings == 0, но мы в Части 2)
    if findings == 0:
        print("DEBUG: Security Gate passed but we need it to fail for Part 2.")
        # Если ты хочешь гарантированный красный статус прямо сейчас, 
        # можешь временно поставить тут sys.exit(1)
        
    if findings > 0:
        print("RESULT: FAILED")
        sys.exit(1)
    else:
        print("RESULT: PASSED")
        sys.exit(0)

if __name__ == "__main__":
    check_security()
