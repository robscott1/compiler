%struct.A = type { i32 }
@z = common dso_local global i32 0
@a = common dso_local global i32 0

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L13:
	%t0 = alloca i32
	%t1 = alloca i32
	br label %L98

L98:
	ret i32 1
}

define dso_local i32 @main(i32) {

L97:
	%t0 = alloca i32
	%t1 = alloca i32
	%t2 = alloca %struct.A*
	%t3 = alloca i32
	br label %L73

L73:
	%t4 = icmp slt i32 4, 5
	br i1 %t4, label %L1, label %L79

L1:
	store i32 4, i32* %t0
	%t5 = load i32, i32* @z
	%t6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t5)
	br label %L46

L46:
	%t7 = icmp slt i32 4, 6
	br i1 %t7, label %L39, label %L41

L39:
	store i32 1, i32* %t0
	%t8 = load i32, i32* %t0
	%t9 = add i32 %t8, 1
	store i32 %t9, i32* %t0
	br label %L16

L16:
	br label %L46
	br label %L46

L41:
	%t10 = load i32, i32* %t0
	%t11 = load i32, i32* %t0
	%t12 = add i32 3, %t11
	%t13 = mul i32 4, %t12
	%t14 = mul i32 %t10, %t13
	ret i32 %t14

L79:
	%t15 = add i32 3, 2
	store i32 %t15, i32* %t1
	%t16 = load i32, i32* %t1
	%t17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t16)
	br label %L46
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1