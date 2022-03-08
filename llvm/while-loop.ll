
define dso_local i32 @main(i32) {

	; <label>: 33
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: ff
	store i32 4, i32* %t1

	; <label>: 53
	%t3 = load i32, i32* %t1
	%t4 = icmp lt i1 %t3, 4
	br i1 %t4, label 48, label 28

	; <label>: 48
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 69
	br label 53

	; <label>: 28
	ret i32 2
}