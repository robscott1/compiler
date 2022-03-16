

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L56:
%g = alloca i32
%f = alloca i32
br label %L86

L86:
%t0 = add i32 4, 2
store i32 %t0, i32* %g
%t2 = icmp slt i32 %t0, 5
br i1 %t2, label %L5, label %L7

L5:
store i32 8, i32* %g
br label %L61

L7:
store i32 1, i32* %g
br label %L61

L61:
%t4 = phi i32 [8, %L5], [1, %L7]
%t5 = add i32 %t4, 3
store i32 %t5, i32* %f
ret i32 %t5
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1