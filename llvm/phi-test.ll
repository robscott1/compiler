

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L13:
%g = alloca i32
%f = alloca i32
br label %L100

L100:
%t0 = add i32 4, 2
store i32 %t0, i32* %g
%t1 = load i32, i32* %t0
%t2 = icmp slt i32 %t1, 5
br i1 %t2, label %L7, label %L29

L7:
store i32 8, i32* %g
br label %L9

L29:
store i32 1, i32* %g
br label %L9

L9:
%t4 = phi([8, %L7] [1, %L29])
%t5 = add i32 %t4, 3
store i32 %t5, i32* %f
%t6 = load i32, i32* %t5
ret i32 %t6
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1