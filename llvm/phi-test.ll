

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L95:
%g = alloca i32
%f = alloca i32
br label %L17

L17:
%t0 = add i32 4, 2
store i32 %t0, i32* %g
%t0 = load i32, i32* %g
%t1 = icmp slt i32 %t0, 5
br i1 %t1, label %L58, label %L50

L58:
store i32 8, i32* %g
br label %L13

L13:
%t2 = phi()
%t2 = load i32, i32* %g
%t3 = add i32 %t2, 3
store i32 %t3, i32* %f
%t3 = load i32, i32* %f
ret i32 %t3

L50:
store i32 1, i32* %g
br label %L13
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1