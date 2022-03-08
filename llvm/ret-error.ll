
define dso_local i32 @main(i32) {

	; <label>: LABEL@6b
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: LABEL@a6
	store i32 3, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp sgt i1 %t3, 0
	br i1 %t4, label LABEL@87, label LABEL@0f

	; <label>: LABEL@87
	ret i32 2

	; <label>: LABEL@0f
	%t5 = load i32, i32* %t1
	%t6 = icmp slt i1 %t5, 0
	br i1 %t6, label LABEL@b4, label LABEL@37

	; <label>: LABEL@b4
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: LABEL@37
	ret i32 0
}