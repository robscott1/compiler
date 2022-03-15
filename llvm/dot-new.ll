%struct.A = type { i32, i32, %struct.A* }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L76:
%x = alloca %struct.A*
%j = alloca i32
br label %L61

L61:
store i32 4, i32* %j
%t0 = load %struct.A*, %struct.A** None
%t1 = bitcast %struct.A* %t0 to i8*
call void @free(i8* %t1)
%t2 = call i8* @malloc(i32 9)
%t3 = bitcast i8* %t2 to %struct.A*
%t4 = getelementptr %struct.A, %struct.A* %t3, i32 0, i32 0
%t5 = load i32, i32* %t4
ret i32 %t5
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1