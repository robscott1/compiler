
define dso_local i32 @main(i32) {

	; <label>: c1
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: fc
	store 3 i32, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp gt i1 %t3, 0
	br i1 %t4 label b2 label ac

	; <label>: b2
	ret i32 2

	; <label>: ac
	%t5 = load i32, i32* %t1
	%t6 = icmp lt i1 %t5, 0
	br i1 %t6 label ae label d6

	; <label>: ae
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

	; <label>: d6
	ret i32 0
}