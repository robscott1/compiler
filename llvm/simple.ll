define dso_local <TYPE> @main(i32) {

	; <label>: b9
	%1 = alloca i32

	; <label>: c5
	%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	ret i32 0
}