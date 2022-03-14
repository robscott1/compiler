%struct.A = type { i32, i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L55:
%a = alloca %struct.A*
%l = alloca i32
br label %L56

L56:
store i32 3, i32* %l
%t0 = call i8* @malloc(i32 8)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %a
%t2 = load %struct.A*, %struct.A** %a
%t3 = getelementptr %struct.A, %struct.A* %t2, i32 0, i32 0
%t4 = load i32, i32* 3
store i32 %t4, i32* %t3
%t5 = load %struct.A*, %struct.A** %t1
%t6 = getelementptr %struct.A, %struct.A* %t5, i32 0, i32 0
%t7 = load i32, i32* %t6
ret i32 %t7
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1