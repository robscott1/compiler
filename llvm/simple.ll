define dso_local <TYPE> @main(i32) {

	; <label>: 8d
	%1 = alloca i32

	; <label>: 59
	%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	ret i32 0
}