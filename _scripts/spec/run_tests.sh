# Run tests for author data validation script

echo "Author data validation script tests";
echo "-----------------------------------\n";

for file in _scripts/spec/authors/*.py; do
  wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_data/authors.yml -P _data -q;
  python3.9 $file;
  rm -rf _data;
  echo "\n";
done

rm -rf temp.txt;
echo "\n";

# Run tests for drafts validation script

echo "Drafts validation script tests";
echo "------------------------------\n";

wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_data/authors.yml -P _data -q;

for file in _scripts/spec/drafts/*.py; do
  wget https://raw.githubusercontent.com/genicsblog/genicsblog.com/main/_drafts/test.md -P _drafts -q;
  python3.9 $file;
  rm -rf _drafts;
done

rm -rf _data temp.txt;
