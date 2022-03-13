

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L88:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L50

L50:
	%t2 = add i32 4, 2
	store i32 %t2, i32* %t0
	%t3 = load i32, i32* %t0
	store i32 %t3, i32* %t1
	ret i32 3
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1