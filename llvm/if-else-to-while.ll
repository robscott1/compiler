%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L37:
%x = alloca i32
%y = alloca i32
br label %L99

L99:
ret i32 1
}

define dso_local i32 @main(i32) {

L41:
%a = alloca i32
%b = alloca i32
%x = alloca %struct.A*
%i = alloca i32
br label %L66

L66:
%t0 = icmp slt i32 4, 5
br i1 %t0, label %L74, label %L78

L74:
store i32 4, i32* %a
%t1 = load i32, i32* None
%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t1)
br label %L12

L78:
%t3 = add i32 3, 2
store i32 %t3, i32* %b
%t4 = load i32, i32* %t3
%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t4)
br label %L12

L12:
%t6 = icmp slt i32 4, 6
br i1 %t6, label %L82, label %L12

L82:
store i32 1, i32* %a
%t7 = load i32, i32* 1
%t8 = add i32 %t7, 1
store i32 %t8, i32* %a
br label %L26

L26:
br label %L12
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1