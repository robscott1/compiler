
define dso_local i32 @foo(i32) {

	; <label>: a2
	%t1 = alloca i32

	; <label>: 2e
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

	; <label>: 22
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 82
	store i32 1, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp sgt i1 %t3, 0
	br i1 %t4, label bf, label 55

	; <label>: bf
	ret i32 1

	; <label>: 55
	ret i32 1
}