%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0define dso_local i32 @foo(i32, i32) {

	; <label>: c5
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 4f
	ret i32 1
}
define dso_local i32 @main(i32) {

	; <label>: 0e
	%t1 = alloca i32
	%t2 = alloca i32
	%t3 = alloca %struct.A*
	%t4 = alloca i32

	; <label>: 00
	%t5 = icmp lt i1 4, 5
	br i1 %t5, label c5, label 50

	; <label>: c5
	store i32 4, i32* %t1
	%t6 = load i32, i32* @z
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t6)

	; <label>: aa
	%t8 = icmp lt i1 4, 6
	br i1 %t8, label f9, label af

	; <label>: f9
	store i32 1, i32* %t1
	%t9 = load i32, i32* %t1
	%t10 = add i32 %t9, 1
	store i32 %t10, i32* %t1

	; <label>: 60
	br label aa

	; <label>: af
	%t11 = load i32, i32* %t1
	%t12 = load i32, i32* %t1
	%t13 = add i32 3, %t12
	%t14 = mul i32 4, %t13
	%t15 = mul i32 %t11, %t14
	ret i32 %t15

	; <label>: 50
	%t16 = add i32 3, 2
	store i32 %t16, i32* %t2
	%t17 = load i32, i32* %t2
	%t18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t17)
}