# Authors data validation script - TEST 2
# This test ensures that only the github account associated with an author
# in the data file should be allowed to change its content.

print("Test 2")
print("------")

import copy
import yaml
import subprocess

fail_count = 0
folder = "_scripts"
script = "validate-authors.py"
data_file = "_data/authors.yml"

def validate(case, code, shouldBeZero):
  global fail_count

  if((code == 0 and shouldBeZero) or (code != 0 and not shouldBeZero)):
    print(f"Case {case}: PASSED")
  else:
    print(f"Case {case}: FAILED")
    fail_count += 1

with open(data_file, "r") as authorData:
  data = yaml.safe_load(authorData)

preserved = copy.deepcopy(data)

def dump(data):
  with open(data_file, 'w') as authorData:
    yaml.dump(data, authorData)

def reset():
  dump(preserved)
  data = copy.deepcopy(preserved)
  subprocess.run("rm temp.txt", shell = True)

# Case 1: author gouravkhunger is changed by commiter gouravkhunger (VALID)
data["gouravkhunger"]["name"] = "ABCDEF"

dump(data)

command = f"""
  echo '{data_file}' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command returns 0
validate(case = 1, code = res.returncode, shouldBeZero = True)

reset()

# Case 2: author kushagra is changed by commiter gouravkhunger (INVALID)
data["kushagra"]["name"] = "ABCDEF"

dump(data)

command = f"""
  echo '{data_file}' >> temp.txt;
  python3.9 {folder}/{script} gouravkhunger;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
validate(case = 2, code = res.returncode, shouldBeZero = False)

reset()

# Case 3: author gouravkhunger is changed by commiter kushagra (INVALID)
data["gouravkhunger"]["links"]["stackoverflow"] = "1000101"

dump(data)

command = f"""
  echo '{data_file}' >> temp.txt;
  python3.9 {folder}/{script} kushagra;
"""
res = subprocess.run(command, capture_output = True, shell = True)

# The above case should pass if the command does not return 0
validate(case = 3, code = res.returncode, shouldBeZero = False)

reset()

if fail_count != 0:
  exit(1)
