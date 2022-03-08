
define dso_local i32 @main(i32) {

	; <label>: e6
	%1 = alloca i32

	; <label>: 24
	%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %1)
	br i1 true label 3a label c7

	; <label>: 3a
	ret i32 2

	; <label>: c7
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 53
	ret i32 1
}