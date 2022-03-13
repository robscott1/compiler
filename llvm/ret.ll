

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32) {

L87:
	%t0 = alloca i32
	br label %L12

L12:
	%t1 = load i32, i32* %t0
	ret i32 %t1
}

define dso_local i32 @main(i32) {

L97:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L28

L28:
	store i32 1, i32* %t0
	%t2 = load i32, i32* %t0
	%t3 = icmp sgt i32 %t2, 0
	br i1 %t3, label %L10, label %L71

L10:
	ret i32 1

L71:
	ret i32 1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1