define dso_local <TYPE> @main(i32) {

	; <label>: 93
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 3f
	%1 = load i32, i32* 3
	%3 = icmp gt i1 %1, 0
	br i1 %3 label 63 label 91

	; <label>: 63
	ret i32 2

	; <label>: 91
	%4 = icmp lt i1 %1, 0
	br i1 %4 label e6 label 1e

	; <label>: e6
	%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 1e
	ret i32 0
}