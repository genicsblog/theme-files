set -e;

clean_up () {
  rm -rf _data _drafts temp.txt temp.yml;
};

trap clean_up EXIT;

clean_up;

# Run tests for author data validation script
echo "Author data validation script tests";
echo "-----------------------------------";
echo;

for file in _scripts/spec/authors/*.py; do
  wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_data/authors.yml -P _data -q;
  python3.9 $file;
  rm -rf _data temp.txt;
  echo;
done

rm -rf temp.txt;
echo;

# Run tests for drafts validation script
echo "Drafts validation script tests";
echo "------------------------------";
echo;

wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_data/authors.yml -P _data -q;

for file in _scripts/spec/drafts/*.py; do
  wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_drafts/test.md -P _drafts -q;
  python3.9 $file;
  rm -rf _drafts temp.txt;
done

clean_up;
