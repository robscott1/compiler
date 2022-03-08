
define dso_local i32 @foo(i32) {

	; <label>: 09
	%t1 = alloca i32

	; <label>: 39
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

	; <label>: 94
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: f7
	store i32 1, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4, label da, label 70

	; <label>: da
	ret i32 1

	; <label>: 70
	ret i32 1
}