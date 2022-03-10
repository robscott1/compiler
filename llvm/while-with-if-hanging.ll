
define dso_local i32 @main(i32) {

L48:
	%t1 = alloca i32
	%t2 = alloca i32
	br label %L16

L16:
	store i32 3, i32* %t1
	br label %L45

L45:
	br i1 true, label %L58, label %L57

L58:
	%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br i1 true, label %L79, label %L65

L79:
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br label %L65

L65:
	br label %L45
	br label %L45

L57:
	ret i32 2
}