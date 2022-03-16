%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L100:
	%t0 = alloca %struct.A*
	%t1 = alloca i32
	br label %L23

L23:
	%t2 = call i8* @malloc(i32 4)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %struct.A* %t3, %struct.A** %t0
	%t4 = load %struct.A*, %struct.A** %t0
	%t5 = getelementptr %struct.A, %struct.A* %t4, i32 0, i32 0
	%t6 = call i32 @f()
	store i32 %t6, i32* %t5
	%t7 = call i32 @f()
	%t8 = icmp slt i32 0, %t7
	br i1 %t8, label %L96, label %L71

L96:
	%t9 = call i8* @malloc(i32 4)
	%t10 = bitcast i8* %t9 to %struct.A*
	store %struct.A* %t10, %struct.A** %t0
	%t11 = load %struct.A*, %struct.A** %t0
	%t12 = getelementptr %struct.A, %struct.A* %t11, i32 0, i32 0
	store i32 10, i32* %t12
	br label %L71

L71:
	%t13 = load %struct.A*, %struct.A** %t0
	%t14 = getelementptr %struct.A, %struct.A* %t13, i32 0, i32 0
	%t15 = load i32, i32* %t14
	ret i32 %t15
}

define dso_local i32 @f() {

L18:
	%t0 = alloca i32
	br label %L73

L73:
	store i32 4, i32* %t0
	%t1 = load i32, i32* %t0
	ret i32 %t1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1