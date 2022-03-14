

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32) {

L12:
%i = alloca i32
br label %L98

L98:
%t0 = phi()
%t0 = load i32, i32* %i
ret i32 %t0
}

define dso_local i32 @main(i32) {

L81:
%a = alloca i32
%i = alloca i32
br label %L25

L25:
store i32 1, i32* %a
1 = load i32, i32* %a
%t0 = icmp sgt i32 1, 0
br i1 %t0, label %L8, label %L81

L8:
ret i32 1

L81:
ret i32 1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1