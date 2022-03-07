define dso_local <TYPE> @main(i32) {

	; <label>: 8f
	%1 = alloca i32

	; <label>: 48
	%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %1)
	br i1 true label d1 label ec

	; <label>: d1
	ret i32 2

	; <label>: ec
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
}