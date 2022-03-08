
define dso_local i32 @main(i32) {

	; <label>: 09
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 7a
	store i32 4, i32* %t1

	; <label>: e4
	%t3 = load i32, i32* %t1
	%t4 = icmp slt i1 %t3, 4
	br i1 %t4, label 9f, label 99

	; <label>: 9f
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: 2b
	br label e4

	; <label>: 99
	ret i32 2
}