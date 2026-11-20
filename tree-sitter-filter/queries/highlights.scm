; Kata kunci
["and" "or" "not" "in" "contains"] @keyword

; Operator perbandingan
["=" "!=" ">" "<" ">=" "<="] @operator

; Jenis nilai
(string) @string
(number) @number
(boolean) @constant.builtin

; Nama field
(comparison
  field: (identifier) @property)

(in_expression
  field: (identifier) @property)

(contains_expression
  field: (identifier) @property)

; Tanda baca
["(" ")"] @punctuation.bracket
"," @punctuation.delimiter