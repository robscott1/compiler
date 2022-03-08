
define dso_local i32 @main(i32) {

	; <label>: 77
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 28
	%t1 = load i32, i32* 3
	%t3 = icmp gt i1 %t1, 0
	br i1 %t3 label e0 label b8

	; <label>: e0
	ret i32 2

	; <label>: b8
	%t4 = icmp lt i1 %t1, 0
	br i1 %t4 label a8 label 5e

	; <label>: a8
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 5e
	ret i32 0
}