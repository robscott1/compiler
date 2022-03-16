

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L5:
%a = alloca i32
%i = alloca i32
br label %L62

L62:
store i32 4, i32* %a
br label %L94

L94:
%t0 = phi i32 [4, %L62], [%t3, %L60]
%t1 = icmp slt i32 %t0, 4
br i1 %t1, label %L8, label %L61

L8:
%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
%t3 = add i32 %t0, 1
store i32 %t3, i32* %a
br label %L60

L61:
ret i32 %t0

L60:
br label %L94
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1