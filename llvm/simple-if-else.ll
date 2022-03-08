
define dso_local i32 @main(i32) {

	; <label>: df
	%t1 = alloca i32

	; <label>: 41
	%t2 = load i32, i32* %t1
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
	br i1 true, label ed, label a5

	; <label>: ed
	ret i32 2

	; <label>: a5
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 52
	ret i32 1
}