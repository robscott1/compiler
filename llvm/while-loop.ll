

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

L47:
%a = alloca i32
%i = alloca i32
br label %L90

L90:
store i32 4, i32* %a
br label %L74

L74:
%t0 = phi()
%t0 = load i32, i32* %a
%t1 = icmp slt i32 %t0, 4
br i1 %t1, label %L44, label %L25

L44:
%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 1)
br label %L16

L16:
br label %L74
br label %L74

L25:
ret i32 2
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1