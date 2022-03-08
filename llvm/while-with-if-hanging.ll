
define dso_local i32 @main(i32) {

	; <label>: 5a
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 20
	store i32 3, i32* %t1

	; <label>: ad
	br i1 true, label 7e, label e1

	; <label>: 7e
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true, label fd, label 9e

	; <label>: fd
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 9e
	br label ad

	; <label>: e1
	ret i32 2
}