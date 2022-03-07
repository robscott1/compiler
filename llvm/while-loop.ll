define dso_local <TYPE> @main(i32) {

	; <label>: 12
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 73
	%1 = load i32, i32* 4

	; <label>: 76
	%3 = icmp lt i1 %1, 4
	br i1 %3 label 01 label 12

	; <label>: 01
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 4b
	br label 76

	; <label>: 12
	ret i32 2
}