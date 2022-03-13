

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L74:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L51

L51:
	store i32 4, i32* %t0
	br label %L60

L60:
	%t2 = load i32, i32* %t0
	%t3 = icmp slt i32 %t2, 4
	br i1 %t3, label %L55, label %L22

L55:
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	br label %L56

L56:
	br label %L60
	br label %L60

L22:
	ret i32 2
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1