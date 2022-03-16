

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L15:
%a = alloca i32
%i = alloca i32
br label %L76

L76:
store i32 4, i32* %a
br label %L68

L68:
%t0 = phi i32 [4, %L76], [%t3, %L22]
%t1 = icmp slt i32 %t0, 4
br i1 %t1, label %L55, label %L98

L55:
%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
%t3 = add i32 %t0, 1
store i32 %t3, i32* %a
br label %L22

L98:
ret i32 %t0

L22:
br label %L68
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1