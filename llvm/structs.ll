%struct.A = type { i32, i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L83:
	%t0 = alloca %struct.A*
	%t1 = alloca i32
	br label %L77

L77:
	store i32 3, i32* %t1
	%t2 = call i8* @malloc(i32 8)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %struct.A* %t3, %struct.A** %t0
	%t4 = load %struct.A*, %struct.A** %t0
	%t5 = getelementptr %struct.A, %struct.A* %t4, i32 0, i32 0
	%t6 = load i32, i32* %t1
	store i32 %t6, i32* %t5
	%t7 = load %struct.A*, %struct.A** %t0
	%t8 = getelementptr %struct.A, %struct.A* %t7, i32 0, i32 0
	%t9 = load i32, i32* %t8
	ret i32 %t9
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1