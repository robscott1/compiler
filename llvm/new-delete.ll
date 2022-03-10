%struct.A = type { i32, i32 }
define dso_local i32 @main() {

L30:
	%t1 = alloca %struct.A*
	br label %L29

L29:
	%t2 = call i8* @malloc(i32 8)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %struct.A* %t3, %struct.A** %t1
	%t4 = load %struct.A*, %struct.A** %t1
	%t5 = bitcast %struct.A* %t4 to i8*
	call void @free(i8* %t4)
	ret i32 3
}