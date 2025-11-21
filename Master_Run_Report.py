import subprocess
import time
import datetime
import os
import html

print("\n===== STARTING FULL SELENIUM SUITE =====\n")

test_cases = [
    "TC1_google_search.py",
    "TC2_FLIPKART SEARCH.py",
    "TC3_Search_item.py",
    "TC4_hrm_login.py"
]

results = []
suite_start = time.time()

for tc in test_cases:
    print(f"\nRunning: {tc}")
    print("-------------------------------------------")

    start_time = time.time()

    # run + capture output
    completed = subprocess.run(
        ["python", tc],
        capture_output=True,
        text=True
    )

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    status = "PASS" if completed.returncode == 0 else "FAIL"

    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()

    results.append({
        "name": tc,
        "status": status,
        "duration": duration,
        "stdout": stdout,
        "stderr": stderr
    })

    print(f"Completed: {tc}  --> {status}  ({duration}s)")
    print("-------------------------------------------")
    time.sleep(1)

suite_end = time.time()
total_duration = round(suite_end - suite_start, 2)

# -------------------------
# Generate HTML Report
# -------------------------
report_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
report_file = "report.html"

def color(status):
    return "#22c55e" if status == "PASS" else "#ef4444"

rows_html = ""
for r in results:
    rows_html += f"""
    <tr>
        <td>{html.escape(r['name'])}</td>
        <td style="font-weight:bold; color:{color(r['status'])};">{r['status']}</td>
        <td>{r['duration']} sec</td>
        <td>
            <details>
                <summary>View Output</summary>
                <pre>{html.escape(r['stdout'] or "No stdout")}</pre>
            </details>
        </td>
        <td>
            <details>
                <summary>View Error</summary>
                <pre style="color:#ef4444;">{html.escape(r['stderr'] or "No error")}</pre>
            </details>
        </td>
    </tr>
    """

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Selenium Basic Suite Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            padding: 20px;
        }}
        h1 {{ color: #38bdf8; }}
        .summary {{
            background: #111827;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: flex;
            gap: 20px;
        }}
        .card {{
            background: #1f2937;
            padding: 10px 15px;
            border-radius: 8px;
            min-width: 150px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: #111827;
            border-radius: 10px;
            overflow: hidden;
        }}
        th, td {{
            padding: 12px;
            border-bottom: 1px solid #334155;
            vertical-align: top;
        }}
        th {{
            background: #1e293b;
            color: #f8fafc;
        }}
        tr:hover {{ background: #0b1220; }}
        pre {{
            white-space: pre-wrap;
            background: #0b1020;
            padding: 10px;
            border-radius: 6px;
            margin-top: 6px;
        }}
        details summary {{
            cursor: pointer;
            color: #a5b4fc;
        }}
    </style>
</head>
<body>
    <h1>✅ Selenium Basic Test Suite Report</h1>

    <div class="summary">
        <div class="card"><b>Run Time:</b><br>{report_time}</div>
        <div class="card"><b>Total TCs:</b><br>{len(results)}</div>
        <div class="card"><b>Total Duration:</b><br>{total_duration} sec</div>
        <div class="card"><b>Passed:</b><br>{sum(1 for r in results if r['status']=="PASS")}</div>
        <div class="card"><b>Failed:</b><br>{sum(1 for r in results if r['status']=="FAIL")}</div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Test Case</th>
                <th>Status</th>
                <th>Time</th>
                <th>Stdout</th>
                <th>Error</th>
            </tr>
        </thead>
        <tbody>
            {rows_html}
        </tbody>
    </table>

</body>
</html>
"""

with open(report_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"\n===== ALL TEST CASES FINISHED =====")
print(f"HTML report generated: {os.path.abspath(report_file)}")

