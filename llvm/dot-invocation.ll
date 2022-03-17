%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L1:
%x = alloca %struct.A*
%j = alloca i32
br label %L88

L88:
store i32 4, i32* %j
%t0 = call %struct.A* @foo()
%t1 = getelementptr %struct.A, %struct.A* %t0, i32 0, i32 0
%t2 = load i32, i32* %t1
ret i32 %t2
}

define dso_local %struct.A* @foo() {

L76:
%x = alloca %struct.A*
br label %L65

L65:
%t0 = call i8* @malloc(i32 4)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
ret %struct.A* %t1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1