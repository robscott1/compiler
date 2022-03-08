
define dso_local i32 @main(i32) {

	; <label>: ee
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 22
	%1 = load i32, i32* 4

	; <label>: 85
	%3 = icmp lt i1 %1, 4
	br i1 %3 label 2d label 91

	; <label>: 2d
	%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: a3
	br label 85

	; <label>: 91
	ret i32 2
}