import subprocess
import time
import datetime
import os
import html
import webbrowser

print("\n===== STARTING FULL SELENIUM SUITE =====\n")

# =====================================================
# USER TOGGLES (Tune here only)
# =====================================================
AUTO_OPEN_REPORT = True                 # True/False
CAPTURE_SCREENSHOTS_ON_FAIL = True      # True/False
TC_LIST_FILE = "TC_List.txt"
REPORTS_DIR = "reports"
TEMPLATES_DIR = "templates"
TEMPLATE_FILE = os.path.join(TEMPLATES_DIR, "report_template.html")
# =====================================================

# Ensure folders exist
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Load test cases from TC_List.txt
if not os.path.exists(TC_LIST_FILE):
    print(f"ERROR: '{TC_LIST_FILE}' not found!")
    exit()

with open(TC_LIST_FILE, "r", encoding="utf-8") as f:
    test_cases = [line.strip() for line in f.readlines() if line.strip()]

print("Loaded Test Cases:")
for tc in test_cases:
    print(" →", tc)

results = []
suite_start = time.time()
run_id = int(time.time())

# Run each TC
for tc in test_cases:
    print(f"\nRunning: {tc}")
    print("-------------------------------------------")

    start_time = time.time()

    TC_DIR = "DEMOQA"
    completed = subprocess.run(
    ["python", os.path.join(TC_DIR, tc)],
    capture_output=True,
    text=True
)


    duration = round(time.time() - start_time, 2)
    status = "PASS" if completed.returncode == 0 else "FAIL"

    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()

    # Screenshot path convention:
    # TC should save screenshot into reports/screenshots/<tc_name>_<timestamp>.png
    screenshot_path = ""
    if CAPTURE_SCREENSHOTS_ON_FAIL and status == "FAIL":
        # Find latest screenshot for this TC (if TC saved it)
        shots_dir = os.path.join(REPORTS_DIR, "screenshots")
        if os.path.isdir(shots_dir):
            base = os.path.splitext(os.path.basename(tc))[0]
            matches = [f for f in os.listdir(shots_dir) if f.startswith(base + "_") and f.endswith(".png")]
            if matches:
                latest = sorted(matches)[-1]
                screenshot_path = os.path.join("screenshots", latest)  # relative inside reports

    results.append({
        "name": tc,
        "status": status,
        "duration": duration,
        "stdout": stdout,
        "stderr": stderr,
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "screenshot": screenshot_path
    })

    print(f"Completed: {tc}  --> {status}  ({duration}s)")
    print("-------------------------------------------")
    time.sleep(1)

total_duration = round(time.time() - suite_start, 2)

# Prepare report values
report_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
timestamp = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
report_filename = f"report_{timestamp}.html"
report_file_path = os.path.join(REPORTS_DIR, report_filename)

tc_names_list = [r["name"] for r in results]
tc_times_list = [r["duration"] for r in results]
tc_status_list = [r["status"] for r in results]

passed = sum(1 for r in results if r["status"] == "PASS")
failed = sum(1 for r in results if r["status"] == "FAIL")

def status_class(s):
    return "status-pass" if s == "PASS" else "status-fail"

# Build rows
rows_html = ""
for r in results:
    shot_cell = "—"
    if r["screenshot"]:
        shot_cell = f'<span class="sshot-link"><a target="_blank" href="{html.escape(r["screenshot"])}">View</a></span>'

    rows_html += f"""
    <tr>
        <td>{html.escape(r['name'])}</td>
        <td class="{status_class(r['status'])}">{r['status']}</td>
        <td>{r['duration']} sec<br><small>{r['time']}</small></td>
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
        <td>{shot_cell}</td>
    </tr>
    """

# Load template
if not os.path.exists(TEMPLATE_FILE):
    print(f"ERROR: '{TEMPLATE_FILE}' not found!")
    exit()

with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()

# Replace placeholders
html_output = (template
    .replace("{{REPORT_TIME}}", report_time)
    .replace("{{RUN_ID}}", str(run_id))
    .replace("{{TOTAL_TCS}}", str(len(results)))
    .replace("{{TOTAL_DURATION}}", str(total_duration))
    .replace("{{PASSED}}", str(passed))
    .replace("{{FAILED}}", str(failed))
    .replace("{{TC_ROWS}}", rows_html)
    .replace("{{TC_NAMES}}", str(tc_names_list))
    .replace("{{TC_TIMES}}", str(tc_times_list))
    .replace("{{TC_STATUS}}", str(tc_status_list))
)

# Write report
with open(report_file_path, "w", encoding="utf-8") as f:
    f.write(html_output)

print("\n===== ALL TEST CASES FINISHED =====")
print(f"HTML report generated: {os.path.abspath(report_file_path)}")

# Auto-open if enabled
if AUTO_OPEN_REPORT:
    webbrowser.open(os.path.abspath(report_file_path))
