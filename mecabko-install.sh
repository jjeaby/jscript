wget -O /tmp/mecab-0.996-ko-0.9.2.tar.gz  https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
tar -zxvf /tmp/mecab-0.996-ko-0.9.2.tar.gz -C /tmp
cd /tmp/mecab-0.996-ko-0.9.2
./configure
make
sudo make install

wget -O /tmp/mecab-ko-dic-2.1.1-20180720.tar.gz https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
tar -zxvf /tmp/mecab-ko-dic-2.1.1-20180720.tar.gz -C /tmp
cd /tmp/mecab-ko-dic-2.1.1-20180720
./autogen.sh
./configure
make
sudo make install
