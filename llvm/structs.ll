%struct.A = type { i32, i32 }
define dso_local i32 @main() {

	; <label>: LABEL@66
	%t1 = alloca %struct.A*
	%t2 = alloca i32

	; <label>: LABEL@f1
	store i32 3, i32* %t2
	%t3 = call i8* @malloc(i32 8)
	%t4 = bitcast i8* %t3 to %struct.A*
	store %struct.A* %t4, %struct.A** %t1
	%t5 = load %struct.A*, %struct.A** %t1
	%t6 = getelementptr %struct.A, %struct.A* %t5 i1 0, i32 0
	%t7 = load i32, i32* %t2
	store i32 %t7, i32* %t6
	%t8 = load %struct.A*, %struct.A** %t1
	%t9 = getelementptr %struct.A, %struct.A* %t8 i1 0, i32 0
	ret i32 %t9
}