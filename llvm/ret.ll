

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32) {

L42:
	%t0 = alloca i32
	br label %L10

L10:
	store i32 1, i32* %t0
	%t1 = load i32, i32* %t0
	ret i32 %t1
}

define dso_local i32 @main(i32) {

L7:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L95

L95:
	store i32 1, i32* %t0
	%t2 = load i32, i32* %t0
	%t3 = icmp sgt i32 %t2, 0
	br i1 %t3, label %L100, label %L51

L100:
	ret i32 1

L51:
	ret i32 1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1