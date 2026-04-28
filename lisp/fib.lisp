(defun fib-series (n)
  (let ((a 0) (b 1))
    (dotimes (i (+ n 1))
      (format t "~a " a)
      (psetq a b
             b (+ a b)))))

(defun main ()
  (format t "Enter n: ")
  (finish-output)
  (let ((n (read)))
    (fib-series n)
    (terpri)))   ;; move to next line

(main)