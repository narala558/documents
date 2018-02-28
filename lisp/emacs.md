## Emacs


#### Key bindings


```cl
emacs -nd  # start emacs in terminal
emacs -q   # start emacs without init file


;; set global key binding
(global-set-key (kbd "C-x C-t") 'sh-send-line-or-region)
```

# control

    C-u  # prefix argument
    C-/ (C-_ or C-x u)  undo
    C-+  # increase font size
    C--  # decrease font size
    C-o  open-line

    C-x m  eshell  # launch inferior shell
    C-x M-m  shell  # launch default shell

    C-x z  repeat  # Repeat last command
    C-x h  mark-whole-buffer
    C-x g  magit-status

    C-x C-s save-buffer  # Save file


# help


    C-h    help
    C-h A  apropos  patterns matching word
    C-h c  describe-key-briefly
    C-h f  display documentation for given functions
    C-h k  describe-key
    C-h l  view-lossage  display last 300 input keystroke
    C-h r  emacs manual
    C-h w  where-is

    C-c C-h   show all key binding that start with C-c


# windows


    C-x 0  delete-window
    C-x 1  delete-other-windows
    C-x 2  split-window-below
    C-x 3  split-window-right
    C-x 4  # prefix to deal with files in other window
    C-x 4 f ido-find-file-other-window


# macros


    C-x ( Start a macros
    C-x ) Stop macro
    C-x e execute a macro
    C-u 5 C-x e  # execute macro 5 times


# narrowing

    C-x n n  nnarrow-to-region
    C-x n d  py-narrow-to-defun
    C-x n p  narrow-to-region
    C-x n w  widen


# bookmarks

    C-x r m <RET>  bookmark-set
    C-x r b <bookmark> <RET>  bookmark-jump
    C-x r l  list-bookmarks


# meta


    M-!  # run a shell command
    M-;  # comment/uncomment selected region
    M-^  delete-indentation

    M-g g (M-g M-g)  goto-line
    M-u  uppercase-word
    M-x  # run command by name
    M-t  # transpose words


# functions

```
# open url
browse-url

# show line numbers
linum-mode
```



### packages



#### org mode

```cl
# align table at point based on vertical bars.
org-table-align

# delete column
org-table-delete-column

# show agenda menu
M-x org-agenda

TAB/S-TAB  - fold/unfold
M-up/down  - move a headline up or down
M-left/right  - promote or demote a headline
M-RET  - insert a new headline
M-x org-reload

# sort
org-sort


# embed images
[[./book.jpg]]

```



#### ace-jump-mode

```cl
# ace-jump-mode
C-c j <char> <char>
```

### dired mode

```cl
# open dir dired mode
C-x d
M-x find-dired
```

# elpy mode

```cl
# elpy-find-file
C-c C-f
```


#### expand-region

```cl
# expand-region
C-=
```


#### helm

```cl
C-c h l  helm-locate-files
C-c C-i  helm-copy-to-buffer
C-c h g  helm-do-grep
C-c h b  helm-resume
C-x b    helm-mini
```

#### Magit

```
C-x g  # magit-status
```

#### multiple-cursors

```cl
(require 'multiple-cursors)

(global-set-key (kbd "C-c m e") 'mc/edit-lines)
(global-set-key (kbd "C-c m n") 'mc/mark-next-like-this)
(global-set-key (kbd "C-c m p") 'mc/mark-previous-like-this)
(global-set-key (kbd "C-c m a") 'mc/mark-all-like-this)
```

```
```

#### paredit

```cl
M-(  # paredit-wrap-around-curly
M-"  # paredit-meta-doublequote
```


#### web-mode

```cl
M-;      # web-mode-comment-or-uncomment

C-c C-n  # web-mode-navigate
C-c C-f  # web-mode-fold-or-unfold
C-c C-s  # web-mode-snippet-insert
C-c C-m  # web-mode-mark-expand
```
