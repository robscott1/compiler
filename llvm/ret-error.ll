
define dso_local i32 @main(i32) {

L58:
	%t1 = alloca i32
	%t2 = alloca i32
	br label %L84

L84:
	store i32 3, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp sgt i32 %t3, 0
	br i1 %t4, label %L30, label %L85

L30:
	ret i32 2

L85:
	%t5 = load i32, i32* %t1
	%t6 = icmp slt i32 %t5, 0
	br i1 %t6, label %L15, label %L21

L15:
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)

L21:
	ret i32 0
}