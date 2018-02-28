#! /bin/sh

sync_repo()
{
    echo "Syncing " $1
    path=$1
    cd $1
    git pull origin master -q
    git push origin master -q
    echo "Done."
}

echo "Syncing repos..."
sync_repo ~/.emacs.d/
sync_repo ~/.os/
