
define dso_local i32 @main(i32) {

	; <label>: 00
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 1b
	store i32 4, i32* %t1

	; <label>: 30
	%t3 = load i32, i32* %t1
	%t4 = icmp lt i1 %t3, 4
	br i1 %t4 label 41 label 3a

	; <label>: 41
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 91
	br label 30

	; <label>: 3a
	ret i32 2
}