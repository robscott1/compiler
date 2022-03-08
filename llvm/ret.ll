
define dso_local i32 @foo(i32) {

	; <label>: 3a
	%t1 = alloca i32

	; <label>: f2
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

	; <label>: 15
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 89
	store i32 1, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4, label 11, label 96

	; <label>: 11
	ret i32 1

	; <label>: 96
	ret i32 1
}