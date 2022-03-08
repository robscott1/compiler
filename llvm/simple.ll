
define dso_local i32 @main(i32) {

	; <label>: b9
	%t1 = alloca i32

	; <label>: 1c
	%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	ret i32 0
}