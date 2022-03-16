%struct.A = type { i32, i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L49:
	%t0 = alloca %struct.A*
	br label %L81

L81:
	%t1 = call i8* @malloc(i32 8)
	%t2 = bitcast i8* %t1 to %struct.A*
	store %struct.A* %t2, %struct.A** %t0
	%t3 = load %struct.A*, %struct.A** %t0
	%t4 = bitcast %struct.A* %t3 to i8*
	call void @free(i8* %t4)
	ret i32 3
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1