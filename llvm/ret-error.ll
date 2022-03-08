
define dso_local i32 @main(i32) {

	; <label>: 6a
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: bb
	store i32 3, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4 label 74 label b2

	; <label>: 74
	ret i32 2

	; <label>: b2
	%t5 = load i32, i32* %t1
	%t6 = icmp lt i1 %t5, 0
	br i1 %t6 label 3c label ef

	; <label>: 3c
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: ef
	ret i32 0
}