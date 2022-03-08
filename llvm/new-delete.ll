%struct.A = type { i32 i32 }
define dso_local i32 @main() {

	; <label>: 69
	%1 = alloca %struct.A*

	; <label>: 66
	%2 = call i8* @malloc(i32 8)
	%3 = bitcast i8* %2 to %struct.A*
	%1 = load %struct.A*, %struct.A** %3
	%4 = bitcast %struct.A** %1 to i8*
	call void @free(i8* %1)
	ret i32 3
}