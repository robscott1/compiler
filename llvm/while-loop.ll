

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L31:
%a = alloca i32
%i = alloca i32
br label %L96

L96:
store i32 4, i32* %a
br label %L45

L45:
%t1 = phi()
%t2 = icmp slt i32 %t1, 4
br i1 %t2, label %L72, label %L36

L72:
%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
%t4 = load i32, i32* %t1
%t5 = add i32 %t4, 1
store i32 %t5, i32* %a
br label %L23

L36:
ret i32 2

L23:
br label %L45
br label %L45
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1