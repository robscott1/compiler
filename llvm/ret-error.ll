
define dso_local i32 @main(i32) {

	; <label>: f7
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 88
	store 3 i32, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4 label c1 label 1e

	; <label>: c1
	ret i32 2

	; <label>: 1e
	%t5 = load i32*, i32* %t1
	%t6 = icmp lt i1 %t5, 0
	br i1 %t6 label df label 2a

	; <label>: df
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 2a
	ret i32 0
}