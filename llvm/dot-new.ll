%struct.A = type { i32, i32, %struct.<Types.StructType.StructType object at 0x7f547249a100> }
define dso_local i32 @main() {

	; <label>: 77
	%t1 = alloca %struct.A*
	%t2 = alloca i32

	; <label>: 4b
	store i32 4, i32* %t2
	%t3 = bitcast %struct.A** %t1 to i8*
	call void @free(i8* %t1)
	%t4 = call i8* @malloc(i32 9)
	%t5 = bitcast i8* %t4 to %struct.A*
	%t6 = getelementptr %struct.A, %struct.A** %t5 i1 0, i32 0
	ret i32 %t6
}