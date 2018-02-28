http 'https://api.github.com' --auth=$USER:$GITHUB_TOKEN --style emacs


http 'https://api.github.com/orgs/project-chalam/teams' --auth=$USER:$GITHUB_TOKEN --style emacs
http 'https://api.github.com/teams/2365317/members' --auth=$USER:$GITHUB_TOKEN --style emacs
http 'https://api.github.com/teams/2323659/members' --auth=$USER:$GITHUB_TOKEN --style emacs

http 'https://api.github.com/user/keys' --auth=$USER:$GITHUB_TOKEN --style emacs

http 'https://api.github.com/orgs/project-chalam/teams' --auth=$USER:$GITHUB_TOKEN --style emacs

http 'https://api.github.com/orgs/user/following' --auth=$USER:$GITHUB_TOKEN --style emacs


hit GET '/user/following'
hit GET '/user/emails'
hit GET '/gists'
hit GET '/gists/public'
hit GET '/rate_limit'
