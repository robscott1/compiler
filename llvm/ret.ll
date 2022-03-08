
define dso_local i32 @foo(i32) {

	; <label>: 01
	%t1 = alloca i32

	; <label>: ad
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

	; <label>: 25
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: fe
	store 1 i32, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4 label 2a label ed

	; <label>: 2a
	ret i32 1

	; <label>: ed
	ret i32 1
}