%struct.A = type { i32, i32, %struct.A* }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L56:
%x = alloca %struct.A*
%j = alloca i32
br label %L31

L31:
store i32 4, i32* %j
%t0 = call i8* @malloc(i32 9)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
%t2 = bitcast %struct.A* %t1 to i8*
call void @free(i8* %t2)
%t3 = call i8* @malloc(i32 9)
%t4 = bitcast i8* %t3 to %struct.A*
%t5 = getelementptr %struct.A, %struct.A* %t4, i32 0, i32 0
%t6 = load i32, i32* %t5
ret i32 %t6
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1