

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main(i32) {

<<<<<<< HEAD:llvm/addition.ll
L65:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L17

L17:
	%t2 = add i32 4, 2
	store i32 %t2, i32* %t0
	%t3 = load i32, i32* %t0
	store i32 %t3, i32* %t1
	%t4 = load i32, i32* %t1
	%t5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t4)
	%t6 = load i32, i32* %t0
	%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t6)
	ret i32 3
=======
L64:
%a = alloca i32
%i = alloca i32
br label %L24

L24:
store i32 1, i32* %a
%t0 = icmp sgt i32 1, 0
br i1 %t0, label %L19, label %L24

L19:
ret i32 1
>>>>>>> ff18075d4211711693276c37fb5089cb7d44c407:llvm/ret-error.ll
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1