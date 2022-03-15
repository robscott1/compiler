%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L46:
%x = alloca %struct.A*
%j = alloca i32
br label %L3

L3:
%t0 = call i8* @malloc(i32 4)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
%t2 = load %struct.A*, %struct.A** %x
%t3 = getelementptr %struct.A, %struct.A* %t2, i32 0, i32 0
%t4 = call i32 @f()
store i32 %t4, i32* %t3
%t5 = call i32 @f()
%t6 = icmp slt i32 0, %t5
br i1 %t6, label %L43, label %L57

L43:
%t7 = call i8* @malloc(i32 4)
%t8 = bitcast i8* %t7 to %struct.A*
store %struct.A* %t8, %struct.A** %x
%t9 = load %struct.A*, %struct.A** %x
%t10 = getelementptr %struct.A, %struct.A* %t9, i32 0, i32 0
store i32 10, i32* %t10
br label %L57

L57:
%t12 = phi %struct.A* ([%t1, %L3] [%t8, %L43])
%t13 = getelementptr %struct.A, %struct.A* %t12, i32 0, i32 0
%t14 = load i32, i32* %t13
ret i32 %t14
}

define dso_local i32 @f() {

L12:
%j = alloca i32
br label %L76

L76:
store i32 4, i32* %j
%t0 = load i32, i32* 4
ret i32 %t0
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1