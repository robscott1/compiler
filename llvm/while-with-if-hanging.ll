
define dso_local i32 @main(i32) {

	; <label>: ae
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: b4
	store i32 3, i32* %t1

	; <label>: 48
	br i1 true, label 97, label 29

	; <label>: 97
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true, label f0, label b9

	; <label>: f0
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: b9
	br label 48

	; <label>: 29
	ret i32 2
}