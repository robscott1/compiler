

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L26:
%g = alloca i32
%f = alloca i32
br label %L28

L28:
%t0 = add i32 4, 2
store i32 %t0, i32* %g
%t1 = load i32, i32* %t0
store i32 %t1, i32* %f
%t2 = load i32, i32* %t1
%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
%t4 = load i32, i32* %t0
%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0), i32 %t4)
ret i32 3
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1