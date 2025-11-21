import subprocess
import time

print("\n===== STARTING FULL SELENIUM SUITE =====\n")

# Your exact file names
test_cases = [
    "TC1_google_search.py",
    "TC2_FLIPKART SEARCH.py",
    "TC3_Search_item.py",
    "TC4_hrm_login.py"
]

for tc in test_cases:
    print(f"\nRunning: {tc}")
    print("-------------------------------------------")

    # Run each Python script
    try:
        subprocess.run(["python", tc])
    except Exception as e:
        print(f"Error running {tc}: {e}")

    print(f"Completed: {tc}")
    print("-------------------------------------------")
    time.sleep(2)

print("\n===== ALL TEST CASES FINISHED SUCCESSFULLY =====")
