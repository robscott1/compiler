
define dso_local i32 @main(i32) {

	; <label>: LABEL@fd
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: LABEL@d6
	store i32 3, i32* %t1

	; <label>: LABEL@36
	br i1 true, label LABEL@83, label LABEL@2b

	; <label>: LABEL@83
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true, label LABEL@13, label LABEL@56

	; <label>: LABEL@13
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: LABEL@56
	br label LABEL@36

	; <label>: LABEL@2b
	ret i32 2
}