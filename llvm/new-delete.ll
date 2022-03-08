%tstruct.A = type { i32 i32 }
define dso_local i32 @main() {

	; <label>: 69
	%t1 = alloca %tstruct.A*

	; <label>: 66
	%t2 = call i8* @malloc(i32 8)
	%t3 = bitcast i8* %t2 to %tstruct.A*
	%t1 = load %tstruct.A*, %tstruct.A** %t3
	%t4 = bitcast %tstruct.A** %t1 to i8*
	call void @free(i8* %t1)
	ret i32 3
}