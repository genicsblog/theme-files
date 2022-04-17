import os
import sys
import yaml
import requests
import frontmatter
from pathlib import Path

file = "_data/authors.yml"
temp = open("temp.txt", "r")

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
                for key in newData:
                    if key not in existingData:
                        changed.add(str(key))
                    else:
                        for subKey in newData[key]:
                            if newData[key][subKey] != existingData[key][subKey]:
                                changed.add(str(key))

                for key in existingData:
                    if key not in newData:
                        changed.add(str(key))
                    else:
                        for subKey in existingData[key]:
                            if existingData[key][subKey] != newData[key][subKey]:
                                changed.add(str(key))

            for author in changed:
                if author in existingData:
                    githubAccount = existingData[author]["links"]["github"]
                else:
                    githubAccount = newData[author]["links"]["github"]

                if githubAccount != sys.argv[1]:
                    raise Exception(f"Committer {sys.argv[1]} tried to change {author} who has GitHub username set to {githubAccount} in the YAML!")
                else:
                    print(f"{sys.argv[1]} is allowed to change {author}.")

            print("authors are valid!")

            os.remove("temp.yml")
        
        else:
            raise Exception(f"Encountered error code {response.status_code} while reaching {url}.")

    except:
        raise Exception(f"Exception occured while reaching {url}.")

    print(f"{file} is ok.")

else:
    raise Exception(f"Files other than {file} was changed too!")
