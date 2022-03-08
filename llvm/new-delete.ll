%struct.A = type { i32, i32 }
define dso_local i32 @main() {

	; <label>: ff
	%t1 = alloca %struct.A*

	; <label>: f8
	%t2 = call i8* @malloc(i32 8)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %struct.A* %t3, %struct.A** %t1
	%t4 = bitcast %struct.A** %t1 to i8*
	call void @free(i8* %t1)
	ret i32 3
}