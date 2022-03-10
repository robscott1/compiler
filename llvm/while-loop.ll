
define dso_local i32 @main(i32) {

L26:
	%t1 = alloca i32
	%t2 = alloca i32
	br label %L32

L32:
	store i32 4, i32* %t1
	br label %L99

L99:
	%t3 = load i32, i32* %t1
	%t4 = icmp slt i32 %t3, 4
	br i1 %t4, label %L74, label %L91

L74:
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br label %L73

L73:
	br label %L99
	br label %L99

L91:
	ret i32 2
}