#!/usr/bin/env bash

set -eu

if [[ $# -eq 0 ]] ; then
    echo "usage: $0 [VERSION]"
    exit 0
fi

version=$1

if [[ ${version:0:1} != "v" ]] ; then
    version="v${version}"
fi

echo "updating f1viewer.spec"
sed -i "s/Version:        [0-9\.]*/Version:        ${version:1:100}/g" f1viewer.spec
sed -i "s/Release:        [0-9]*%/Release:        1%/g" f1viewer.spec
sed -i "s/%changelog/%changelog\n\* $(date '+%a %b %d %Y') SoMuchForSubtlety <jakob@ahrer.dev> - ${version:1:100}-1\n- bump release to ${version:1:100}/g" f1viewer.spec


echo "committing changes"
git add f1viewer.spec
git commit -m "update to ${version}"

echo ""
echo "run 'git push' to publish new version"