%struct.A = type { i32, i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L98:
%x = alloca i32
br label %L33

L33:
%t0 = call i32 (i8*, ...) @__isoc99__scanf(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0), i32* @READ_MEM)
%t1 = load i32, i32* @READ_MEM
store i32 %t1, i32* %x
ret i32 3
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1