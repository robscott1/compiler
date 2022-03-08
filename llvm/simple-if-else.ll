
define dso_local i32 @main(i32) {

	; <label>: LABEL@31
	%t1 = alloca i32

	; <label>: LABEL@cb
	%t2 = load i32, i32* %t1
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
	br i1 true, label LABEL@69, label LABEL@a5

	; <label>: LABEL@69
	ret i32 2

	; <label>: LABEL@a5
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: LABEL@0c
	ret i32 1
}