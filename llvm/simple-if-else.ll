
define dso_local i32 @main(i32) {

L6:
	%t1 = alloca i32
	br label %L49

L49:
	%t2 = load i32, i32* %t1
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
	br i1 true, label %L57, label %L56

L57:
	ret i32 2

L56:
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br label %L49

L49:
	ret i32 1
}