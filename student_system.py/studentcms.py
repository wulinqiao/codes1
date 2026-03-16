from student import Student
class StudentCMS:
    def __init__(self):
        self.stu_list = []

    def show_view(self):
        print('*'*23)
        print("学生信息管理系统V2.0")
        print("\t1. 添加学生信息")
        print("\t2. 修改学生信息")
        print("\t3. 删除学生信息")
        print("\t4. 查询单个学生信息")
        print("\t5. 显示所有学生信息")
        print("\t6. 保存学生信息")
        print("\t0. 退出系统")
        print('*'*23)
        print()

    def add_student(self):
        name=input("请输入学生姓名: ")
        gender=input("请输入学生性别: ")
        age=int(input("请输入学生年龄: "))
        phonenumber=input("请输入学生电话号码: ")
        describe=input("请输入学生描述信息: ")
        stu=Student(name,gender,age,phonenumber,describe)
        self.stu_list.append(stu)
        print(f"学生 {name} 信息添加成功！")
        print()
    
    def update_student(self):
        name = input("请输入要修改的学生姓名: ")
        for stu in self.stu_list:
            if stu.name == name:
                print("找到该学生，可以进行修改。")
                new_name = input("请输入新的学生姓名: ")
                new_gender = input("请输入新的学生性别: ")
                new_age = int(input("请输入新的学生年龄: "))
                new_phonenumber = input("请输入新的学生电话号码: ")
                new_describe = input("请输入新的学生描述信息: ")
                self.stu_list.remove(stu)
                self.stu_list.append(Student(new_name, new_gender, new_age, new_phonenumber, new_describe))
                print(f"学生 {name} 信息修改成功！")
                return
        print(f"未找到姓名为 {name} 的学生。")

    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for stu in self.stu_list:
            if stu.name == name:
                self.stu_list.remove(stu)
                print(f"学生 {name} 信息删除成功！")
                return
        print(f"未找到姓名为 {name} 的学生。")

    def search_one_student(self):
        name = input("请输入要查询的学生姓名: ")
        for stu in self.stu_list:
            if stu.name == name:
                print(stu)
                return
        print(f"未找到姓名为 {name} 的学生。")

    def show_all_students(self):
        if not self.stu_list:
            print("当前没有学生信息。")
        else:
            for stu in self.stu_list:
                print(stu)
        print()
    def save_students(self):
        filename = input("请输入要保存的文件名（如 students.txt）: ")
        
    def start(self):
       
       
       
        while True:
            self.show_view()
            choice = input("请输入操作选项(0-6): ")
            if choice == '1':
                print("添加学生信息")
                self.add_student()
            elif choice == '2':
                print("修改学生信息")
                self.update_student()
            elif choice == '3':
                print("删除学生信息")
                self.delete_student()
            elif choice == '4':
                print("查询单个学生信息")
                self.search_one_student()
            elif choice == '5':
                print("显示所有学生信息")
                self.show_all_students()
            elif choice == '6':
                print("保存学生信息")
                self.save_students()
            elif choice == '0':
                result = input("您确定要退出系统吗？(y/n): ")
                if result.lower() == 'y':
                    print("感谢使用学生信息管理系统，再见！")
                    break
            else:
                print("无效的选项，请重新输入。")
