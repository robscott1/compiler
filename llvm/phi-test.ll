

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L28:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L11

L11:
	%t2 = add i32 4, 2
	store i32 %t2, i32* %t0
	%t3 = load i32, i32* %t0
	%t4 = icmp slt i32 %t3, 5
	br i1 %t4, label %L21, label %L50

L21:
	store i32 8, i32* %t0
	br label %L84

L84:
	%t5 = load i32, i32* %t0
	%t6 = add i32 %t5, 3
	store i32 %t6, i32* %t1
	%t7 = load i32, i32* %t1
	ret i32 %t7

L50:
	store i32 1, i32* %t0
	br label %L84
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1