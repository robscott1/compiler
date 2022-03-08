
define dso_local i32 @foo(i32) {

	; <label>: 81
	%1 = alloca i32

	; <label>: d2
	ret i32 %1
}
define dso_local i32 @main(i32) {

	; <label>: db
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 5d
	%1 = load i32, i32* 1
	%3 = icmp gt i1 %1, 0
	br i1 %3 label e3 label 71

	; <label>: e3
	ret i32 1

	; <label>: 71
	ret i32 1
}