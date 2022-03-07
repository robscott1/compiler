define dso_local <TYPE> @foo(i32) {

	; <label>: 23
	%1 = alloca i32

	; <label>: 59
	ret i32 %1
}
define dso_local <TYPE> @main(i32) {

	; <label>: aa
	%1 = alloca i32
	%2 = alloca i32

	; <label>: e5
	%1 = load i32, i32* 1
	%3 = icmp gt i1 %1, 0
	br i1 %3 label 88 label 0d

	; <label>: 88
	ret i32 1

	; <label>: 0d
	ret i32 1
}