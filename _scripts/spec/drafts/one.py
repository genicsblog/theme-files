# Drafts validation script - TEST 1
# This test ensures that there should be a failure when files
# other than _drafts/test.md are changed.

print("Test 1")
print("------")

import subprocess

fail_count = 0
folder = "_scripts"
script = "validate-drafts.py"
draft_file = "_drafts/test.md"

def validate(case, code, shouldBeZero):
  global fail_count

  if((code == 0 and shouldBeZero) or (code != 0 and not shouldBeZero)):
    print(f"Case {case}: PASSED")
  else:
    print(f"Case {case}: FAILED")
    fail_count += 1

# Case 1: Only _drafts/test.md is edited.
command = f"""
  echo '{draft_file}' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command returns 0
validate(case = 1, code = res.returncode, shouldBeZero = True)

# Reset temp.txt in between runs
subprocess.run("rm temp.txt", shell = True)

# Case 2: Multiple files are edited along with _drafts/test.md
command = f"""
  echo 'Gemfile _config.yml {draft_file}' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
validate(case = 2, code = res.returncode, shouldBeZero = False)

if fail_count != 0:
  exit(1)

print()
