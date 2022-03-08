
define dso_local i32 @main(i32) {

	; <label>: 43
	%t1 = alloca i32

	; <label>: fd
	%t2 = load i32, i32* %t1
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
	br i1 true label 2d label 45

	; <label>: 2d
	ret i32 2

	; <label>: 45
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 2e
	ret i32 1
}