
define dso_local i32 @main(i32) {

	; <label>: 99
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 2a
	store 4 i32, i32* %t1

	; <label>: 72
	%t3 = load i32, i32* %t1
	%t4 = icmp lt i1 %t3, 4
	br i1 %t4 label 5f label 9f

	; <label>: 5f
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: bd
	br label 72

	; <label>: 9f
	ret i32 2
}