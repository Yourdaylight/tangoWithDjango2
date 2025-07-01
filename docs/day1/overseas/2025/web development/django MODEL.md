# django MODEL

## sqlite

#### sqlite 与mysql

sqlite： 文档形数据库

mysql： 数据库系统（数据库服务器），访问方式依赖于http（tcp）链接

### 创建一个app

​`python manage.py startapp rango`​

‍

## ORM(Object-Relational Mapping) 对象关系映射

**Object**： 对象。类实例。 我们models中的Page ， Category。 Object是我们自己定义的

**Relational:**  关系形数据库，数据以Table的形式存储。 Relational可以理解为migrations下面生成的py文件（由makemigrations命令生成的）

**Mapping：**  执行migrate命令时生成object-Relational的映射关系。

‍

migrate命令执行完成后，它在数据库生成的table名称是 app_table（ClassName）的名称。会给关联的表中自动生成一个id属性（id被称为自增id）

 数据库中的所有字段名称或者表名称均为小写。

### 新增数据库表

​`python .\manage.py migrate`​

### 创建app的数据库表

​`python .\manage.py makemigrations rango`​

makrmigrations命令后面需要接一个已创建的app的名称。django会读取这个app名称下面的models.py. 并根据models.py定义的类，在app的migrations目录下生成一个**迁移文件**。
