#!/usr/bin/env bash

fix-urls-in-file () {
  local file="${1}"
  sed -i -e 's/\/http/http/g' "${file}"
}

# Build site using Academic Hugo
echo "Building site with Academic Hugo;"
hugo

# Fix URLs if needed
while read -r file; do
  echo "Analysing file (${file});"
  fix-urls-in-file "${file}"
done < <(find docs -name '*.html')
