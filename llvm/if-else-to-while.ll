%struct.A = type { i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @foo(i32, i32) {

L37:
%x = alloca i32
%y = alloca i32
br label %L68

L68:
ret i32 1
}

define dso_local i32 @main(i32) {

L95:
%a = alloca i32
%b = alloca i32
%x = alloca %struct.A*
%i = alloca i32
br label %L86

L86:
store i32 4, i32* %a
%t0 = icmp slt i32 4, 5
br i1 %t0, label %L7, label %L87

L7:
store i32 4, i32* %a
%t1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 4)
br label %L84

L87:
%t2 = add i32 3, 2
store i32 %t2, i32* %b
%t3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %t2)
br label %L84

L84:
%t4 = phi i32 [4, %L87], [4, %L7], [%t6, %L4]
%t5 = icmp slt i32 %t4, 6
br i1 %t5, label %L67, label %L97

L67:
%t6 = add i32 %t4, 1
store i32 %t6, i32* %a
br label %L4

L97:
%t7 = add i32 3, %t4
%t8 = mul i32 4, %t7
%t9 = mul i32 %t4, %t8
ret i32 %t9

L4:
br label %L84
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1