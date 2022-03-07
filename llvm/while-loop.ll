define dso_local <TYPE> @main(i32) {

	; <label>: 6c
	%1 = alloca i32
	%2 = alloca i32

	; <label>: d8
	%1 = load i32, i32* 4

	; <label>: a0
	%3 = icmp lt i1 %1, 4
	br i1 %3 label 9b label e2

	; <label>: 9b
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: ae
	br label a0

	; <label>: e2
	ret i32 2
}