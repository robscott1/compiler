define dso_local <TYPE> @main(i32) {

	; <label>: 8a
	%1 = alloca i32

	; <label>: 2b
	%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %1)
	br i1 true label 31 label ec

	; <label>: 31
	ret i32 2

	; <label>: ec
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 7c
	ret i32 1
}