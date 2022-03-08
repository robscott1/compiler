%tstruct.A = type { i32 i32 %tstruct.<Types.StructType.StructType object at 0x7f9b587b1190> }
define dso_local i32 @main() {

	; <label>: c1
	%t1 = alloca %tstruct.A*
	%t2 = alloca i32

	; <label>: 20
	%t2 = load i32, i32* 4
	%t3 = bitcast %tstruct.A** %t1 to i8*
	call void @free(i8* %t1)
	%t4 = call i8* @malloc(i32 9)
	%t5 = bitcast i8* %t4 to %tstruct.A*
	%t6 = getelementptr %tstruct.A*, %tstruct.A** %t5 i1 0, i32 0
	ret i32 %t6
}