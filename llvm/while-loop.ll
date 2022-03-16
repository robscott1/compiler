

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L2:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L77

L77:
	store i32 4, i32* %t0
	br label %L68

L68:
	%t2 = load i32, i32* %t0
	%t3 = icmp slt i32 %t2, 4
	br i1 %t3, label %L15, label %L66

L15:
	%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
	%t5 = load i32, i32* %t0
	%t6 = add i32 %t5, 1
	store i32 %t6, i32* %t0
	br label %L21

L21:
	br label %L68

L66:
	%t7 = load i32, i32* %t0
	ret i32 %t7
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1