

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32) {

L24:
%i = alloca i32
br label %L50

L50:
ret i32 %i
}

define dso_local i32 @main(i32) {

L67:
%a = alloca i32
%i = alloca i32
br label %L10

L10:
store i32 1, i32* %a
%t1 = icmp sgt i32 1, 0
br i1 %t1, label %L35, label %L74

L35:
ret i32 1

L74:
ret i32 1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1