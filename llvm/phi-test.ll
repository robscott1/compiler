

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L55:
%g = alloca i32
%f = alloca i32
br label %L11

L11:
%t0 = add i32 4, 2
store i32 %t0, i32* %g
%t0 = load i32, i32* %g
%t1 = icmp slt i32 %t0, 5
br i1 %t1, label %L82, label %L7

L82:
store i32 8, i32* %g
br label %L73

L73:
<PhiNode.PhiNode object at 0x7f1a703d8a60> = load i32, i32* %g
%t2 = add i32 <PhiNode.PhiNode object at 0x7f1a703d8a60>, 3
store i32 %t2, i32* %f
%t2 = load i32, i32* %f
ret i32 %t2

L7:
store i32 1, i32* %g
br label %L73
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1