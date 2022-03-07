define dso_local <TYPE> @foo(i32) {

	; <label>: 7a
	%1 = alloca i32

	; <label>: d5
	ret i32 %1
}
define dso_local <TYPE> @main(i32) {

	; <label>: 37
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 2f
	%1 = load i32, i32* 1
	%3 = icmp gt i1 %1, 0
	br i1 %3 label 83 label 50

	; <label>: 83
	ret i32 1

	; <label>: 50
	ret i32 1
}