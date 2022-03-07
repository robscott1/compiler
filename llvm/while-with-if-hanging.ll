define dso_local <TYPE> @main(i32) {

	; <label>: 55
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 42
	%1 = load i32, i32* 3

	; <label>: c3
	br i1 true label 9f label f9

	; <label>: 9f
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label 62 label c0

	; <label>: 62
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: c0
	br label c3

	; <label>: f9
	ret i32 2
}