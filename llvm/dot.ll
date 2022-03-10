%struct.A = type { i32 }
define dso_local i32 @main() {

L90:
	%t1 = alloca %struct.A*
	%t2 = alloca i32
	br label %L80

L80:
	%t3 = call i32 @f()
	%t4 = icmp slt i32 0, %t3
	br i1 %t4, label %L23, label %L15

L23:
	ret i32 4

L15:
	%t5 = load %struct.A*, %struct.A** %t1
	%t6 = getelementptr %struct.A, %struct.A* %t5, i1 0, i32 0
	ret i32 %t6
}
define dso_local i32 @f() {

L65:
	%t1 = alloca i32
	br label %L14

L14:
	store i32 4, i32* %t1
	%t2 = load i32, i32* %t1
	ret i32 %t2
}