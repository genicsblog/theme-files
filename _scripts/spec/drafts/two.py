# Drafts validation script - TEST 2
# These tests ensures that only a valid github account may
# may change a draft.

print("Test 2")
print("------")

import subprocess

folder = "_scripts"
script = "validate-drafts.py"
fail_count = 0

# Case 1: draft test.md is changed by committer gouravkhunger (VALID)
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


# Case 1: draft test.md is changed by committer gouravkhunger (VALID)
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

# Case 2: draft test.md is changed by committer kushagra (INVALID)
command = f"""
  echo '_drafts/test.md' >> temp.txt;
  python3.9 {folder}/{script} kushagra;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
if(res.returncode == 0):
  print("Case 1: PASSED")
else:
  print("Case 1: FAILED")
  fail_count += 1

# Reset temp.txt in between runs
subprocess.run("rm temp.txt", shell = True)

if fail_count != 0:
  exit(1)
