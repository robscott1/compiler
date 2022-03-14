%struct.A = type { i32, i32 }

@.str = private unnamed_addr constant [3 x i8] c"%d\00"
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@READ_MEM = common global i32 0
define dso_local i32 @main() {

L73:
%x = alloca %struct.A*
br label %L25

L25:
%t0 = call i8* @malloc(i32 8)
%t1 = bitcast i8* %t0 to %struct.A*
store %struct.A* %t1, %struct.A** %x
%t1 = load %struct.A*, %struct.A** %x
%t2 = bitcast %struct.A* %t1 to i8*
call void @free(i8* %t2)
ret i32 3
}


declare dso_local void @free(i8*) #1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i8* @malloc(i32) #1
declare dso_local i32 @__isoc99__scanf(i8*, ...) #1