%struct.A = type { i32 }@z = common dso_local global i32 0
@a = common dso_local global i32 0define dso_local <TYPE> @foo(i32, i32) {

	; <label>: 14
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 90
	ret i32 1
}
define dso_local <TYPE> @main(i32) {

	; <label>: c4
	%1 = alloca i32
	%2 = alloca i32
	%3 = alloca %struct.A*
	%4 = alloca i32

	; <label>: 36
	%5 = icmp lt i1 4, 5
	br i1 %5 label 3f label 22

	; <label>: 3f
	%1 = load i32, i32* 4
	%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 @z)

	; <label>: 3a
	%7 = icmp lt i1 4, 6
	br i1 %7 label fe label 5d

	; <label>: fe
	%1 = load i32, i32* 1
	%8 = add i32 %1, 1
	%1 = load i32, i32* %8

	; <label>: ac
	br label 3a

	; <label>: 5d
	%9 = add i32 3, %1
	%10 = mul i32 4, %9
	%11 = mul i32 %1, %10
	ret i32 %11

	; <label>: 22
	%12 = add i32 3, 2
	%2 = load i32, i32* %12
	%13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %2)
}