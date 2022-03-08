
define dso_local i32 @main(i32) {

	; <label>: LABEL@72
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: LABEL@2f
	store i32 4, i32* %t1

	; <label>: LABEL@dd
	%t3 = load i32, i32* %t1
	%t4 = icmp slt i1 %t3, 4
	br i1 %t4, label LABEL@da, label LABEL@e7

	; <label>: LABEL@da
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: LABEL@e4
	br label LABEL@dd

	; <label>: LABEL@e7
	ret i32 2
}