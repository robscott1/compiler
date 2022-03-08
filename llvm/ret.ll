
define dso_local i32 @foo(i32) {

	; <label>: LABEL@91
	%t1 = alloca i32

	; <label>: LABEL@b4
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

	; <label>: LABEL@0d
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: LABEL@e7
	store i32 1, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp sgt i1 %t3, 0
	br i1 %t4, label LABEL@64, label LABEL@f0

	; <label>: LABEL@64
	ret i32 1

	; <label>: LABEL@f0
	ret i32 1
}