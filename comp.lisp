(defmacro string-case (v) (concatenate 'string "case " v ":"))
(defmacro string-case-lookup (k v var) (concatenate 'string (string-case k) " " var " = " v "; break;"))
(def main (print (string-case-lookup "40" "20" "seed")))
