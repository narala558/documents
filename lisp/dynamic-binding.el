;; dynamic binding

;;; Code:

(defvar x 100)

(defun getx ()
  x)

(getx)

(let ((x 1))
  (getx))

(getx)


;; http://www.gnu.org/software/emacs/emacs-paper.html#SEC17
(defun foo1 (x) (foo2))
(defun foo2 () (+ x 5))
(foo1 12)

;; foo1 binds the variable x. All subroutines called by foo1 see the binding made by foo1,
;; instead of the global binding, which we say is shadowed temporarily until foo1 returns


;;; dynamic-binding.el ends here
