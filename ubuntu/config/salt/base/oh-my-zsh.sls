#!stateconf yaml . jinja

#
# ZSH Installation w/ Oh-My-Zsh
#

# Dependencies

.git:
  pkg:
    - installed

# Install ZShell

.zsh:
  pkg:
    - installed

# Clone oh-my-zsh
.oh_my_zsh:
  git.latest:
    - name: git://github.com/robbyrussell/oh-my-zsh.git
    - target: /home/anand/.oh-my-zsh
    - require:
      - pkg: .git
      - pkg: .zsh

#custom zsh
.custom-zsh:
  git.latest:
    - name: git://github.com/ChillarAnand/.custom-zsh.git
    - target: /home/anand/.custom-zsh
    - require:
      - pkg: .git
      - pkg: .zsh
    - watch:
      - file: /home/anand/.zshrc


/home/anand/.zshrc:
  file.symlink:
    - target: /home/anand/.custom-zsh/zshrc
    - unless: /home/anand/.zshrc

# Set ZSH as default shell

.default_shell:
  cmd:
    - run
    - name: "chsh -s /usr/bin/zsh anand"
    - require:
      - pkg: .zsh
