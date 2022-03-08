%struct.A = type { i32 i32 %struct.<Types.StructType.StructType object at 0x7f9b587b1190> }
define dso_local i32 @main() {

	; <label>: c1
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: 20
	%2 = load i32, i32* 4
	%3 = bitcast %struct.A** %1 to i8*
	call void @free(i8* %1)
	%4 = call i8* @malloc(i32 9)
	%5 = bitcast i8* %4 to %struct.A*
	%6 = getelementptr %struct.A*, %struct.A** %5 i1 0, i32 0
	ret i32 %6
}