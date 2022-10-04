import os
import sys
import yaml
import requests
import frontmatter
from pathlib import Path

committer = sys.argv[1]

file = "_data/authors.yml"
temp = open("temp.txt", "r")

bypass_accounts = ["florianwalther-private"]

def get_changed(newData, existingData):
    changed = set()
    for key in newData:
        if key not in existingData:
            changed.add(str(key))
        else:
            for subKey in newData[key]:
                if newData[key][subKey] != existingData[key][subKey]:
                    changed.add(str(key))
    return changed

if temp.readlines()[0].strip() == file:
    post = frontmatter.load("_data/authors.yml")

    with open(file, "r") as authorData:
        newData = yaml.safe_load(authorData)

    url = f"https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/{file}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            tempYml = open("temp.yml", "w")
            tempYml.write(response.text)

            tempYml = open("temp.yml")

            existingData = yaml.safe_load(tempYml)
            changed = set()

            if newData != existingData:
                changed = get_changed(newData, existingData).union(get_changed(existingData, newData))

            for author in changed:
                if author in existingData:
                    githubAccount = existingData[author]["links"]["github"]
                else:
                    githubAccount = newData[author]["links"]["github"]

                if committer not in bypass_accounts and githubAccount != committer:
                    raise Exception(f"Committer {committer} tried to change {author} who has GitHub username set to {githubAccount} in the YAML!")
                else:
                    print(f"{committer} is allowed to change {author}.")

            print("authors are valid!")

            os.remove("temp.yml")
        
        else:
            raise Exception(f"Encountered error code {response.status_code} while reaching {url}.")

    except:
        raise Exception(f"Exception occured while reaching {url}.")

    print(f"{file} is ok.")

else:
    raise Exception(f"Files other than {file} was changed too!")
