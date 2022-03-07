define dso_local <TYPE> @main(i32) {

	; <label>: 66
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 5e
	%1 = load i32, i32* 3

	; <label>: f4
	br i1 true label 3b label 78

	; <label>: 3b
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label f7 label f9

	; <label>: f7
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: f9
	br label f4

	; <label>: 78
	ret i32 2
}