%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L97:
	%t0 = alloca %struct.A*
	%t1 = alloca i32
	br label %L72

L72:
	store i32 4, i32* %t1
	%t2 = call %struct.A* @foo()
	%t3 = getelementptr %struct.A, %struct.A* %t2, i32 0, i32 0
	%t4 = load i32, i32* %t3
	ret i32 %t4
}

define dso_local %struct.A* @foo() {

L95:
	%t0 = alloca %struct.A*
	br label %L83

L83:
	%t1 = load %struct.A*, %struct.A** %t0
	ret %struct.A* %t1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1