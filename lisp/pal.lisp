(defun palindrome (n)
  (let ((original n)
        (rev 0))
    (loop while (> n 0) do
         (setq rev (+ (* rev 10) (mod n 10)))
         (setq n (floor n 10)))
    (if (= original rev)
        (format t "Palindrome~%")
        (format t "Not Palindrome~%"))))

(defun main ()
  (format t "Enter number: ")
  (finish-output)
  (let ((n (read)))
    (palindrome n)))

(main)