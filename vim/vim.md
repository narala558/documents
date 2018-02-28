#### Reselect previous visual block
    gv
    

#### Restart vim without closing it - vim source
    :source ~/.vimrc


#### Surround Plugin
    cs"'
    cs'<p>
    cst"
    ds"
    ysiw]
    yss]
    VS<b>
    
#### NERDTree Plugin
    #File Node Mappings
    o   - open a file/directory 
    go  - preview a file
    i   - split file 
    gi  - split file preview
    s   - vertical split file
    gs  - vertical split file preview
    t   - open file in new tab
    T   - open file preview
    
    u - go up one directory from root 
    
    #Ignore files in nerdtree
    let NERDTreeIgnore = ['\.pyc']
    
#### Insert -> Normal + Run command -> Insert
    CTRL +  o command
    
#### Auto open nerdtree with vim
    autocmd VimEnter * NERDTree

#### Comment/Uncomment a block of code
    [Ctrl] + v, select lines -> I#[Esc]
    V, select lines -> :s/^/#

    [Ctrl] + v, select lines -> x 
