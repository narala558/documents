utils:
  pkg.installed:
    - pkgs:
      - unzip
      - tree
      - htop
      - byobu


emacs:
  cmd.run:
    - cwd: /tmp
    - names:
      - sudo apt-get install build-essential
      - sudo apt-get build-dep emacs24
      - wget http://ftp.gnu.org/gnu/emacs/emacs-24.5.tar.xz
      - tar -xf emacs*
      - cd emacs-24.5 && ./configure
      - cd emacs-24.5 && make
      - cd emacs-24.5 && sudo make install
