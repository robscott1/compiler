%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L62:
%x = alloca i32
%y = alloca i32
br label %L97

L97:
ret i32 1
}

define dso_local i32 @main(i32) {

L20:
%a = alloca i32
%b = alloca i32
%x = alloca %struct.A*
%i = alloca i32
br label %L80

L80:
store i32 4, i32* %a
%t0 = icmp slt i32 4, 5
br i1 %t0, label %L10, label %L77

L10:
store i32 4, i32* %a
%t1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 4)
br label %L31

L77:
%t2 = add i32 3, 2
store i32 %t2, i32* %b
%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
br label %L31

L31:
%t6 = phi i32 [4, %L80], [4, %L10], [%t9, %L78]
%t7 = icmp slt i32 %t6, 6
br i1 %t7, label %L78, label %L19

L78:
%t9 = add i32 %t6, 1
store i32 %t9, i32* %a
br label %L6

L19:
%t12 = add i32 3, %t6
%t13 = mul i32 4, %t12
%t14 = mul i32 %t6, %t13
ret i32 %t14

L6:
br label %L31
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1