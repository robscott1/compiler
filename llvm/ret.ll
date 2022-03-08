
define dso_local i32 @foo(i32) {

	; <label>: 04
	%t1 = alloca i32

	; <label>: 2e
	%t2 = load i32, i32* %t1
	ret i32* %t2
}
define dso_local i32 @main(i32) {

	; <label>: c5
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 9d
	store 1 i32, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4 label 8f label 2b

	; <label>: 8f
	ret i32 1

	; <label>: 2b
	ret i32 1
}