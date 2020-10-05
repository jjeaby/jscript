sudo apt update && sudo apt upgrade --yes
sudo apt install build-essential git python python-pip python3 python3-pip zsh nodejs vim tmux --yes
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
pip install -U pip
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
