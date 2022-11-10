# Drafts validation script - TEST 2
# These tests ensures that only a valid github account may
# may change a draft.

print("Test 2")
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

# Case 1: draft test.md is changed by committer gouravkhunger (VALID)
command = f"""
  echo '{draft_file}' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command returns 0
validate(case = 1, code = res.returncode, shouldBeZero = True)

# Reset temp.txt in between runs
subprocess.run("rm temp.txt", shell = True)

# Case 2: draft test.md is changed by committer kushagra (INVALID)
command = f"""
  echo '{draft_file}' >> temp.txt;
  python3.9 {folder}/{script} kushagra;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
validate(case = 2, code = res.returncode, shouldBeZero = False)

if fail_count != 0:
  exit(1)
