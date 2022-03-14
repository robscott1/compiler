%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L66:
%x = alloca i32
%y = alloca i32
br label %L16

L16:
ret i32 1
}

define dso_local i32 @main(i32) {

L66:
%a = alloca i32
%b = alloca i32
%x = alloca %struct.A*
%i = alloca i32
br label %L98

L98:
%t0 = icmp slt i32 4, 5
br i1 %t0, label %L65, label %L25

L65:
%t1 = phi()
store i32 4, i32* %a
%t1 = load i32, i32* @z
%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t1)
br label %L59

L59:
%t3 = icmp slt i32 4, 6
br i1 %t3, label %L60, label %L66

L60:
store i32 1, i32* %a
1 = load i32, i32* %a
%t4 = add i32 1, 1
store i32 %t4, i32* %a
br label %L85

L85:
br label %L59
br label %L59

L66:
%t6 = phi()
%t6 = phi()
%t5 = load i32, i32* %a
%t6 = load i32, i32* %a
%t7 = add i32 3, %t6
%t8 = mul i32 4, %t7
%t9 = mul i32 %t5, %t8
ret i32 %t9

L25:
%t10 = add i32 3, 2
store i32 %t10, i32* %b
%t10 = load i32, i32* %b
%t11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t10)
br label %L59
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1