#!/usr/bin/env bash

# Global variables
date_string="$(date +"%F %H:%M:%S")"
commit_message_submodule="${date_string} Automatic update!"
commit_message_main="${date_string} Automatic submodule tracking!"

fix-urls-in-file () {
  local file="${1}"
  sed -i -e 's/\/http/http/g' "${file}"
}

exit-message () {
  local message="${1}"
  echo "${message}"
  exit
}

git-submodule-management () {
  cd ./docs/ || exit-message "[ERROR] Failed to change directory;"
  echo "[INFO] Submodule add/commit/push changes;"
  git checkout master
  git commit -a -m "${commit_message_submodule}"
  git push origin master
  cd - || exit-message "[ERROR] Failed to return to main directory"
  echo "[INFO] Main project submodule tracking (commit only);"
  git add docs
  git commit -m "${commit_message_main}"
}

# Build site using Academic Hugo
echo "[INFO] Building site with Academic Hugo;"
hugo

# Fix URLs if needed
while read -r file; do
  echo "[INFO] Analysing file (${file});"
  fix-urls-in-file "${file}"
done < <(find docs -name '*.html')

# Add/commit submodule changes
git-submodule-management
