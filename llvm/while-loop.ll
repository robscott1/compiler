
define dso_local i32 @main(i32) {

	; <label>: ee
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 22
	%t1 = load i32, i32* 4

	; <label>: 85
	%t3 = icmp lt i1 %t1, 4
	br i1 %t3 label 2d label 91

	; <label>: 2d
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: a3
	br label 85

	; <label>: 91
	ret i32 2
}