%struct.A = type { i32, i32, %struct.<Types.StructType.StructType object at 0x7f8560eea100> }
define dso_local i32 @main() {

	; <label>: 10
	%t1 = alloca %struct.A*
	%t2 = alloca i32

	; <label>: 2b
	store i32 4, i32* %t2
	%t3 = load %struct.A*, %struct.A** %t1
	%t4 = bitcast %struct.A** %t3 to i8*
	call void @free(i8* %t3)
	%t5 = call i8* @malloc(i32 9)
	%t6 = bitcast i8* %t5 to %struct.A*
	%t7 = getelementptr %struct.A, %struct.A* %t6 i1 0, i32 0
	ret i32 %t7
}