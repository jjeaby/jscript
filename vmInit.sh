sudo apt update && sudo apt upgrade --yes
sudo apt install build-essential git python3 python-pip zsh nodejs vim tmux --yes
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
pip install -U pip

