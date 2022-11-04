# Drafts validation script - TEST 1
# These test ensures that there should be a failure when files
# other than _drafts/test.md are changed.

print("Test 1")
print("------")

import subprocess

folder = "_scripts"
script = "validate-drafts.py"
fail_count = 0

# Case 1: Only _drafts/test.md is edited.
command = f"""
  echo '_drafts/test.md' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command returns 0
if(res.returncode == 0):
  print("Case 1: PASSED")
else:
  print("Case 1: FAILED")
  fail_count += 1

# Reset temp.txt in between runs
subprocess.run("rm temp.txt", shell = True)

# Case 2: Multiple files are edited along with _drafts/test.md
command = f"""
  echo 'Gemfile _drafts/test.md' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
if(res.returncode != 0):
  print("Case 2: PASSED")
else:
  print("Case 2: FAILED")
  fail_count += 1

if fail_count != 0:
  exit(1)

print("\n")
