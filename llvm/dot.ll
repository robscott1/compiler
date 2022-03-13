%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L16:
	%t0 = alloca %struct.A*
	%t1 = alloca i32
	br label %L80

L80:
	%t2 = call i8* @malloc(i32 4)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %struct.A* %t3, %struct.A** %t0
	%t4 = load %struct.A*, %struct.A** %t0
	%t5 = getelementptr %struct.A, %struct.A* %t4, i32 0, i32 0
	%t6 = call i32 @f()
	store i32 %t6, i32* %t5
	%t7 = call i32 @f()
	%t8 = icmp slt i32 0, %t7
	br i1 %t8, label %L88, label %L19

L88:
	ret i32 4

L19:
	%t9 = load %struct.A*, %struct.A** %t0
	%t10 = getelementptr %struct.A, %struct.A* %t9, i32 0, i32 0
	%t11 = load i32, i32* %t10
	ret i32 %t11
}

define dso_local i32 @f() {

L59:
	%t0 = alloca i32
	br label %L52

L52:
	store i32 4, i32* %t0
	%t1 = load i32, i32* %t0
	ret i32 %t1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1