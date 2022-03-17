%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L45:
%x = alloca i32
%y = alloca i32
br label %L35

L35:
ret i32 1
}

define dso_local i32 @main(i32) {

L71:
%a = alloca i32
%b = alloca i32
%x = alloca %struct.A*
%i = alloca i32
br label %L69

L69:
store i32 4, i32* %a
%t0 = icmp slt i32 4, 5
br i1 %t0, label %L39, label %L39

L39:
store i32 4, i32* %a
%t1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 4)
br label %L55

L55:
%t2 = phi i32 [4, %L39], [4, %L39], [%t4, %L83]
%t3 = icmp slt i32 %t2, 6
br i1 %t3, label %L6, label %L16

L6:
%t4 = add i32 %t2, 1
store i32 %t4, i32* %a
br label %L83

L16:
%t5 = add i32 3, %t2
%t6 = mul i32 4, %t5
%t7 = mul i32 %t2, %t6
ret i32 %t7

L83:
br label %L55
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1