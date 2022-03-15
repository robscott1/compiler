%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L28:
%x = alloca %struct.A*
%j = alloca i32
br label %L87

L87:
%t0 = call i8* @malloc(i32 4)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
%t2 = load %struct.A*, %struct.A** %x
%t3 = getelementptr %struct.A, %struct.A* %t2, i32 0, i32 0
%t4 = call i32 @f()
store i32 %t4, i32* %t3
%t5 = call i32 @f()
%t6 = icmp slt i32 0, %t5
br i1 %t6, label %L40, label %L14

L40:
ret i32 4

L14:
%t7 = load %struct.A*, %struct.A** %t1
%t8 = getelementptr %struct.A, %struct.A* %t7, i32 0, i32 0
%t9 = load i32, i32* %t8
ret i32 %t9
}

define dso_local i32 @f() {

L46:
%j = alloca i32
br label %L91

L91:
store i32 4, i32* %j
%t0 = load i32, i32* 4
ret i32 %t0
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1