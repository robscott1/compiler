%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L7:
	%x = alloca i32
	%y = alloca i32
	br label %L13

L13:
	ret i32 1
}

define dso_local i32 @main(i32) {

L86:
	%a = alloca i32
	%b = alloca i32
	%x = alloca %struct.A*
	%i = alloca i32
	br label %L91

L91:
	%t0 = icmp slt i32 4, 5
	br i1 %t0, label %L83, label %L94

L83:
	store i32 4, i32* %a
	%t1 = load i32, i32* @z
	%t2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t1)
	br label %L76

L76:
	%t3 = icmp slt i32 4, 6
	br i1 %t3, label %L67, label %L71

L67:
	store i32 1, i32* %a
	%t4 = load i32, i32* %a
	%t5 = add i32 %t4, 1
	store i32 %t5, i32* %a
	br label %L35

L35:
	br label %L76
	br label %L76

L71:
	%t6 = load i32, i32* %a
	%t7 = load i32, i32* %a
	%t8 = add i32 3, %t7
	%t9 = mul i32 4, %t8
	%t10 = mul i32 %t6, %t9
	ret i32 %t10

L94:
	%t11 = add i32 3, 2
	store i32 %t11, i32* %b
	%t12 = load i32, i32* %b
	%t13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t12)
	br label %L76
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1