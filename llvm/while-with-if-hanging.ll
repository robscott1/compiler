
define dso_local i32 @main(i32) {

	; <label>: 12
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 91
	store 3 i32, i32* %t1

	; <label>: 1d
	br i1 true label 6a label 12

	; <label>: 6a
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label 98 label fb

	; <label>: 98
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: fb
	br label 1d

	; <label>: 12
	ret i32 2
}