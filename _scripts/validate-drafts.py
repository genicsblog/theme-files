import os
import sys
import yaml
import requests
import frontmatter
from pathlib import Path

committer = sys.argv[1]

temp = open("temp.txt", "r")
files = temp.readlines()[0].split(" ")

total_files = len(files)

bypass_accounts = ["florianwalther-private"]

if total_files != 0:
    for file in files:
        file = file.strip()

        if(file.split("/")[0] != "_drafts"):
            raise Exception("File is outside the _drafts folder")

        post = frontmatter.load(file)

        with open("_data/authors.yml", "r") as authors:
            author = yaml.safe_load(authors)[post["author"]]["links"]["github"]

        author = author.lower()

        if committer.lower() not in bypass_accounts and author != committer.lower():
            raise AssertionError(f"Errors in {file}: File author ({post['author']}), committer ({committer}) and github account of author({author}) have conflicts.")

        url = "https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_drafts/" + file.split('/')[1]

        try:
            response = requests.get(url)

            if response.status_code == 200:
                tempMd = open("temp.md", "w")
                tempMd.write(response.text)

                tempMd = open("temp.md")

                yml = frontmatter.load(tempMd)
                existingDraftAuthor = yml["author"].lower()

                if author != existingDraftAuthor:
                    raise AssertionError(f"Committer tried to manipulate the author of {file}")

                os.remove("temp.md")

            elif response.status_code == 404:
                print(f"File not present on main branch, skipping...")

            else:
                raise Exception(f"Encountered error code {response.status_code} while reaching {url}. File may not be present on main branch.")

        except:
            raise Exception(f"Exception occured while reaching {url}")

        print(f"{file} is ok")

else:
    raise Exception("No changed files found.")
