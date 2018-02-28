;; (setq lexical-binding t) or ;; -*- lexical-binding: t -*-



(defvar myticker nil)

(let ((x 0))
  (setq myticker (lambda ()
                   (setq x (1+ x)))))

(funcall myticker)


;;; lexical-binding.el ends here
