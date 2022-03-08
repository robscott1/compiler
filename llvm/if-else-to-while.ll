%tstruct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0define dso_local i32 @foo(i32, i32) {

	; <label>: 49
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 3c
	ret i32 1
}
define dso_local i32 @main(i32) {

	; <label>: 47
	%t1 = alloca i32
	%t2 = alloca i32
	%t3 = alloca %tstruct.A*
	%t4 = alloca i32

	; <label>: 09
	%t5 = icmp lt i1 4, 5
	br i1 %t5 label e2 label 07

	; <label>: e2
	%t1 = load i32, i32* 4
	%t6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 @z)

	; <label>: ea
	%7 = icmp lt i1 4, 6
	br i1 %7 label 23 label 7a

	; <label>: 23
	%1 = load i32, i32* 1
	%8 = add i32 %1, 1
	%1 = load i32, i32* %8

	; <label>: e4
	br label ea

	; <label>: 7a
	%9 = add i32 3, %1
	%10 = mul i32 4, %9
	%11 = mul i32 %1, %10
	ret i32 %11

	; <label>: 07
	%12 = add i32 3, 2
	%2 = load i32, i32* %12
	%13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %2)
}