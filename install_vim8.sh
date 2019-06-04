# If we would like to let the vim support ruby, we need to install the package
rpm -i https://rpmfind.net/linux/mageia/distrib/6/x86_64/media/core/updates/lib64ruby2.2-2.2.10-16.1.mga6.x86_64.rpm
# clone the vim dir
git clone git@github.com:vim/vim.git
cd vim
# Normally we do not need to remove cache, but If we .configure with different parameters,
# we need to clean the cache first then to configure it again
rm -rf src/auto/config.cache
# Usually, we have installed the lower version vim, then the following vim exists
# Let us remove it to avoid the failure
rm ~/.local/share/vim/vimrc
# Here I secify vim built with python3.6, if you are using different python, please adjust the python related parameters
# More, the enable-rubyinterp is not required to support python. I am using ruby, so I make it to support ruby.
./configure --enable-multibyte --enable-cscope --prefix=$HOME/.local --enable-rubyinterp=yes --with-python3-command=python3  --enable-pythoninterp=yes  --enable-python3interp=yes  --enable-gui=gtk3  --with-python3-config-dir=/usr/local/lib/python3.6/config-3.6m-x86_64-linux-gnu/ 
make install
echo "export PATH=$HOME/.local/bin:$PATH" >>~/.bashrc
echo "export alias vi=vim" >>~/.bashrc
ln -s /etc/vimrc $HOME/.local/share/vim #load system defaults for vim editing like syntax on
source ~/.bashrc
vim --version | grep python3
