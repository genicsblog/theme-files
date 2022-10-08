# Drafts validation script - TEST 1
# There test ensures that there should be a failure when files
# other than _drafts/test.md are changed.

import subprocess

folder = "_scripts"
script = "validate-drafts.py"
fail_count = 0

# Case 1: Multiple files are edited along with _drafts/test.md
command = f"""
  echo 'Gemfile _drafts/test.md' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should not return 0
if(res.returncode == 0):
  print("Test 1, case 1: FAILURE")
  fail_count += 1
else:
  print("Test 1, case 1: PASSED")

# Reset temp.txt in between runs
subprocess.run("rm temp.txt", shell = True)

# Case 2: Only _drafts/test.md is edited.
command = f"""
  echo '_drafts/test.md' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass should return 0
if(res.returncode != 0):
  print("Test 1, case 2: FAILURE")
  fail_count += 1
else:
  print("Test 1, case 2: PASSED")

if fail_count != 0:
  exit(1)

print("=======================")
