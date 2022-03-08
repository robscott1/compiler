
define dso_local i32 @main(i32) {

	; <label>: c4
	%t1 = alloca i32

	; <label>: 39
	%t2 = load i32, i32* %t1
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
	br i1 true, label f3, label 65

	; <label>: f3
	ret i32 2

	; <label>: 65
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: ef
	ret i32 1
}