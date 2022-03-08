
define dso_local i32 @main(i32) {

	; <label>: 17
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: b3
	store i32 3, i32* %t1

	; <label>: 29
	br i1 true, label bf, label 7a

	; <label>: bf
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true, label f7, label 4c

	; <label>: f7
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 4c
	br label 29

	; <label>: 7a
	ret i32 2
}