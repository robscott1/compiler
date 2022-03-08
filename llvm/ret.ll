
define dso_local i32 @foo(i32) {

	; <label>: 81
	%t1 = alloca i32

	; <label>: d2
	ret i32 %t1
}
define dso_local i32 @main(i32) {

	; <label>: db
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 5d
	%t1 = load i32, i32* 1
	%t3 = icmp gt i1 %t1, 0
	br i1 %t3 label e3 label 71

	; <label>: e3
	ret i32 1

	; <label>: 71
	ret i32 1
}