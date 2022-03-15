

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32) {

L24:
%i = alloca i32
br label %L79

L79:
%t0 = load i32, i32* None
ret i32 %t0
}

define dso_local i32 @main(i32) {

L93:
%a = alloca i32
%i = alloca i32
br label %L18

L18:
store i32 1, i32* %a
%t0 = load i32, i32* 1
%t1 = icmp sgt i32 %t0, 0
br i1 %t1, label %L93, label %L7

L7:
ret i32 1
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1