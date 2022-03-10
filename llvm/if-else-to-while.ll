%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0define dso_local i32 @foo(i32, i32) {

L10:
	%t1 = alloca i32
	%t2 = alloca i32
	br label %L97

L97:
	ret i32 1
}
define dso_local i32 @main(i32) {

L17:
	%t1 = alloca i32
	%t2 = alloca i32
	%t3 = alloca %struct.A*
	%t4 = alloca i32
	br label %L9

L9:
	%t5 = icmp slt i32 4, 5
	br i1 %t5, label %L48, label %L32

L48:
	store i32 4, i32* %t1
	%t6 = load i32, i32* @z
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t6)
	br label %L67

L67:
	%t8 = icmp slt i32 4, 6
	br i1 %t8, label %L60, label %L9

L60:
	store i32 1, i32* %t1
	%t9 = load i32, i32* %t1
	%t10 = add i32 %t9, 1
	store i32 %t10, i32* %t1
	br label %L57

L57:
	br label %L67
	br label %L67

L9:
	%t11 = load i32, i32* %t1
	%t12 = load i32, i32* %t1
	%t13 = add i32 3, %t12
	%t14 = mul i32 4, %t13
	%t15 = mul i32 %t11, %t14
	ret i32 %t15

L32:
	%t16 = add i32 3, 2
	store i32 %t16, i32* %t2
	%t17 = load i32, i32* %t2
	%t18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t17)
	br label %L67
}