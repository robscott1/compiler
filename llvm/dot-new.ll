%struct.A = type { i32, i32, %struct.A* }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L74:
	%t0 = alloca %struct.A*
	%t1 = alloca i32
	br label %L86

L86:
	store i32 4, i32* %t1
	%t2 = load %struct.A*, %struct.A** %t0
	%t3 = bitcast %struct.A* %t2 to i8*
	call void @free(i8* %t3)
	%t4 = call i8* @malloc(i32 9)
	%t5 = bitcast i8* %t4 to %struct.A*
	%t6 = getelementptr %struct.A, %struct.A* %t5, i32 0, i32 0
	%t7 = load i32, i32* %t6
	ret i32 %t7
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1