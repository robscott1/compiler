
define dso_local i32 @main(i32) {

	; <label>: 8d
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 07
	%t1 = load i32, i32* 3

	; <label>: b6
	br i1 true label 7a label 40

	; <label>: 7a
	%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label 2f label 7e

	; <label>: 2f
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 7e
	br label b6

	; <label>: 40
	ret i32 2
}