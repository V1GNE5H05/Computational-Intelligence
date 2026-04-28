(defun area-of-circle ()
  (format t "~%Enter Radius: ")
  (let* ((radius (read))
         (area (* pi radius radius)))
    (format t "~%Radius = ~F~%Area = ~F~%" radius area)))

(area-of-circle)