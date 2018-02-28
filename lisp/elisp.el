;;; elisp --- simple elisp



;;; BASICS



;; assign value to a symbol
(defparameter vern 11)

(defvar version 11)

(set 'version "24.3")

(setq version 11)

(setq editor "emacs" version "24.3")    ; this is a comment





;; use let for local variables
(let (a b)
  (setq a 3)
  (setq b 4)
  (+ a b))

(let ((a "3"))
  a)

(setq y 2)

(let ((y 1)
      (z y))
  (list y z))

(let* ((y 1)
       (z y))    ; Use the just-established value of y.
  (list y z))






;;; list operations

;; list is a sequence of zero or more lisp exp enclosed in parens
()

'( (1 2 3))

;; car returns first element of the list.
(car '(a b c d))

;; cdr returns first element of the list.
(cdr '(a b c d))
(cdr '(a b))
(car (cdr '(a b)))

;; append items
(append '(1 2 3) '(a b c d))
(append '(1 2 3) 4)
(append '(1 2 3) )

(setq list1 '(1 2 3))
(add-to-list 'list1 4)



;; list - make list from arguments
(list 'a 'x "asdf" 6)

(setq ll '("elisp.el" "test"))
(remove (buffer-name) ll)
(message "%s" ll)



;; printing
(message "Master emacs")
(message "emacs version %s" "24.3")

;; arithmetic
(- 9 2 3)
(expt 2 3)

(integerp 3.)
(floatp 3.)

;; true false
(if nil "yes" "no")
(if () "yes" "no")
(if '() "yes" "no")
(if (list) "yes" "no")
(if t "yes" "no")
(if 0 "yes" "no")
(if "" "yes" "no")
(if [] "yes" "no")
(and t nil)
(or t nil)



(unless (not nil)
  (message "foo"))

(unless "foo"
  (message "bar"))

(unless nil
  (message "bar"))

(setq res "aa")
(setq res nil)
(and res (stringp res))

(equal (length '("a" "b")) 2)

(unless (and res (stringp res))
  (message "fffffff"))

;; hash
(make-hash-table)
(setq h (make-hash-table :test #'equal))
(puthash "foo" "bar" h)
(puthash "python" "elpy" h)
(puthash "p" "q" h)
(dolist (k (hash-table-keys h))
  (message k))





;; strings
(defun string )

(string-equal "r" "r")

(stringp "r")
(stringp "")

(format "%s - %s" "foo" "bar")





;; testing

(defun  add (x y)
  (+ x y))

(add 3 4)

(ert-deftest add-test ()
  (should (= 7 (add 3 4))))


;; order
(defun x ()
    (x))

(defun test(x y)
  (if (= x 0)
      0
    y))


(test 0 (x))



(call-process "/bin/bash" nil t nil "-c" "ls -t ~/test.el *.txt | head -5")

(with-temp-buffer foo)
(call-process "/bin/bash" nil t nil "-c"
              "pandoc -o test.html test.md")


(shell-command (format "%s -o %s %s"
                       "pandoc"
                       "test.html"
                       "test.md"
                       )
               )

(get-buffer-process (buffer-file-name))

(current-dired)

(defun im-is-markdown-bufferp ()
  "return t if opened buffer is markdown"
  (member (downcase (file-name-extension (buffer-file-name)))
          '("md", "markdown")))

(defun im-serve-file (file)
  (with-current-buffer (get-buffer file)
    (httpd-start)
    (impatient-mode)
    (browse-url (concat im-server-url temp-file))))

(im-serve-file "/home/anand/projects/lisp/impatient-markdown/test.html")

(get-buffer-create "/home/anand/projects/lisp/impatient-markdown/test.html")

(forward-block 2)

(defun forward-block (&optional n)
  (interactive "p")
  (let ((n (if (null n) 1 n)))
    (search-forward-regexp "\n[\t\n ]*\n+" nil "NOERROR" n)))

(concat im-server-url "ff")

(browse-url "http://127.0.0.1:8080/imp/")


;; conditioanls
(if (not (require 'elpy))
    (message "elpy is not installed")
  (message "elpy is installed"))

(when (not (require 'elpy))
  (message "elpy is not installed")
  (message "go for next package."))

(cond
 (1 2aa)
 (2 2))

(defun changed (&rest args)
  (message "changed"))

(add-hook 'after-change-functions 'changed nil t)

(dolist (buf impatient-markup-buffers-list)
  (shell-command (format "%s -o %s %s"
                         impatient-markup-pandoc
                         (impatient-markup-make-html-file buf)
                         (buffer-file-name buf)))
  (message "updated")
  )

(equal "abc" "abc")
(not (equal 3 4))


;; group a bunch of expressions
(progn (message "a") (message "b"))


;; iteration
(setq x 0)

(while (< x 4)
  (print (format "yay %d" x))
  (setq x (1+ x)))


;; dolist
(setq animals '(gazelle giraffe lion tiger))
(dolist (element animals)
  (message "%s" element))

(defun print-list (list)
  (dolist (element list)
    (message "%s" element)))

(defun efoo ()
  (interactive)
  (dolist (buf (list-buffers))
    (with-current-buffer buf
      (dolist (mod minor-mode-alist)
        (member elpy-mode (car mod))))))

(describe-mode (current-buffer))
(member lispy-mode minor-mode-list)
(member lispy-mode minor-mode-alist)
(member elpy-mode minor-mode-alist)

(let (value)
  (dolist (element animals value)
    (message "%s" value)
    (message "%s" animals)))

(defun reverse-list-with-dolist (list)
  "Reverse elements with dolist"
  (let (value)
    (dolist (element list value)
      (setq value (cons element value)))))

(reverse-list-with-dolist animals)

(unless (< 2 3)
  (message "body execute"))

(unless nil
  (message "body execute"))

(unless t
  (message "body execute"))

(while nil
  (message "body execute"))

(defun imp--notify-clients ()
  (interactive)
  (while imp-client-list
    (imp--send-state-ignore-errors (pop imp-client-list))))

(unless t
  (message "body execute"))

;; try catch
(condition-case nil
    (progn
      (asaa)
      (message "running try "))
  (error
   (message "catched error")))

(eql "r" "ar")
(eql "r" "r")

(eq "r" "r")



;; strings
(string-equal "r" "r")

(replace-regexp-in-string "\n$" "" "a \n b \n")

(defun double-space-cleanup  ()
  (interactive)
  (goto-char (point-min))
  (while (/= (point) (point-max))
    (just-one-space)
    (forward-word)))

(case (char-to-string 114)
  ("r"
   (message "r"))
  ("i"
   (message "i"))
  (otherwise
   "Something else"))

;; functions inbuilt
(defun cr (choice)
  (interactive "c[a]: a  [b]:b")
  (cond
   ((string-equal choice "i")
    (message "i"))
   (t
    (message "foo"))))


(cl-letf (((symbol-function 'message) (lambda (&rest _) nil)))
  (message "hello"))

(defun test (&optional foo)
  (interactive "P")
  (if foo
      (message "foo")
    (message "bar")))

(insert-button "fsf"
               'action (lambda (x) (browse-url (button-get x 'url)))
               'url "http://www.fsf.org")

(push (cons "pyml" "*.py *.htm *.html") grep-files-aliases)


(defun save-buffer-without-message (&optional arg)
  (interactive "p")
  (let ((modp (buffer-modified-p))
        (make-backup-files (or (and make-backup-files (not (eq arg 0)))
                               (memq arg '(16 64)))))
    (and modp (memq arg '(16 64)) (setq buffer-backed-up nil))
    (basic-save-buffer)
    (and modp (memq arg '(4 64)) (setq buffer-backed-up nil))))


;; functions
(defun yay ()
  "Insert “Yay!” at cursor position."
  (insert "Yay!"))

(defun yay ()
  "Insert “Yay!” at cursor position."
  (interactive)
  (insert "Yay!"))

(defun myFunction (myArg)
  "Prints the argument"
  (interactive "p")
  (message "Your argument is: %d" myArg))

(defun myFunction (myStart myEnd)
  "Prints region start and end positions"
  (interactive "r")
  (message "Region begin at: %d, end at: %d" myStart myEnd))

(defun add-number (x y)
  "Add two numbers"
  (interactive)
  (message (+ x y)))
(add-number)


(defun add-number (x y)
  "…"
  (interactive "nN1: \n N2: \n")
  (message "sum is %d" (+ x y)))

(describe-function-1 'describe-function)
(describe-function-1 describe-function)
(describe-function)

(defun foo ()
  "fffffffff"
(message "%s" "aa"))
(message "%s" (find-lisp-object-file-name function 'foo))
(message "%s" (find-lisp-object-file-name 'foo function))
(message "%s" (find-lisp-object-file-name function #'describe-function))

(find-lisp-object-file-name #'describe-function function)
(find-lisp-object-file-name #'describe-function "elpy")
(find-lisp-object-file-name #'describe-function "elpy")


(help-make-xrefs "*Help*")
(help-make-xrefs "elisp.el")


(defun add-numbers (x y &optional z)
  (if z
      (+ x y z))
  (+ x y)
  )
(add-numbers 1 2 3)
(add-numbers 1 2)

(forward-line 1)
(forward-line 0)
(forward-line)
(forward-line -1)

(beginning-of-line)
(goto-char end)


(push-mark )
;; timers
(defun foo ()
  (interactive)
  (message "foo"))

(timer-create)

(print timer-list)
(print timer-idle-list)

(setq test-timer
      (run-with-idle-timer 5 t 'foo))
(setq test-timer
      (run-with-idle-timer 5 t 'foo))

(cancel-timer test-timer)

(seconds-to-time (nth 2 'test-timer))

(helm-elisp--format-timer test-timer)

(defun helm-elisp--format-timer (timer)
  (format "%s repeat=%s %s(%s)"
          (let ((time (timer--time timer)))
            (if (timer--idle-delay timer)
                (format-time-string "idle-for=%5s" time)
              (format-time-string "%m/%d %T" time)))
          (or (timer--repeat-delay timer) "nil")
          (mapconcat 'identity (split-string
                                (prin1-to-string (timer--function timer))
                                "\n") " ")
          (mapconcat 'prin1-to-string (timer--args timer) " ")))

(defclass helm-idle-time-timers-class (helm-source-sync helm-type-timers)
  ((candidates :initform timer-idle-list)
   (allow-dups :initform t)
   (volatile :initform t)
   (filtered-candidate-transformer
    :initform
    (lambda (candidates _source)
      (cl-loop for timer in candidates
               collect (cons (helm-elisp--format-timer timer) timer))))))



;;(get-universal-time)
(current-time-string)
(current-time)



;; helm

(defvar helm-source-commands-history
  (helm-build-sync-source "Emacs commands history"
    :candidates (lambda ()
                  (let ((cmds))
                    (dolist (elem extended-command-history)
                      (push (intern elem) cmds))
                    cmds))
    :coerce #'intern-soft
    :action #'command-execute)
  "Emacs commands history")
(helm :sources helm-source-commands-history)
(setq helm-echo-input-in-header-line t)

(defun hello ()
  (message "hello"))

(defun helm-selection-user-choice (orig &rest args)
  (let ((result (apply orig args)))
    (when result
      (hello))
    result))

(advice-add 'helm-comp-read--move-to-first-real-candidate :around #'helm-selection-user-choice)
(advice-add 'helm-after-update-hook :around #'helm-selection-user-choice)

(setq f-loc1 "/foo/bar" f-loc2 f-loc1)


(defun strip-text-properties(txt)
  (set-text-properties 0 (length txt) nil txt)
  txt)

(setq auto-capitalize-words '(1))

(defun add-to-autocapitalize-words ()
  "Add word at point to auto-capitalize-words list."
  (interactive)
  (add-to-list 'auto-capitalize-words
               (strip-text-properties (thing-at-point 'word))))




(defun tap ()
  "Add word at point to auto-capitalize-words list."
  (interactive)
  (thing-at-point 'word))


(defun foo ()
  (message "foo"))

(add-hook 'buffer-list-update-hook 'foo)


(helm :sources helm-source-emacs-commands)
(defvar helm-source-emacs-commands
  (helm-build-sync-source "Emacs commands"
    :candidates (lambda ()
                  (let ((cmds) (h-cmds))
                    (mapatoms
                     (lambda (elt) (when (commandp elt) (push elt cmds))))
                    (dolist (elem extended-command-history)
                      (push (intern elem) h-cmds))
                    (append h-cmds cmds)))
    :coerce #'intern-soft
    :action #'command-execute)
  "A simple helm source for Emacs commands.")

(commandp 'gnus-score-mode)


(setq elem "foo")
(setq helm-commands-history-source nil)
(setq helm-commands-history-source (append '(intern elem) helm-commands-history-source))


(helm :sources (let ((cmds  ()))
                 (mapatoms (lambda (s) (when (commandp s) (push s cmds))))
                 cmds))

(helm
 :sources '(helm-source-dired-recent-dirs)
 :buffer buf)

(helm
 :sources '(1 2 3)
 :buffer buf)


(defun xx ()
  "print current word."
  (interactive)
  (message "%s" (thing-at-point 'word)))

(defun xx2 ()
  "print current word."
  (interactive)
  (let (p1 p2)
    (save-excursion
      (skip-chars-backward "-a-z0-9./")
      (setq p1 (point))
      (skip-chars-forward "-a-z0-9./")
      (setq p2 (point))
      (message "%s" (buffer-substring-no-properties p1 p2)))))

"(or (> (nth 0 (syntax-ppss)) 0) (nth 3 (syntax-ppss)))"
(syntax-ppss '(193, 12))
(nthcdr 3 '(1 2  3 4 5))
(cdr '(1 2  3 4 5))
(nth 3 '(1 2 3 4 5))


(defun point-inside-string-or-comment ()
  "This is it."
  (interactive)
  (let ((ppss (syntax-ppss)))
    (or (car (setq ppss (nthcdr 3 ppss)))
        (car (setq ppss (cdr ppss)))
        (nth 3 ppss))))

(defun foo ()
  (interactive)
  (or (> (nth 0 (syntax-ppss)) 0)
      (nth 3 (syntax-ppss))))

(elpy-doc--symbol-at-point)

(defun goto-template ()
  (interactive)
  (save-excursion
    (let ((beg (+ (search-backward-regexp "['\"]") 1))
          (end nil)
          (file nil))
      (forward-char)
      (search-forward-regexp "['\"]")
      (setq end (- (point) 1))
      (kill-ring-save beg end)
      (setq file (current-kill 0))
      (find-file (expand-file-name
                  (dolist (f (projectile-current-project-files))
                    (if (s-contains? file f)
                        (return f)))
                  (projectile-project-root))))))

(defun test-inside-curly-braces ()
  (interactive)
  (when (and (looking-back "\"") (looking-at  "\""))
    (message "inside curly braces")))





(defun inside-string ()
  "Returns non-nil if inside string, else nil.
This depends on major mode having setup syntax table properly."
  (interactive)
  (nth 3 (syntax-ppss)))


(defun get-thing-at-point ()
  (interactive)
  (message (thing-at-point 'filename)))

(defun inside-string? ()
  "Returns non-nil if inside string, else nil.
This depends on major mode having setup syntax table properly."
  (interactive)
  (let ((result (nth 3 (syntax-ppss))))
    (message "%s" result)
    result))

(defun beginning-of-string ()
  "Moves to the beginning of a syntactic string"
  (interactive)
  (unless (point-in-string-p (point))
    (error "You must be in a string for this command to work"))
  (while (point-in-string-p (point))
    (forward-char -1))
  (point))

(defun qq ()
  "Moves to the beginning of a syntactic string"
  (interactive)
  (unless (point-in-string-p (point))
    (error "You must be in a string for this command to work"))
  (while (point-in-string-p (point))
    (forward-char -1))
  (progn
    (point)
    (point)))

(defun foo ()
  (interactive)
  (let ((beg (python-nav-beginning-of-statement))
        (end (python-nav-end-of-statement)))
    (elpy-shell-get-or-create-process)
    (python-shell-send-string (buffer-substring beg end)))
  ;; (python-shell-send-string "print('a')")
  )

(defun bar()
  (interactive)
  (python-shell-send-string (buffer-string) "print('a')"))

(next-line -1)
(previous-line -1)

(* 2 3)

(defun move ()
  (interactive)
  (let  (indent (current-indentation))
    (while (eq indent (current-indentation))
      (next-line)))
  (previous-line))

(while
    )
(search-forward-regexp ".")
(buffer-file-name)
(setq test-str )
(string-match "eliz" buffer-file-name)
(string-match tramp-file-name-regexp buffer-file-name)

(goto-char (nth 8 (syntax-ppss)))

(point)
(mark)
(current-buffer)

(helm :sources helm-source-commands-history)

{ "(test-inside-curly-braces)" }

(setq real-auto-save-timer (timer-create))
(timer-set-time real-auto-save-timer (current-time)
                real-auto-save-interval)

(buffer-string)

(timer-set-function real-auto-save-timer 'real-auto-save)
(timer-activate real-auto-save-timer)



(shell-command-to-string (concat "locate " (current-word) "|head -c -1" ))

(shell-command (format "%s"  "ls") "*scratch*")


(get-buffer-create  (concat (downcase (file-name-sans-extension buf)) ".html"))

(setq buf "/home/anand/projects/lisp/impatient-markup/README.md")


(defun goto-file ()
  "open file under cursor"
  (interactive)
  (find-file (shell-command-to-string (concat "locate " (current-word) "|head -c -1" )) ))


;; connect to server sql
(sql-mysql (setq sql-user "root" sql-password "bacillus123"
                 sql-database "pearl" sql-server "192.168.0.100"))


;; check for files & load them
(defun load-file-if-exists (list)
  "Check for file & load it."
  (let (value)
    (dolist (element list value)
      (if (file-exists-p element)
          (load-file (expand-file-name e lement prelude-personal-dir))))))

(load-file-if-exists '("config.el" "kbd.el" "packages.el" "prelude-modules.el"))


;; mysql
(setq sql-mysql-login-params
      '((user :default "root")
        (database :default "pearl")
        (server :default "192.168.0.110")
        (port :default 5432)))


sort-lines
delete-trailing-whitespaces
count-words  # word count on current buffer

(defalias 'qrr 'query-replace-regexp)

(unless (file-exists-p "file.txt") (shell-command "touch file.txt"))


;;; variables
package-activate-list  - list of installed packages



(defvar elpy-config--get-config "import json
import sys

try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

from distutils.version import LooseVersion

config = {}
json.dump(config, sys.stdout)
")


(define-minor-mode esc-mode
  "Toggle esc-keys mode.
   A minor mode so that my key settings override annoying major modes."
  t " esc" 'esc-mode-map)



(recenter-top-bottom 0)
(set-window-start (selected-window) (point))


(make-button 1 50 'action (lambda(x) (find-file "~/test.py")))


;; org mode
[[;; ./book.jpg]]
[[./book.jpg]]
[[./book.jpg]]
[[./book.jpg]]



;;; elisp.el ends here
