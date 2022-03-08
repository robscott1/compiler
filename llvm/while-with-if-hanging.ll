
define dso_local i32 @main(i32) {

	; <label>: 36
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 88
	store 3 i32, i32* %t1

	; <label>: 3e
	br i1 true label 14 label 22

	; <label>: 14
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label 6e label 73

	; <label>: 6e
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 73
	br label 3e

	; <label>: 22
	ret i32 2
}