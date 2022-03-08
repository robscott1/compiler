
define dso_local i32 @main(i32) {

	; <label>: 7c
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: d6
	store 4 i32, i32* %t1

	; <label>: 7d
	%t3 = load i32, i32* %t1
	%t4 = icmp lt i1 %t3, 4
	br i1 %t4 label c0 label d1

	; <label>: c0
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 16
	br label 7d

	; <label>: d1
	ret i32 2
}