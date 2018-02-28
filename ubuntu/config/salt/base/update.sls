.git:
  pkg:
    - installed

# Clone os
.os:
  git.latest:
    - name: git://github.com/robbyrussell/oh-my-zsh.git
    - target: /home/anand/projects/ubuntu/os
    - require:
      - pkg: .git
