%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L75:
%x = alloca %struct.A*
%j = alloca i32
br label %L20

L20:
%t0 = call i8* @malloc(i32 4)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
%t2 = load %struct.A*, %struct.A** %x
%t3 = getelementptr %struct.A, %struct.A* %t2, i32 0, i32 0
%t4 = call i32 @f()
store i32 %t4, i32* %t3
%t5 = call i32 @f()
%t6 = icmp slt i32 0, %t5
br i1 %t6, label %L18, label %L12

L18:
%t7 = call i8* @malloc(i32 4)
%t8 = bitcast i8* %t7 to %struct.A*
store %struct.A* %t8, %struct.A** %x
%t9 = load %struct.A*, %struct.A** %x
%t10 = getelementptr %struct.A, %struct.A* %t9, i32 0, i32 0
store i32 10, i32* %t10
br label %L12

L12:
%t11 = phi %struct.A* [%t8, %L18], [%t1, %L20]
%t12 = getelementptr %struct.A, %struct.A* %t11, i32 0, i32 0
%t13 = load i32, i32* %t12
ret i32 %t13
}

define dso_local i32 @f() {

L85:
%j = alloca i32
br label %L17

L17:
store i32 4, i32* %j
ret i32 4
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1