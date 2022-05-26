tech used by kubenetes website

from: https://github.com/gohugoio/hugo
from: https://gohugo.io/getting-started/installing/
sudo apt install hugo
or
docker pull klakegg/hugo

hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo theme = \"ananke\" >> config.toml

hugo new posts/my-first-post.md



hugo server --bind=130.245.4.176 --baseURL=http://130.245.4.176:1313

## new theme
git clone https://github.com/panr/hugo-theme-terminal.git themes/terminal
