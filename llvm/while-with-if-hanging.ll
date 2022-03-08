
define dso_local i32 @main(i32) {

	; <label>: ce
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: b2
	store i32 3, i32* %t1

	; <label>: ca
	br i1 true label 1f label 5b

	; <label>: 1f
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true label c9 label 0f

	; <label>: c9
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 0f
	br label ca

	; <label>: 5b
	ret i32 2
}