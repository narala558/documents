#! /bin/sh


package_exists()
{
    package=$1
   if dpkg --get-selections | grep -q "^$package[[:space:]]*install$" >/dev/null;
    then
        return 0
   fi
}


if ! package_exists 'apt-fast'; then
    echo 'aaaaaaaa';
fi

package_exists apt-fastoo

if ! pgrep 'minio'; then
    echo 'minio not running'
fi


echo "Done"
