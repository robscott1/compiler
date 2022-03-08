%tstruct.A = type { i32 i32 }
define dso_local i32 @main() {

	; <label>: 56
	%t1 = alloca %struct.A*

	; <label>: c0
	%t2 = call i8* @malloc(i32 8)
	%t3 = bitcast i8* %t2 to %struct.A*
	store %t3 %struct.A*, %struct.A** %t1
	%t4 = bitcast %struct.A** %t1 to i8*
	call void @free(i8* %t1)
	ret i32 3
}